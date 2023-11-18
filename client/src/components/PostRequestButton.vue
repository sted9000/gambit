<template>
  <div class="self-center text-center mx-4">
    <button
      id="button"
      type="submit"
      @click="$emit('clicked')"
      class="bg-indigo-600 shadow-xl hover:bg-indigo-500 text-white rounded-full px-8 py-2"
    >
      {{ text }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'PostRequestButton',
  props: {
    text: String
  }
}
</script>
