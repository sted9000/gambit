<!--Note: These are presentational components, so they don't have any data or methods. They just receive props and emit events.-->
<template>
  <div class="relative inline-block text-left mx-4">
    <label for="options" class="block text-sm font-medium text-gray-700">{{
      name
    }}</label>
    <select
      id="options"
      :value="value"
      @change.stop="onChange($event)"
      class="block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
    >
      <option disabled value="">Please select one</option>
      <option
        v-for="(option, index) in options"
        :key="index"
        :value="option.value"
        :disabled="isDisabled(option.label)"
      >
        {{ option.label }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  name: "HMSelect",
  props: {
    name: String,
    options: Array,
    disabledOptions: Array,
    value: String,
  },
  methods: {
    onChange(event) {
      this.$emit("change", event.target.value);
    },
    isDisabled(option) {
      return this.disabledOptions.includes(option);
    },
  },
};
</script>
