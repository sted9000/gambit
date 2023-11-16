<template>
  <div
    :class="[
      'grid grid-cols-1 border-2 rounded-lg border-gray-600 p-2',
      grade !== null ? gradeBackgroundColor : '',
    ]"
  >
    <!--    Cards-->
    <div class="flex justify-center p-2">
      <div
        v-for="(card, index) in cardArray"
        :key="index"
        :class="['text-xl', colorArray[index]]"
      >
        {{ cardAndSuit(index) }}
      </div>
    </div>
    <!--  Open or Fold-->
    <div class="grid grid-cols-2 m-2">
      <div class="flex justify-center items-center">
        <input
          type="radio"
          :id="trueName"
          value="true"
          :name="trueName"
          class="sr-only"
          v-model="selectedOption"
          :disabled="grade !== null"
          @change="emitValue(selectedOption)"
        />
        <label
          :class="{
            'bg-blue-600 text-white': selectedOption === 'true',
          }"
          :for="trueName"
          class="cursor-pointer px-4 py-2 border rounded"
        >
          Open
        </label>
      </div>
      <div class="flex justify-center items-center">
        <input
          type="radio"
          :id="falseName"
          value="false"
          :name="falseName"
          class="sr-only"
          v-model="selectedOption"
          :disabled="grade !== null"
          @change="emitValue(selectedOption)"
        />
        <label
          :class="{
            'bg-gray-600 text-white': selectedOption === 'false',
          }"
          :for="falseName"
          class="cursor-pointer px-4 py-2 border rounded"
        >
          Fold
        </label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "QuizQuestion",
  emits: ["selectionChanged"],
  props: {
    question: Object,
    name: String,
    grade: Boolean,
  },
  data() {
    return {
      selectedOption: "",
      cardArray: [],
      suitArray: [],
      colorArray: [],
      cardDim: {
        height: 70,
        width: 50,
      },
      trueName: this.name + "_" + "true",
      falseName: this.name + "_" + "false",
    };
  },
  methods: {
    composeCardArray() {
      let sd = this.question.showdown_cards;
      let sc = this.question.sidecards;
      let hand_array = [sd[0], sd[1], sc[0], sc[1]];
      let ranks = [
        "A",
        "K",
        "Q",
        "J",
        "T",
        "9",
        "8",
        "7",
        "6",
        "5",
        "4",
        "3",
        "2",
      ];
      return hand_array.sort((a, b) => {
        if (ranks.indexOf(a) >= ranks.indexOf(b)) {
          return 1;
        } else {
          return -1;
        }
      });
    },
    composeSuitArray() {
      // return array of suits
      // the suits in the string this.question.detailed_suit
      let suit_array = this.question.detailed_suit.split("");
      let replace_object = {
        w: "♠",
        x: "♣",
        y: "♥",
        z: "♦",
      };
      return suit_array.map((suit) => {
        return replace_object[suit];
      });
    },
    composeColorArray() {
      let color_array = this.question.detailed_suit.split("");
      let replace_object = {
        w: "text-green-600",
        x: "text-blue-600",
        y: "text-red-600",
        z: "text-orange-600",
      };
      return color_array.map((suit) => {
        return replace_object[suit];
      });
    },
    cardAndSuit(index) {
      let card = this.cardArray[index];
      let suit = this.suitArray[index];
      return card + suit;
    },
    emitValue(value) {
      this.$emit("selectionChanged", value);
    },
  },
  computed: {
    gradeBackgroundColor() {
      if (this.grade) {
        return "bg-green-200";
      } else {
        return "bg-red-200";
      }
    },
  },
  mounted() {
    this.cardArray = this.composeCardArray();
    this.suitArray = this.composeSuitArray();
    this.colorArray = this.composeColorArray();
    console.log("here");
  },
};
</script>
