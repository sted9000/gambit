<template>
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
</template>

<script>
import ComboCell from "./ComboCell.vue";
import Legend from "./Legend.vue";
import HMSelect from "./HMSelect.vue";
import PostRequestButton from "./PostRequestButton.vue";
import axios from "axios";
import NoDataMessage from "./NoDataMessage.vue";

export default {
  name: "Header",
  components: {NoDataMessage, HMSelect, ComboCell, Legend, PostRequestButton },
  data() {
    return {
      // set options for position, combo, simple suitedness, and detailed suitedness
      positionsArray: [
        { label: "EP", value: 0 },
        { label: "MP", value: 1 },
        { label: "CO", value: 2 },
        { label: "BTN", value: 3 },
        { label: "SB", value: 4 },
      ],
      showdownCardsArray: [
        { label: "AA", value: "AA" },
        { label: "AK", value: "AK" },
        { label: "AQ", value: "AQ" },
        { label: "AJ", value: "AJ" },
        { label: "AT", value: "AT" },
        { label: "A9", value: "A9" },
        { label: "A8", value: "A8" },
        { label: "A7", value: "A7" },
        { label: "A6", value: "A6" },
        { label: "A5", value: "A5" },
        { label: "A4", value: "A4" },
        { label: "A3", value: "A3" },
        { label: "A2", value: "A2" },
        { label: "KK", value: "KK" },
        { label: "KQ", value: "KQ" },
        { label: "KJ", value: "KJ" },
        { label: "KT", value: "KT" },
        { label: "K9", value: "K9" },
        { label: "K8", value: "K8" },
        { label: "K7", value: "K7" },
        { label: "K6", value: "K6" },
        { label: "K5", value: "K5" },
        { label: "K4", value: "K4" },
        { label: "K3", value: "K3" },
        { label: "K2", value: "K2" },
        { label: "QQ", value: "QQ" },
        { label: "QJ", value: "QJ" },
        { label: "QT", value: "QT" },
        { label: "Q9", value: "Q9" },
        { label: "Q8", value: "Q8" },
        { label: "Q7", value: "Q7" },
        { label: "Q6", value: "Q6" },
        { label: "Q5", value: "Q5" },
        { label: "Q4", value: "Q4" },
        { label: "Q3", value: "Q3" },
        { label: "Q2", value: "Q2" },
        { label: "JJ", value: "JJ" },
        { label: "JT", value: "JT" },
        { label: "J9", value: "J9" },
        { label: "J8", value: "J8" },
        { label: "J7", value: "J7" },
        { label: "J6", value: "J6" },
        { label: "J5", value: "J5" },
        { label: "J4", value: "J4" },
        { label: "J3", value: "J3" },
        { label: "J2", value: "J2" },
        { label: "TT", value: "TT" },
        { label: "T9", value: "T9" },
        { label: "T8", value: "T8" },
        { label: "T7", value: "T7" },
        { label: "T6", value: "T6" },
        { label: "T5", value: "T5" },
        { label: "T4", value: "T4" },
        { label: "T3", value: "T3" },
        { label: "T2", value: "T2" },
        { label: "99", value: "99" },
        { label: "98", value: "98" },
        { label: "97", value: "97" },
        { label: "96", value: "96" },
        { label: "95", value: "95" },
        { label: "94", value: "94" },
        { label: "93", value: "93" },
        { label: "92", value: "92" },
        { label: "88", value: "88" },
        { label: "87", value: "87" },
        { label: "86", value: "86" },
        { label: "85", value: "85" },
        { label: "84", value: "84" },
        { label: "83", value: "83" },
        { label: "82", value: "82" },
        { label: "77", value: "77" },
        { label: "76", value: "76" },
        { label: "75", value: "75" },
        { label: "74", value: "74" },
        { label: "73", value: "73" },
        { label: "72", value: "72" },
        { label: "66", value: "66" },
        { label: "65", value: "65" },
        { label: "64", value: "64" },
        { label: "63", value: "63" },
        { label: "62", value: "62" },
        { label: "55", value: "55" },
        { label: "54", value: "54" },
        { label: "53", value: "53" },
        { label: "52", value: "52" },
        { label: "44", value: "44" },
        { label: "43", value: "43" },
        { label: "42", value: "42" },
        { label: "33", value: "33" },
        { label: "32", value: "32" },
        { label: "22", value: "22" },
      ],
      simpleSuitednessArray: [
        { label: "Double Suited", value: "ds" },
        { label: "Single Suited", value: "ss" },
        { label: "Three to suit", value: "3s" },
        { label: "Four to suit", value: "4s" },
        { label: "Rainbow", value: "rb" },
      ],
      detailedSuitednessArray: [
        { label: "wxwx", value: "wxwx" },
        { label: "wxxw", value: "wxxw" },
        { label: "wwxy", value: "wwxy" },
        { label: "wxwy", value: "wxwy" },
        { label: "wxxy", value: "wxxy" },
        { label: "wxyw", value: "wxyw" },
        { label: "wxyx", value: "wxyx" },
        { label: "wxyy", value: "wxyy" },
        { label: "wwwx", value: "wwwx" },
        { label: "wwxw", value: "wwxw" },
        { label: "wxww", value: "wxww" },
        { label: "wxxx", value: "wxxx" },
        { label: "wwww", value: "wwww" },
        { label: "wxyz", value: "wxyz" },
      ],

      // user selected options for position, combo, simple suitedness, and detailed suitedness
      position: "1",
      showdownCards: "AK",
      simpleSuit: "ss",
      detailedSuit: "wxyx",

      // arrays of detailed suitedness for respective simple suitedness
      simpleDetailArray: {
        ds: ["wxwx", "wxxw"], // 'wwxx'
        ss: ["wwxy", "wxwy", "wxxy", "wxyw", "wxyx", "wxyy"],
        "3s": ["wwwx", "wwxw", "wxww", "wxxx"],
        "4s": ["wwww"],
        rb: ["wxyz"],
      },

      // fetched heatmap data
      heatmap: null,

      // styling variables
      numRows: 13,
      numCols: 13,
      windowWidth: window.innerWidth / 2,
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
  mounted() {
    window.addEventListener("resize", this.handleResize);
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
