<template>
  <div class="card" :class="[suitColor, { 'card-disabled': disabled }]">
    <div class="card-corner top-left">
      <div class="card-rank">{{ rank }}</div>
      <div class="card-suit">{{ suitSymbol }}</div>
    </div>
    <div class="card-suit center">{{ suitSymbol }}</div>
    <div class="card-corner bottom-right">
      <div class="card-rank">{{ rank }}</div>
      <div class="card-suit">{{ suitSymbol }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    rank: String,
    suit: String,
    disabled: Boolean,
  },
  computed: {
    suitSymbol() {
      const symbols = { w: "♠", x: "♣", y: "♥", z: "♦" };
      return symbols[this.suit.toLowerCase()] || this.suit;
    },
    suitColor() {
      return ["y", "z"].includes(this.suit.toLowerCase())
        ? "text-red-600"
        : "text-black";
    },
  },
};
</script>

<style scoped>
.card {
  width: 60px;
  height: 84px;
  background-color: white;
  border-radius: 4px;
  border: 1px solid #ccc;
  position: relative;
  display: inline-block;
  margin: 0 4px;
  font-family: Arial, sans-serif;
}

.card-disabled {
  opacity: 0.5;
}

.card-corner {
  position: absolute;
  font-size: 16px;
  line-height: 1;
}

.top-left {
  top: 4px;
  left: 4px;
}

.bottom-right {
  bottom: 4px;
  right: 4px;
  transform: rotate(180deg);
}

.card-rank {
  font-weight: bold;
}

.card-suit {
  font-size: 16px;
}

.center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 24px;
}
</style>
