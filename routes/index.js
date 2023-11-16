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
      /*** Hacking here ***/
      // Need to turn quizzes string into array
      let quizzes_array = JSON.parse(result.quizzes);
      // Then chose one of the elements randomly to return to client
      let random_quiz =
        quizzes_array[Math.floor(Math.random() * quizzes_array.length)];

      return res.json(random_quiz);
    }
  });
});

/*** Export Router for use in app.js ***/
module.exports = router;