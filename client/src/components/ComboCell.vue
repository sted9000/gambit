<template>
  <div :class="[computedColor, computedColumn, 'flex justify-center items-center']" :style="computedHeight">{{combo}}</div>
</template>

<script>
export default {
  name: "ComboCell",
  props: {
    combo: String,
    class: String,
    column: Number,
    height: String,
  },
  computed: {
    computedColor() {
      switch (this.class) {
        case "impossible":
          return "text-gray-400";
        case "rfi-5":
          return "bg-green-600";
        case "rfi-4":
          return "bg-green-500";
        case "rfi-3":
          return "bg-green-400";
        case "rfi-2":
          return "bg-green-300";
        case "rfi-1":
          return "bg-green-200";
        case "rfi-0":
          return "bg-green-100";
      }
    },
    computedColumn() {
      return `col-span-${this.column}`;
    },
    computedHeight() {
      return {
        height: this.height,
      };
    },




  }
};
</script>
