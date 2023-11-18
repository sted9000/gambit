<template>
  <header class="flex justify-between items-center py-4 px-8 bg-green-400">
    <h1 class="text-4xl font-bold text-gray-800">{{ name }}</h1>
    <nav>
      <div class="flex justify-center items-center">
        <a
          href="https://github.com/sted9000/gambit#description"
          rel="noopener noreferrer"
          class="text-lg font-bold text-gray-800 mx-4"
          >About</a
        >
        <a href="https://github.com/sted9000/gambit" rel="noopener noreferrer">
          <img
            src="../assets/github-mark.png"
            alt="Github Logo"
            class="h-8 mx-4"
          />
        </a>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Header",
  props: {
    name: String,
  },
};
</script>
