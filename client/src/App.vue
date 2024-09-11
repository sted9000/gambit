<template>
  <div class="flex flex-col min-h-screen bg-gray-50 mb-4">
    <div class="flex-grow bg-gray-50">
      <Header name="Gambit PLO" />
      <ToggleBar @toggle="toggleView" :active="activeView" />
      <div v-show="activeView === 'Heatmaps'">
        <Heatmaps />
      </div>
      <div v-show="activeView === 'Quizzes'">
        <Quizzes />
      </div>
    </div>
  </div>
</template>

<script setup>
import Header from "./components/Header.vue";
import ToggleBar from "./components/ToggleBar.vue";
import Heatmaps from "./components/Heatmaps.vue";
import Quizzes from "./components/Quizzes.vue";
import { ref } from "vue";

const activeView = ref("Heatmaps");
const toggleView = (newView) => {
  activeView.value = newView;
};
</script>

<style>
body {
  background-color: rgb(249 250 251);
}
</style>
