# gambit
[GambitPLO.com](https://gambitplo.com/) is up and running and free to use.

## Description
A tool for learning Pot Limit Omaha opening ranges utilizing Heatmaps.

Seeing that there are 270,725 unique starting hands in Pot Limit Omaha, we need a clever way to think about them rather than learn them one by one. One way, is to learn the patterns (referred to as "shapes") of different categories of hands. Example: Rather than knowing specifically AKQ2, you can simply know the shape of AK combinations. This is what "heatmaps" are designed to do -- allow you to visualize all four card combinations given the best two cards in your hand. IE the hand AKQ2 is shown in the AK heatmap. In my experience learning these shapes help learn efficiently, play quickly, and make less opening blunders!

Paired with the heatmaps are quizzes that help you test your knowledge. Miss a question a quiz? Take a look at the relevant heatmap and learn from your mistake.

The heatmaps and quizzes are derived from strategies for low-mid stake 6max PLO cash games.

## How Gambit and Heatmaps Were Made
The data for the strategy was obtained by running large simulations and then grouping the results into categories that would be useful for learning.

### 1 - Design and Run Simulations
The data for the strategy was obtained by running large simulations with [MonkerSolver](https://monkerware.com/solver.html). The results of the large simulations are strategies that are massive and saved in csv files.

### 2 - Capture the Data
The results of the simulation are saved in an illegible file format. I wrote a script using [PyAutoGUI](https://github.com/asweigart/pyautogui) to traverse the MonkerSolver UI and export the data as csv files.

### 3 - Manipulate Data
In order for the solver data to be useful, it needed to be manipulated and formatted into heatmaps. The Jupyter Notebook is in the `resources/notebook` folder.

### 4 - Store, Host, and Display Data
- Heatmap and quiz data is stored in a [MongoDB Atlas Database](https://www.mongodb.com/atlas).
- The server is build with [ExpressJS](https://expressjs.com/).
- The web ui is built with [Vue](https://vuejs.org/).
- The app is hosted on [Heroku](https://www.heroku.com/).

## Resources
- The processed data is in the `resources/data` folder.
- The Jupyter Notebook used to process the raw data are in the `resources/notebook` folder.
- Scripts to scrape the data from the MonkerSolver files are in the `resources/scripts` folder.

## Todo
- [ ] Update UI with for more context for users (rake, stack size, etc.)
- [ ] Feature: Shareable links with and query params
- [ ] Feature: Look up heatmap from quiz question
