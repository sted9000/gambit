<template>
  <div class="flex justify-center">
    <div class="px-8 py-2 bg-gray-100 text-gray-400 rounded-xl">
{{ text}}
    </div>
  </div>
</template>

<script>
export default {
  name: "NoDataMessage",
  props: {
    text: {
      type: String,
    },
  },
};
</script>
