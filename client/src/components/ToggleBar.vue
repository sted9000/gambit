<template>
  <div
    class="max-w-6xl mx-auto bg-gray-50 px-4 sm:px-6 lg:px-8 w-full border-t border-gray-200"
  >
    <div class="flex justify-center items-center py-3">
      <button
        :class="[
          'text-gray-600 hover:text-gray-900 font-medium transition duration-300 ease-in-out px-4 py-2',
          {
            'text-gray-900 border-b-2 border-gray-900': active === 'Heatmaps',
          },
        ]"
        :disabled="active === 'Heatmaps'"
        @click="toggle('Heatmaps')"
      >
        Heatmaps
      </button>
      <button
        :class="[
          'text-gray-600 hover:text-gray-900 font-medium transition duration-300 ease-in-out px-4 py-2',
          {
            'text-gray-900 border-b-2 border-gray-900': active === 'Quizzes',
          },
        ]"
        :disabled="active === 'Quizzes'"
        @click="toggle('Quizzes')"
      >
        Quizzes
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue";
const emit = defineEmits(["toggle"]);

const props = defineProps({
  active: String,
});

const toggle = (newView) => {
  emit("toggle", newView);
};
</script>
