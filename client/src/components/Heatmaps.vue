<template>
  <div>
    <div class="flex justify-center my-4">
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

      <PostRequestButton @clicked="sendPostRequest" text="Load" />
    </div>


    <div class="flex justify-center my-8">

      <!--    Heatmap and Legend-->
      <div v-if="heatmap" :style="gridContainerStyle">
        <div v-for="(row, rowIndex) in heatmap" :key="rowIndex" :style="rowStyle">
          <div
              v-for="(col, colIndex) in row"
              :key="colIndex"
              :style="columnStyle"
          >
            <ComboCell
                :combo="col[0]"
                :class="col[1]"
                :column="rowIndex + colIndex + 1"
                :height="cellDim"
            />
          </div>
        </div>

        <Legend />

      </div>
      <NoDataMessage v-else text="Enter parameters and click load to view a Heatmap!" />
    </div>
  </div>

</template>

<script>
import ComboCell from "./ComboCell.vue";
import Legend from "./Legend.vue";
import HMSelect from "./HMSelect.vue";
import PostRequestButton from "./PostRequestButton.vue";
import axios from "axios";
import NoDataMessage from "./NoDataMessage.vue";
import dataMixin from "../mixins/dataMixin";

export default {
  name: "Heatmaps",
  mixins: [dataMixin],
  components: {NoDataMessage, HMSelect, ComboCell, Legend, PostRequestButton },
  data() {
    return {
      position: "1",
      showdownCards: "AK",
      simpleSuit: "ss",
      detailedSuit: "wxyx",
      heatmap: null,
      numRows: 13,
      numCols: 13,
      windowWidth: window.innerWidth / 2.5,
    };
  },
  methods: {
    handlePositionChange(value) {
      this.position = value;
    },
    handleComboChange(value) {
      this.showdownCards = value;
    },
    handleSuitChange(value) {
      this.simpleSuit = value;
      // a few simple suitedness options have only one detailed suitedness option
      // so just go ahead and set the detailed suitedness to that option for the user
      if (value === "rb" || value === "4s") {
        this.detailedSuit = this.simpleDetailArray[value][0];
      } else {
        if (!this.simpleDetailArray[value].includes(this.detailedSuit)) {
          this.detailedSuit = this.simpleDetailArray[value][0];
        }
      }
    },
    handleDetailChange(value) {
      this.detailedSuit = value;
      // a few simple suitedness options have only one detailed suitedness option
      // so just go ahead and set the single suit to that option for the user
      if (value === "wxyz") {
        this.simpleSuit = "rb";
      } else if (value === "wwww") {
        this.simpleSuit = "4s";
      }
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
          { headers: { "Content-Type": "application/json" } }
        );
        // Note the use of JSON.parse here. This is because the response.data.map is a stringified JSON object.
        this.heatmap = JSON.parse(response.data.map);
      } catch (error) {
        console.error("There was an error", error);
      }
    },
    handleResize() {
      this.windowWidth = window.innerWidth / 2;
    },
  },
  async mounted() {
    window.addEventListener("resize", this.handleResize);
    await this.sendPostRequest()
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.handleResize);
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
    disabledDetailedSuitedness() {
      let detailSuits = this.detailedSuitednessArray.map((suit) => suit.value);
      return detailSuits.filter(
        (suit) => !this.simpleDetailArray[this.simpleSuit].includes(suit)
      );
    },
    cellDim() {
      return `${this.windowWidth / this.numRows}px`;
    },
    gridContainerStyle() {
      return {
        width: `${this.windowWidth}px`,
        height: `${this.windowWidth}px`,
      };
    },
    rowStyle() {
      return {
        height: this.cellDim,
        display: "grid",
        gridTemplateColumns: `repeat(${this.numCols}, 1fr)`,
      };
    },
    columnStyle() {
      return {
        width: this.cellDim,
      };
    },
  },
};
</script>
