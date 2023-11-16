/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/App.vue',
    './src/components/*.vue',
  ],
  theme: {
    extend: {
      gridTemplateColumns: {
        // Creates a 13-column grid layout
        '13': 'repeat(13, minmax(0, 1fr))',
      },
      gridTemplateRows: {
        // Creates a 13-row grid layout
        '13': 'repeat(13, minmax(0, 1fr))',
      },
    },
  },
  plugins: [],
}

