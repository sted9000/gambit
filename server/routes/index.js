/*** Require ***/
const express = require("express");
const heatmapModel = require("../models/heatmapModel");
const quizModel = require("../models/quizModel");
const router = express.Router();

/*** POST Routes ***/
router.post("/heatmap", function (req, res) {
  heatmapModel.queryForResults(req, (error, result) => {
    if (error) {
      console.error(error);
    } else {
      return res.json(result);
    }
  });
});

router.post("/quiz", function (req, res) {
  quizModel.queryForQuiz(req, (error, result) => {
    if (error) {
      console.error(error);
    } else {
      // get the quizzes array from the result
      let quizzes = result.quizzes;

      // turn quizzes into an array
      quizzes = JSON.parse(quizzes);

      // select a random index from the array
      let randomIndex = Math.floor(Math.random() * quizzes.length);

      // Select a random quiz from the results
      let quiz = quizzes[randomIndex];

      // Return the random quiz with a maximum of 20 questions
      return res.json({ quiz: quiz.slice(0, 5), id: randomIndex });
    }
  });
});

/*** Export Router for use in app.js ***/
module.exports = router;
