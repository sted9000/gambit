/*** Imports ***/
const mongoose = require("mongoose");

/*** Create Schema ***/
let quizSchema = new mongoose.Schema({
  stack_size: String,
  rake_structure: String,
  players: String,
  position: String,
  simple_suit: String,
  quizzes: String,
});

/*** Create Statics (functions) ***/
quizSchema.statics.queryForQuiz = function (req, callback) {
  quizModel
    .findOne({
      stack_size: req.body.stack_size,
      rake_structure: req.body.rake_structure,
      players: req.body.players,
      position: req.body.position,
      simple_suit: req.body.simple_suit,
    })
    .then((results) => {
      return callback(null, results);
    })
    .catch((err) => {
      return callback(err);
    });
};

/*** Turn Schema into Model ***/
// A model is a class with which we construct documents.
let quizModel = mongoose.model("quizModel", quizSchema, "quizzes");

/*** Export Model for use in App ***/
module.exports = quizModel;
