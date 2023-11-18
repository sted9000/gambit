# gambit
[GambitPLO.com](https://gambitplo.com/) is up and running and FREE to use.

## Description
A tool for learning Pot Limit Omaha opening ranges utilizing Heatmaps.

Seeing that there are 270,725 unique starting hands in Pot Limit Omaha, we need a clever way to think about them rather than learn them one by one. One way, is to learn the patterns (referred to as "shapes") of different categories of hands. Example: Rather than knowing specifically AKQ2, you can simply know the shape of AK combinations. This is what "heatmaps" are designed to do -- allow you to visualize all four card combinations given the best two cards in your hand. IE the hand AKQ2 is shown in the AK heatmap. In my experience learning these shapes help learn efficiently, play quickly, and make less opening blunders! 

Paired with the heatmaps are quizzes that help you test your knowledge. Miss a question a quiz? Take a look at the relevant heatmap and learn from your mistake.

The heatmaps and quizzes are derived from strategies for low-mid stake 6max PLO cash games. 

## How Gambit and Heatmaps Were Made
The data for the strategy was obtained by running large simulations and then grouping the results into categories that would be useful for learning.

### 1 - Design and Run Simulations
The data for the strategy was obtained by running large simulations with [MonkerSolver](https://monkerware.com/solver.html). The results of the large simulations are strategies that are massive and saved in csv files.

### 2 - Manipulate Data
In order for the solver data to be useful, it needed to be manipulated and formatted into heatmaps. I used Python Jupyter Notebooks to do this. The notebooks are in the `notebooks` folder.

### 3 - Store, Host, and Display Data
I used [MongoDB's Atlas](https://www.mongodb.com/atlas) to store the data. I built a simple backend with [ExpressJS](https://expressjs.com/). The frontend is built with [Vue](https://vuejs.org/). The app is hosted on [Heroku](https://www.heroku.com/).

## Todo
- [ ] Add more resources to repo (notebooks, raw data, etc.)
- [ ] Add Auth Provider
- [ ] Update UI with for more context for users (rake, stack size, etc.)
- [ ] Feature: Shareable links with and query params
- [ ] Feature: Look up heatmap from quiz question
