<template>
  <Header name="Gambit PLO" />
  <ToggleBar :toggle="toggle" :active="active" />
  <Heatmaps v-if="active === 'Heatmaps'" />
  <Quizzes v-else />
</template>

<script>
import Header from "./components/Header.vue";
import ToggleBar from "./components/ToggleBar.vue";
import Heatmaps from "./components/Heatmaps.vue";
import Quizzes from "./components/Quizzes.vue";
import { ref } from "vue";
const active = ref("Heatmaps");

const toggle = () => {
  if (active.value === "Heatmaps") {
    active.value = "Quizzes";
  } else {
    active.value = "Heatmaps";
  }
};

export default {
  name: "App",
  components: {
    Header,
    ToggleBar,
    Heatmaps,
    Quizzes,
  },
  setup() {
    return {
      active,
      toggle,
    };
  },
  methods: {
    async sendPostRequest() {
      try {
        const response = await axios.post(
          "http://localhost:8080/test",
          { message: "Hello World" },
          { headers: { "Content-Type": "application/json" } }
        );
        console.log(response.data);
      } catch (error) {
        console.error("There was an error", error);
      }
    },
  },
};
</script>
