<template>
  <!--  Select the parameters of the quiz-->
  <div class="flex justify-center my-4">
    <HMSelect
      name="Position"
      :options="positions"
      :disabledOptions="disabledPositions"
      @optionChanged="positionChanged"
      :initialValue="position"
    />
    <HMSelect
      name="Simple Suitedness"
      :options="simpleSuited"
      :disabledOptions="disabledSimpleSuited"
      @optionChanged="simpleSuitChanged"
      :initialValue="simpleSuit"
    />
  </div>

  <!--  List the quiz questions-->
  <div
    v-if="quizSelected"
    class="container mx-auto grid grid-cols-2 lg:grid-cols-4 gap-4"
  >
    <QuizQuestion
      v-for="(question, index) in quiz"
      :key="index"
      :question="question"
      :name="index.toString()"
      @selectionChanged="
        (eventValue) => handleSelectionChanged(index, eventValue)
      "
      :grade="index >= 0 && index < grade.length ? grade[index] : null"
    />
  </div>

  <!--  Grade the quiz-->
  <div class="flex justify-center mt-8">
    <button
      :class="[
        'text-xl',
        'font-medium',
        'rounded-lg',
        'px-8',
        'py-4',
        allAnswersSelected ? 'bg-green-400' : 'bg-gray-300',
      ]"
      :disabled="!allAnswersSelected"
      @click="gradeQuiz"
    >
      Grade Quiz
    </button>
  </div>

  <!--  Display the grade-->
  <div v-if="grade.length > 0">
    <div class="flex justify-center mt-4">
      <p>Grade: {{ grade.filter((x) => x).length }} / 20</p>
    </div>
    <div class="flex justify-center">
      <p>Percentage: {{ gradePercentage }}%</p>
    </div>
  </div>
</template>

<script>
import HMSelect from "./HMSelect.vue";
import QuizQuestion from "./QuizQuestion.vue";

export default {
  name: "Quizzes",
  components: { QuizQuestion, HMSelect },
  data() {
    return {
      positions: [
        { label: "EP", value: 0 },
        { label: "MP", value: 1 },
        { label: "CO", value: 2 },
        { label: "BTN", value: 3 },
        { label: "SB", value: 4 },
      ],
      disabledPositions: ["EP", "CO", "BTN", "SB"],
      position: "1",
      simpleSuited: [
        { label: "Double Suited", value: "ds" },
        { label: "Single Suited", value: "ss" },
        { label: "Three to suit", value: "3s" },
        { label: "Four to suit", value: "4s" },
        { label: "Rainbow", value: "rb" },
      ],
      disabledSimpleSuited: [
        "Double Suited",
        "Three to suit",
        "Four to suit",
        "Rainbow",
      ],
      simpleSuit: "ss",

      // Object to store the answers to the quiz questions
      answers: Object.assign(
        {},
        ...Array.from({ length: 20 }, (v, i) => ({ [i]: null }))
      ),

      // Array to store the grade of the quiz
      grade: [],

      // Quiz
      quiz: [
        {
          sidecards: "65",
          isOpen: "true",
          showdown_cards: "97",
          detailed_suit: "wxyx",
        },
        {
          sidecards: "76",
          isOpen: "true",
          showdown_cards: "T8",
          detailed_suit: "wxwy",
        },
        {
          sidecards: "97",
          isOpen: "true",
          showdown_cards: "KT",
          detailed_suit: "wxxy",
        },
        {
          sidecards: "32",
          isOpen: "false",
          showdown_cards: "K4",
          detailed_suit: "wxyx",
        },
        {
          sidecards: "AQ",
          isOpen: "true",
          showdown_cards: "88",
          detailed_suit: "wxyx",
        },
        {
          sidecards: "53",
          isOpen: "false",
          showdown_cards: "K6",
          detailed_suit: "wwxy",
        },
        {
          sidecards: "96",
          isOpen: "false",
          showdown_cards: "KJ",
          detailed_suit: "wwxy",
        },
        {
          sidecards: "43",
          isOpen: "false",
          showdown_cards: "75",
          detailed_suit: "wxwy",
        },
        {
          sidecards: "AQ",
          isOpen: "false",
          showdown_cards: "22",
          detailed_suit: "wxxy",
        },
        {
          sidecards: "A9",
          isOpen: "false",
          showdown_cards: "33",
          detailed_suit: "wxyw",
        },
        {
          sidecards: "A5",
          isOpen: "true",
          showdown_cards: "22",
          detailed_suit: "wxyw",
        },
        {
          sidecards: "AQ",
          isOpen: "false",
          showdown_cards: "55",
          detailed_suit: "wxxy",
        },
        {
          sidecards: "32",
          isOpen: "false",
          showdown_cards: "A5",
          detailed_suit: "wxwy",
        },
        {
          sidecards: "74",
          isOpen: "true",
          showdown_cards: "A8",
          detailed_suit: "wxyw",
        },
        {
          sidecards: "AQ",
          isOpen: "false",
          showdown_cards: "44",
          detailed_suit: "wxyx",
        },
        {
          sidecards: "32",
          isOpen: "false",
          showdown_cards: "64",
          detailed_suit: "wxyw",
        },
        {
          sidecards: "32",
          isOpen: "false",
          showdown_cards: "64",
          detailed_suit: "wxyx",
        },
        {
          sidecards: "T7",
          isOpen: "true",
          showdown_cards: "QJ",
          detailed_suit: "wxxy",
        },
        {
          sidecards: "32",
          isOpen: "false",
          showdown_cards: "A4",
          detailed_suit: "wxxy",
        },
        {
          sidecards: "96",
          isOpen: "false",
          showdown_cards: "QT",
          detailed_suit: "wxyx",
        },
      ],
    };
  },
  methods: {
    positionChanged(position) {
      this.position = position;
    },
    simpleSuitChanged(simpleSuit) {
      this.simpleSuit = simpleSuit;
    },
    handleSelectionChanged(index, value) {
      this.answers[index.toString()] = value;
      console.log(index, value);
    },
    gradeQuiz() {
      let localGrade = [];
      for (let i = 0; i < 20; i++) {
        let correctAnswer = this.quiz[i].isOpen;
        let userAnswer = this.answers[i.toString()];
        localGrade.push(correctAnswer === userAnswer);
      }
      this.grade = localGrade;
    },
  },
  computed: {
    quizSelected() {
      return this.position !== "" && this.simpleSuit !== "";
    },
    allAnswersSelected() {
      return !Object.values(this.answers).includes(null);
    },
    gradePercentage() {
      return Math.round((this.grade.filter((x) => x).length / 20) * 100);
    },
  },
  mounted() {
    console.log(this.quiz);
    console.log(this.quiz.length);
  },
};
</script>
