<template>
  <div class="flex justify-center my-4">
    <HMSelect
      name="Position"
      :options="positions"
      :disabledOptions="disabledPositions"
      @optionChanged="positionChanged"
      :initialValue="position"
    />
    <HMSelect
      name="Showdown Cards"
      :options="sdCombos"
      :disabledOptions="disabledCombos"
      @optionChanged="comboChanged"
      :initialValue="combo"
    />
    <HMSelect
      name="Simple Suitedness"
      :options="simpleSuitedness"
      :disabledOptions="disabledSimpleSuitedness"
      @optionChanged="suitChanged"
      :initialValue="suit"
    />
    <HMSelect
      name="Detailed Suitedness"
      :options="detailedSuitedness"
      :disabledOptions="disabledDetailedSuitedness"
      @optionChanged="detailedSuitChanged"
      :initialValue="detailedSuit"
    />
  </div>

  <div class="flex justify-center my-8">
    <div v-if="mapSelected" :style="gridContainerStyle">
      <div v-for="(row, rowIndex) in map" :key="rowIndex" :style="rowStyle">
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
  </div>
</template>

<script>
import ComboCell from "./ComboCell.vue";
import Legend from "./Legend.vue";
import HMSelect from "./HMSelect.vue";

export default {
  name: "Header",
  components: { HMSelect, ComboCell, Legend },
  data() {
    return {
      numRows: 13,
      numCols: 13,
      windowWidth: window.innerWidth / 2,
      positions: [
        { label: "EP", value: 0 },
        { label: "MP", value: 1 },
        { label: "CO", value: 2 },
        { label: "BTN", value: 3 },
        { label: "SB", value: 4 },
      ],
      disabledPositions: ["EP", "CO", "BTN", "SB"],
      position: "1",
      sdCombos: [
        { label: "AA", value: "AA" },
        { label: "AK", value: "AK" },
        { label: "AQ", value: "AQ" },
        { label: "AJ", value: "AJ" },
        { label: "AT", value: "AJ" },
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
      disabledCombos: [
        "AA",
        "AJ",
        "AT",
        "A9",
        "A8",
        "A7",
        "A6",
        "A5",
        "A4",
        "A3",
        "A2",
        "KK",
        "KQ",
        "KJ",
        "KT",
        "K9",
        "K8",
        "K7",
        "K6",
        "K5",
        "K4",
        "K3",
        "K2",
        "QQ",
        "QJ",
        "QT",
        "Q9",
        "Q8",
        "Q7",
        "Q6",
        "Q5",
        "Q4",
        "Q3",
        "Q2",
        "JJ",
        "JT",
        "J9",
        "J8",
        "J7",
        "J6",
        "J5",
        "J4",
        "J3",
        "J2",
        "TT",
        "T9",
        "T8",
        "T7",
        "T6",
        "T5",
        "T4",
        "T3",
        "T2",
        "99",
        "98",
        "97",
        "96",
        "95",
        "94",
        "93",
        "92",
        "88",
        "87",
        "86",
        "85",
        "84",
        "83",
        "82",
        "77",
        "76",
        "75",
        "74",
        "73",
        "72",
        "66",
        "65",
        "64",
        "63",
        "62",
        "55",
        "54",
        "53",
        "52",
        "44",
        "43",
        "42",
        "33",
        "32",
        "22",
      ],
      combo: "AK",
      simpleSuitedness: [
        { label: "Double Suited", value: "ds" },
        { label: "Single Suited", value: "ss" },
        { label: "Three to suit", value: "3s" },
        { label: "Four to suit", value: "4s" },
        { label: "Rainbow", value: "rb" },
      ],
      disabledSimpleSuitedness: [
        "Double Suited",
        "Three to suit",
        "Four to suit",
        "Rainbow",
      ],
      suit: "ss",
      detailedSuitedness: [
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
      disabledDetailedSuitedness: [
        "wxwx",
        "wxxw",
        "wwxy",
        "wxwy",
        "wxxy",
        "wxyw",
        "wxyy",
        "wwwx",
        "wwxw",
        "wxww",
        "wxxx",
        "wwww",
        "wxyz",
      ],
      detailed_suits: {
        ds: ["wxwx", "wxxw"], // 'wwxx'
        ss: ["wwxy", "wxwy", "wxxy", "wxyw", "wxyx", "wxyy"],
        "3s": ["wwwx", "wwxw", "wxww", "wxxx"],
        "4s": ["wwww"],
        rb: ["wxyz"],
      },
      detailedSuit: "wxyx",
      items: {
        AK: [
          [
            ["AA", "impossible"],
            ["AK", "impossible"],
            ["AQ", "impossible"],
            ["AJ", "impossible"],
            ["AT", "impossible"],
            ["A9", "impossible"],
            ["A8", "impossible"],
            ["A7", "impossible"],
            ["A6", "impossible"],
            ["A5", "impossible"],
            ["A4", "impossible"],
            ["A3", "impossible"],
            ["A2", "impossible"],
          ],
          [
            ["KK", "impossible"],
            ["KQ", "impossible"],
            ["KJ", "impossible"],
            ["KT", "impossible"],
            ["K9", "impossible"],
            ["K8", "impossible"],
            ["K7", "impossible"],
            ["K6", "impossible"],
            ["K5", "impossible"],
            ["K4", "impossible"],
            ["K3", "impossible"],
            ["K2", "impossible"],
          ],
          [
            ["QQ", "impossible"],
            ["QJ", "rfi-4"],
            ["QT", "rfi-4"],
            ["Q9", "rfi-1"],
            ["Q8", "rfi-1"],
            ["Q7", "rfi-1"],
            ["Q6", "rfi-1"],
            ["Q5", "rfi-1"],
            ["Q4", "rfi-1"],
            ["Q3", "rfi-1"],
            ["Q2", "rfi-1"],
          ],
          [
            ["JJ", "impossible"],
            ["JT", "rfi-4"],
            ["J9", "rfi-2"],
            ["J8", "rfi-1"],
            ["J7", "rfi-1"],
            ["J6", "rfi-1"],
            ["J5", "rfi-1"],
            ["J4", "rfi-1"],
            ["J3", "rfi-0"],
            ["J2", "rfi-0"],
          ],
          [
            ["TT", "impossible"],
            ["T9", "rfi-2"],
            ["T8", "rfi-2"],
            ["T7", "rfi-1"],
            ["T6", "rfi-1"],
            ["T5", "rfi-1"],
            ["T4", "rfi-0"],
            ["T3", "rfi-0"],
            ["T2", "rfi-0"],
          ],
          [
            ["99", "impossible"],
            ["98", "rfi-1"],
            ["97", "rfi-0"],
            ["96", "rfi-0"],
            ["95", "rfi-0"],
            ["94", "fold"],
            ["93", "fold"],
            ["92", "fold"],
          ],
          [
            ["88", "impossible"],
            ["87", "rfi-1"],
            ["86", "rfi-0"],
            ["85", "rfi-0"],
            ["84", "fold"],
            ["83", "fold"],
            ["82", "fold"],
          ],
          [
            ["77", "impossible"],
            ["76", "rfi-0"],
            ["75", "rfi-0"],
            ["74", "rfi-0"],
            ["73", "fold"],
            ["72", "fold"],
          ],
          [
            ["66", "impossible"],
            ["65", "rfi-0"],
            ["64", "rfi-0"],
            ["63", "fold"],
            ["62", "fold"],
          ],
          [
            ["55", "impossible"],
            ["54", "rfi-1"],
            ["53", "rfi-0"],
            ["52", "fold"],
          ],
          [
            ["44", "impossible"],
            ["43", "rfi-0"],
            ["42", "fold"],
          ],
          [
            ["33", "impossible"],
            ["32", "fold"],
          ],
          [["22", "impossible"]],
        ],
        AQ: [
          [
            ["AA", "impossible"],
            ["AK", "impossible"],
            ["AQ", "impossible"],
            ["AJ", "impossible"],
            ["AT", "impossible"],
            ["A9", "impossible"],
            ["A8", "impossible"],
            ["A7", "impossible"],
            ["A6", "impossible"],
            ["A5", "impossible"],
            ["A4", "impossible"],
            ["A3", "impossible"],
            ["A2", "impossible"],
          ],
          [
            ["KK", "impossible"],
            ["KQ", "impossible"],
            ["KJ", "impossible"],
            ["KT", "impossible"],
            ["K9", "impossible"],
            ["K8", "impossible"],
            ["K7", "impossible"],
            ["K6", "impossible"],
            ["K5", "impossible"],
            ["K4", "impossible"],
            ["K3", "impossible"],
            ["K2", "impossible"],
          ],
          [
            ["QQ", "impossible"],
            ["QJ", "impossible"],
            ["QT", "impossible"],
            ["Q9", "impossible"],
            ["Q8", "impossible"],
            ["Q7", "impossible"],
            ["Q6", "impossible"],
            ["Q5", "impossible"],
            ["Q4", "impossible"],
            ["Q3", "impossible"],
            ["Q2", "impossible"],
          ],
          [
            ["JJ", "impossible"],
            ["JT", "rfi-4"],
            ["J9", "rfi-1"],
            ["J8", "rfi-1"],
            ["J7", "rfi-0"],
            ["J6", "rfi-0"],
            ["J5", "rfi-0"],
            ["J4", "rfi-0"],
            ["J3", "rfi-0"],
            ["J2", "rfi-0"],
          ],
          [
            ["TT", "impossible"],
            ["T9", "rfi-2"],
            ["T8", "rfi-1"],
            ["T7", "rfi-0"],
            ["T6", "rfi-0"],
            ["T5", "rfi-0"],
            ["T4", "rfi-0"],
            ["T3", "rfi-0"],
            ["T2", "rfi-0"],
          ],
          [
            ["99", "impossible"],
            ["98", "rfi-0"],
            ["97", "rfi-0"],
            ["96", "fold"],
            ["95", "fold"],
            ["94", "fold"],
            ["93", "fold"],
            ["92", "fold"],
          ],
          [
            ["88", "impossible"],
            ["87", "rfi-0"],
            ["86", "rfi-0"],
            ["85", "fold"],
            ["84", "fold"],
            ["83", "fold"],
            ["82", "fold"],
          ],
          [
            ["77", "impossible"],
            ["76", "rfi-0"],
            ["75", "fold"],
            ["74", "fold"],
            ["73", "fold"],
            ["72", "fold"],
          ],
          [
            ["66", "impossible"],
            ["65", "fold"],
            ["64", "fold"],
            ["63", "fold"],
            ["62", "fold"],
          ],
          [
            ["55", "impossible"],
            ["54", "rfi-0"],
            ["53", "fold"],
            ["52", "fold"],
          ],
          [
            ["44", "impossible"],
            ["43", "fold"],
            ["42", "fold"],
          ],
          [
            ["33", "impossible"],
            ["32", "fold"],
          ],
          [["22", "impossible"]],
        ],
      },
    };
  },
  methods: {
    handleResize() {
      this.windowWidth = window.innerWidth / 2;
    },
    positionChanged(position) {
      this.position = position;
      console.log(this.position);
    },
    comboChanged(combo) {
      this.combo = combo;
      console.log(this.combo);
    },
    suitChanged(suit) {
      this.suit = suit;
      console.log(this.suit);
    },
    detailedSuitChanged(detailedSuit) {
      this.detailedSuit = detailedSuit;
      console.log(this.detailedSuit);
    },
  },
  mounted() {
    window.addEventListener("resize", this.handleResize);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.handleResize);
  },
  computed: {
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
    mapSelected() {
      return !!(this.position && this.combo && this.suit && this.detailedSuit);
    },
    map() {
      // Todo: Modify this when using real data
      return this.items[this.combo];
    },
  },
};
</script>
