<template>
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex flex-wrap justify-center gap-4 my-4">
      <HMSelect
        name="Position"
        :options="positionsArray"
        :disabledOptions="disabledPositions"
        :value="position"
        @change="handlePositionChange"
      />
      <HMSelect
        name="Showdown Cards"
        :options="showdownCardsArray"
        :disabledOptions="disabledShowdownCards"
        :value="showdownCards"
        @change="handleComboChange"
      />
      <HMSelect
        name="Simple Suitedness"
        :options="simpleSuitednessArray"
        :disabledOptions="disabledSimpleSuitedness"
        :value="simpleSuit"
        @change="handleSuitChange"
      />
      <HMSelect
        name="Detailed Suitedness"
        :options="detailedSuitednessArray"
        :disabledOptions="disabledDetailedSuitedness"
        :value="detailedSuit"
        @change="handleDetailChange"
      />
    </div>
    <div class="flex justify-center my-8">
      <div
        v-if="heatmap"
        :style="gridStyle"
        class="shadow-lg rounded-lg overflow-hidden border-2"
      >
        <div
          v-for="(row, rowIndex) in heatmap"
          :key="rowIndex"
          class="grid-row"
        >
          <ComboCell
            v-for="(col, colIndex) in row"
            :key="colIndex"
            :combo="col[0]"
            :class="col[1]"
            :column="rowIndex + colIndex + 1"
          />
        </div>
      </div>
      <NoDataMessage
        v-else
        text="Enter parameters to view a Heatmap!"
        class="text-gray-600"
      />
    </div>
  </div>
  <Legend />
</template>

<script>
import ComboCell from "./ComboCell.vue";
import Legend from "./Legend.vue";
import HMSelect from "./HMSelect.vue";
import axios from "axios";
import NoDataMessage from "./NoDataMessage.vue";
import dataMixin from "../mixins/dataMixin";

export default {
  name: "Heatmaps",
  mixins: [dataMixin],
  components: { NoDataMessage, HMSelect, ComboCell, Legend },
  data() {
    return {
      position: "1",
      showdownCards: "AK",
      simpleSuit: "ss",
      detailedSuit: "wxyx",
      heatmap: null,
    };
  },
  methods: {
    handlePositionChange(value) {
      this.position = value;
      this.sendPostRequest();
    },
    handleComboChange(value) {
      this.showdownCards = value;
      this.sendPostRequest();
    },
    handleSuitChange(value) {
      this.simpleSuit = value;
      if (value === "rb" || value === "4s") {
        this.detailedSuit = this.simpleDetailArray[value][0];
      } else if (!this.simpleDetailArray[value].includes(this.detailedSuit)) {
        this.detailedSuit = this.simpleDetailArray[value][0];
      }
      this.sendPostRequest();
    },
    handleDetailChange(value) {
      this.detailedSuit = value;
      if (value === "wxyz") this.simpleSuit = "rb";
      else if (value === "wwww") this.simpleSuit = "4s";
      this.sendPostRequest();
    },
    async sendPostRequest() {
      try {
        const response = await axios.post(
          `${import.meta.env.VITE_BASE_URL}/heatmap`,
          {
            stack_size: "100",
            rake_structure: "2.5_1.5bb",
            players: "6",
            position: this.position,
            showdown_cards: this.showdownCards,
            simple_suit: this.simpleSuit,
            detailed_suit: this.detailedSuit,
          },
          { headers: { "Content-Type": "application/json" } },
        );
        let map = JSON.parse(response.data.map);
        // For each map, it it is not 13 columns long, add empty columns
        map = map.map((row) => {
          if (row.length < 13) {
            const emptyColumns = 13 - row.length;
            for (let i = 0; i < emptyColumns; i++) {
              row.push(["", "impossible"]);
            }
          }
          return row;
        });
        this.heatmap = map;
      } catch (error) {
        console.error("There was an error", error);
      }
    },
  },
  mounted() {
    this.sendPostRequest();
  },
  computed: {
    disabledPositions() {
      return [];
    },
    disabledShowdownCards() {
      return [];
    },
    disabledSimpleSuitedness() {
      return [];
    },
    gridStyle() {
      const size = `min(90vw, 600px)`;
      return {
        display: "grid",
        gridTemplateColumns: `repeat(13, 1fr)`,
        width: size,
        height: size,
      };
    },
    disabledDetailedSuitedness() {
      return this.detailedSuitednessArray
        .map((suit) => suit.value)
        .filter(
          (suit) => !this.simpleDetailArray[this.simpleSuit].includes(suit),
        );
    },
  },
};
</script>

<style scoped>
.grid-row {
  display: contents;
}
</style>
