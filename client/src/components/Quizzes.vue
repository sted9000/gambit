<template>
  <!--  Select the parameters of the quiz-->
  <div class="flex justify-center my-4">
    <HMSelect
      name="Position"
      :options="positions"
      :disabledOptions="disabledPositions"
      :value="position"
      @change="handlePositionChange"
    />
    <HMSelect
      name="Simple Suitedness"
      :options="simpleSuited"
      :disabledOptions="disabledSimpleSuited"
      :value="simpleSuit"
      @change="handleSimpleSuitChange"
    />
    <PostRequestButton @clicked="sendPostRequest" text="Generate" />
  </div>

  <!--  List the quiz questions-->
  <div class="flex justify-center my-8">
    <div
      v-if="quiz.length"
      class="container mx-auto grid grid-cols-2 lg:grid-cols-4 gap-4"
    >
      <QuizQuestion
        v-for="(question, index) in quiz"
        :key="index + '_' + quizId"
        :question="question"
        :name="index.toString()"
        @selectionChanged="
          (eventValue) => handleSelectionChanged(index, eventValue)
        "
        :grade="index >= 0 && index < grade.length ? grade[index] : null"
      />
    </div>
  </div>

  <!--    Grade the quiz-->
  <div v-if="quiz.length" class="flex justify-center mt-8">
    <button
      :class="[
        'shadow-xl text-white font-bold rounded-full p-4 w-36',
        allAnswersSelected
          ? 'bg-indigo-600 hover:bg-indigo-500'
          : 'bg-gray-300',
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

  <NoDataMessage
    v-if="!quiz.length"
    text="Enter parameters and click load to generate a Quiz!"
  />
</template>

<script>
import HMSelect from "./HMSelect.vue";
import QuizQuestion from "./QuizQuestion.vue";
import axios from "axios";
import PostRequestButton from "./PostRequestButton.vue";
import NoDataMessage from "./NoDataMessage.vue";

export default {
  name: "Quizzes",
  components: { PostRequestButton, QuizQuestion, HMSelect, NoDataMessage },
  data() {
    return {
      // Positions and simple suitedness arrays
      positions: [
        { label: "EP", value: 0 },
        { label: "MP", value: 1 },
        { label: "CO", value: 2 },
        { label: "BTN", value: 3 },
        { label: "SB", value: 4 },
      ],
      simpleSuited: [
        { label: "Double Suited", value: "ds" },
        { label: "Single Suited", value: "ss" },
        { label: "Three to suit", value: "3s" },
        { label: "Four to suit", value: "4s" },
        { label: "Rainbow", value: "rb" },
      ],

      // User selected position and simple suitedness
      position: "1",
      simpleSuit: "ss",

      // Object to store the answers to the quiz questions
      answers: Object.assign(
        {},
        ...Array.from({ length: 20 }, (v, i) => ({ [i]: null }))
      ),

      // Array to store the grade of the quiz
      grade: [],

      // Quiz
      quiz: [],
      quizId: "",
    };
  },
  methods: {
    handlePositionChange(value) {
      this.position = value;
    },
    handleSimpleSuitChange(value) {
      this.simpleSuit = value;
    },
    handleSelectionChanged(index, value) {
      this.answers[index.toString()] = value;
      console.log(index, value);
    },
    async sendPostRequest() {
      // clean the answers
      this.answers = Object.assign(
        {},
        ...Array.from({ length: 20 }, (v, i) => ({ [i]: null }))
      );
      // clean the grade
      this.grade = [];

      try {
        const response = await axios.post(
          `${import.meta.env.VITE_BASE_URL}/quiz`,
          {
            stack_size: "100",
            rake_structure: "2.5_1.5bb",
            players: "6",
            position: this.position,
            simple_suit: this.simpleSuit,
          },
          { headers: { "Content-Type": "application/json" } }
        );
        this.quiz = response.data.quiz;
        this.quizId = response.data.id;
        console.log(this.quiz, this.quizId);
      } catch (error) {
        console.error("There was an error", error);
      }
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
    disabledPositions() {
      return [];
    },
    disabledSimpleSuited() {
      return [];
    },
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
};
</script>
