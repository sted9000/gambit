<template>
  <div>
    <!-- Select the parameters of the quiz -->
    <div class="flex justify-center gap-4 my-4">
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
    </div>

    <!-- Display current question or loading message -->
    <div v-if="quizStarted && !quizCompleted" class="flex justify-center my-8">
      <div v-if="currentQuestionIndex < quiz.length">
        <QuizQuestion
          :question="quiz[currentQuestionIndex]"
          :name="currentQuestionIndex.toString()"
          @selectionChanged="handleSelectionChanged"
        />
        <div class="text-center mt-4">
          Question {{ currentQuestionIndex + 1 }} of {{ quiz.length }}
        </div>
      </div>
      <div v-else class="text-center">
        <p>Loading next question...</p>
      </div>
    </div>

    <!-- Display the grade -->
    <div v-if="quizCompleted" class="mt-8">
      <div class="flex justify-center">
        <p>Quiz Completed!</p>
      </div>
      <div class="flex justify-center">
        <p>Grade: {{ grade.filter((x) => x).length }} / {{ quiz.length }}</p>
      </div>
      <div class="flex justify-center">
        <p>Percentage: {{ gradePercentage }}%</p>
      </div>
    </div>

    <!-- Start/Restart Quiz Button -->
    <div v-if="!quizStarted || quizCompleted" class="flex justify-center mt-4">
      <button
        @click="startQuiz"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        {{ quizCompleted ? "Start New Quiz" : "Start Quiz" }}
      </button>
    </div>

    <!-- Incorrect Answers -->
    <div v-if="incorrectAnswers.length > 0" class="mt-8 max-w-2xl mx-auto">
      <h2 class="text-2xl font-bold mb-6 text-center">Incorrect Answers</h2>
      <div
        v-for="(question, index) in incorrectAnswers"
        :key="index"
        class="mb-8 p-6 border rounded-lg shadow-md"
      >
        <div class="flex justify-between items-center mb-4">
          <span class="font-semibold text-lg"
            >Question {{ question.questionNumber }}</span
          >
          <span class="text-sm text-gray-600">{{
            convertToSymbols(question.detailed_suit)
          }}</span>
        </div>
        <div class="flex justify-center mb-4">
          <Card
            v-for="(card, cardIndex) in (
              question.showdown_cards + question.sidecards
            ).split('')"
            :key="cardIndex"
            :rank="card"
            :suit="question.detailed_suit[cardIndex]"
          />
        </div>
        <div class="flex justify-between items-center">
          <div>
            <span class="font-medium">Your answer: </span>
            <span
              :class="{
                'text-red-600': question.userAnswer !== question.isOpen,
              }"
            >
              {{ question.userAnswer === "true" ? "Open" : "Fold" }}
            </span>
          </div>
          <div>
            <span class="font-medium">Correct answer: </span>
            <span class="text-green-600">
              {{ question.isOpen === "true" ? "Open" : "Fold" }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HMSelect from "./HMSelect.vue";
import QuizQuestion from "./QuizQuestion.vue";
import axios from "axios";
import PostRequestButton from "./PostRequestButton.vue";
import Card from "./Card.vue";

export default {
  name: "Quizzes",
  components: { PostRequestButton, QuizQuestion, HMSelect, Card },
  data() {
    return {
      incorrectAnswers: [],
      showIncorrectAnswers: false,
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
      position: "1",
      simpleSuit: "ss",
      answers: {},
      grade: [],
      quiz: [],
      quizId: "",
      quizStarted: false,
      quizCompleted: false,
      currentQuestionIndex: 0,
    };
  },
  methods: {
    convertToSymbols(detailedSuit) {
      console.log(detailedSuit);
      const suitMap = { w: "♠", x: "♣", y: "♥", z: "♦" };
      return detailedSuit
        .split("")
        .map((suit) => suitMap[suit] || suit)
        .join("");
    },
    compileIncorrectAnswers() {
      console.log(this.answers);
      return this.quiz
        .map((question, index) => ({
          ...question,
          userAnswer: this.answers[index.toString()],
          questionNumber: index + 1,
        }))
        .filter((question, index) => !this.grade[index]);
    },
    finishQuiz() {
      this.gradeQuiz();
      this.incorrectAnswers = this.compileIncorrectAnswers();
      console.log(this.incorrectAnswers);
      this.quizCompleted = true;
    },
    handlePositionChange(value) {
      // clear the answers, grade, and quiz
      this.answers = {};
      this.grade = [];
      this.currentQuestionIndex = 0;
      this.quizStarted = false;
      this.quizCompleted = false;
      this.incorrectAnswers = [];
      this.showIncorrectAnswers = false;

      this.position = value;
    },
    handleSimpleSuitChange(value) {
      // clear the answers, grade, and quiz
      this.answers = {};
      this.grade = [];
      this.currentQuestionIndex = 0;
      this.quizStarted = false;
      this.quizCompleted = false;
      this.incorrectAnswers = [];
      this.showIncorrectAnswers = false;

      this.simpleSuit = value;
    },
    handleSelectionChanged(value) {
      this.answers[this.currentQuestionIndex.toString()] = value;
      this.moveToNextQuestion();
    },
    async startQuiz() {
      this.answers = {};
      this.grade = [];
      this.currentQuestionIndex = 0;
      this.quizStarted = false;
      this.quizCompleted = false;
      this.incorrectAnswers = [];
      this.showIncorrectAnswers = false;

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
          { headers: { "Content-Type": "application/json" } },
        );
        this.quiz = response.data.quiz;
        this.quizId = response.data.id;
        this.quizStarted = true;
      } catch (error) {
        console.error("There was an error", error);
      }
    },
    moveToNextQuestion() {
      if (this.currentQuestionIndex < this.quiz.length - 1) {
        this.currentQuestionIndex++;
      } else {
        this.finishQuiz();
      }
    },
    gradeQuiz() {
      console.log("answers", this.answers);
      console.log("quiz", this.quiz);
      this.grade = this.quiz.map((question, index) => {
        const userAnswer = this.answers[index.toString()];
        const correctAnswer = question.isOpen;
        return userAnswer === correctAnswer;
      });
      console.log("grade", this.grade);
    },
  },
  computed: {
    disabledPositions() {
      return [];
    },
    disabledSimpleSuited() {
      return [];
    },
    gradePercentage() {
      return Math.round(
        (this.grade.filter((x) => x).length / this.quiz.length) * 100,
      );
    },
  },
};
</script>
