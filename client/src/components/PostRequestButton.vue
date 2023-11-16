<template>
  <div class="self-center text-center">
    <button
      id="button"
      type="submit"
      @click="$emit('clicked')"
      class="bg-indigo-600 shadow-xl hover:bg-indigo-500 text-white rounded-full p-2 w-36"
    >
      Generate Quiz
    </button>
  </div>
</template>
