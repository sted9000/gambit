<template>
  <Header name="Gambit PLO" />
  <ToggleBar :toggle="toggle" :active="active" />
  <Heatmaps v-show="active === 'Heatmaps'" />
  <Quizzes v-show="active === 'Quizzes'" />
</template>

<script>
import Header from "./components/Header.vue";
import ToggleBar from "./components/ToggleBar.vue";
import Heatmaps from "./components/Heatmaps.vue";
import Quizzes from "./components/Quizzes.vue";
import { ref } from "vue";

export default {
  name: "App",
  components: {
    Header,
    ToggleBar,
    Heatmaps,
    Quizzes,
  },
  setup() {
    const active = ref("Heatmaps");

    const toggle = () => {
      active.value = active.value === "Heatmaps" ? "Quizzes" : "Heatmaps";
    };

    return {
      active,
      toggle,
    };
  },
};
</script>
