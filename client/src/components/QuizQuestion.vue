<template>
  <div class="p-4">
    <div class="flex justify-center p-2 mb-4">
      <Card
        v-for="(card, index) in cards"
        :key="index"
        :rank="card.rank"
        :suit="card.suit"
      />
    </div>
    <div class="flex justify-center gap-4">
      <button
        @click="selectOption('open')"
        :class="[
          'px-6 py-3 rounded text-white bg-blue-500 hover:bg-blue-600 font-bold shadow-md',
          selectedOption === 'open' ? 'ring-2 ring-blue-300' : '',
        ]"
      >
        Open
      </button>
      <button
        @click="selectOption('fold')"
        :class="[
          'px-6 py-3 rounded text-white bg-red-500 hover:bg-red-600 font-bold shadow-md',
          selectedOption === 'fold' ? 'ring-2 ring-red-300' : '',
        ]"
      >
        Fold
      </button>
    </div>
  </div>
</template>

<script>
import Card from "./Card.vue";

export default {
  name: "QuizQuestion",
  components: { Card },
  emits: ["selectionChanged"],
  props: {
    question: Object,
    name: String,
    grade: Boolean,
  },
  data() {
    return {
      selectedOption: "",
    };
  },
  computed: {
    cards() {
      const ranks = [
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
      const handArray = [
        ...this.question.showdown_cards,
        ...this.question.sidecards,
      ];
      const suitArray = this.question.detailed_suit.split("");

      return handArray
        .map((rank, index) => ({ rank, suit: suitArray[index] }))
        .sort((a, b) => ranks.indexOf(a.rank) - ranks.indexOf(b.rank));
    },
  },
  methods: {
    selectOption(selectedOption) {
      const guess = selectedOption === "open" ? "true" : "false";
      this.$emit("selectionChanged", guess);
    },
  },
};
</script>
