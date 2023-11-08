# gambit
This app is still in development. The app is currently hosted at [gambitplo.com](https://gambitplo.com/).

## Description
This app is a tool for learning Pot Limit Omaha opening ranges. Visualize a situations opening range using "Heatmaps" or test your knowledge of a situation with a quiz.

## Process and Data
The data for the strategy was obtained by running large simulations ([MonkerSolver](https://monkersolver.com/)) and then grouping the results into useful categories.

### Steps
1. Design simulations
2. Run simulations
3. Capture results with Pyautogui
4. Manipulate data with Python Jupyter Notebooks
5. Store the date in database
6. Build app / user interface
7. Host app and server with database

## Todo
- [ ] Add more resources to repo (notebooks, raw data, etc.)
- [ ] Add reset button for quiz
- [ ] Refactor for real dataset
- [ ] Host backend with db and auth
- [ ] Update UI with for more context for users (rake, stack size, etc.)
- [ ] Feature: Heatmap link and query params
- [ ] Feature: Look up heatmap from quiz question
