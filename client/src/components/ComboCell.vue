<template>
  <div
    :class="[computedColor, 'flex justify-center items-center', textColorClass]"
    :style="cellStyle"
    v-tooltip="this.class !== 'impossible' ? ev : null"
  >
    {{ combo }}
  </div>
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
    ev() {
      switch (this.class) {
        case "rfi-5":
          return "Jackpot!";
        case "rfi-4":
          return "Really High EV";
        case "rfi-3":
          return "High EV";
        case "rfi-2":
          return "Moderate EV";
        case "rfi-1":
          return "Low EV";
        case "rfi-0":
          return "Close to break even";
        case "impossible":
          return "Impossible";
        default:
          return "Fold";
      }
    },
    computedColor() {
      switch (this.class) {
        case "impossible":
          return "bg-gray-100";
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
        default:
          return "bg-white";
      }
    },
    textColorClass() {
      return "text-gray-800";
    },
    cellStyle() {
      return {
        height: this.height,
        width: this.height, // Make it square
        fontSize: `calc(${this.height} * 0.4)`, // Adjust font size relative to cell size
        fontWeight: this.class !== "impossible" ? "bold" : "normal",
        fontSize: "1rem",
        fontColor: this.class === "impossible" ? "gray" : "black",
        opacity: this.class === "impossible" ? 0.5 : 1,
        transition: "all 0.3s ease",
      };
    },
  },
};
</script>

<style scoped>
div {
  border: 1px solid white;
  cursor: pointer;
}

div:hover {
  transform: scale(1.1);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  z-index: 10;
}
</style>
