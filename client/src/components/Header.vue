<template>
  <header class="max-w-6xl mx-auto bg-gray-50 px-4 sm:px-6 lg:px-8 w-full">
    <div class="flex justify-between items-center py-4">
      <div class="flex-shrink-0">
        <div class="relative">
          <div class="text-2xl font-bold animated-text">
            {{ APP_NAME }}
          </div>
          <span
            class="absolute right-0 -bottom-3 text-[0.6rem] text-gray-500 hidden sm:inline"
            >by {{ SPONSOR }}</span
          >
        </div>
      </div>
      <nav>
        <a
          :href="GITHUB_LINK"
          target="_blank"
          rel="noopener noreferrer"
          class="text-gray-600 hover:text-gray-900 font-medium"
        >
          About
        </a>
      </nav>
    </div>
  </header>
</template>

<script setup>
import "@/assets/css/animatedText.css";
import { APP_NAME, SPONSOR, GITHUB_LINK } from "@/constants";

const props = defineProps({
  name: String,
});
</script>
