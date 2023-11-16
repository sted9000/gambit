<!--This component is a toggle bar that will be used to toggle between "Heatmaps" and "Quizzes". It will be centered horizontally and will be placed below the header. It will be styled with tailwindcss. It will be a functional component that will take in a prop called "toggle" that will be a function that will toggle between "Heatmaps" and "Quizzes". It will also take in a prop called "active" that will be a string that will be either "Heatmaps" or "Quizzes". It will have two buttons that will be styled with tailwindcss. The first button will be styled with tailwindcss and will have the text "Heatmaps". It will be disabled if the "active" prop is "Heatmaps". It will have an onclick event that will call the "toggle" prop. The second button will be styled with tailwindcss and will have the text "Quizzes". It will be disabled if the "active" prop is "Quizzes". It will have an onclick event that will call the "toggle" prop. It will have a class of "flex justify-center items-center py-4 px-8".-->
<!--The active prop will be underlined-->
<template>
  <div class="flex justify-center items-center py-4 px-8">
    <button
      :class="[
        'text-gray-800 text-xl font-semibold hover:text-gray-600 px-4',
        { underline: active === 'Heatmaps' },
      ]"
      :disabled="active === 'Heatmaps'"
      @click="toggle"
    >
      Heatmaps
    </button>
    <button
      :class="[
        'text-gray-800 text-xl font-semibold hover:text-gray-600 px-4',
        { underline: active === 'Quizzes' },
      ]"
      :disabled="active === 'Quizzes'"
      @click="toggle"
    >
      Quizzes
    </button>
  </div>
</template>

<script>
export default {
  name: "ToggleBar",
  props: {
    toggle: Function,
    active: String,
  },
};
</script>
