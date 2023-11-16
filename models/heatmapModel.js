/*** Imports ***/
const mongoose = require("mongoose");

/*** Create Schema ***/
let heatmapSchema = new mongoose.Schema({
  stack_size: String,
  rake_structure: String,
  players: String,
  position: String,
  // is_pair: Boolean,
  simple_suit: String,
  detailed_suit: String,
  showdown_cards: String,
  map: String,
});

/*** Create Statics (functions) ***/
heatmapSchema.statics.queryForResults = function (req, callback) {
  heatmapModel
    .findOne({
      stack_size: req.body.stack_size,
      rake_structure: req.body.rake_structure,
      players: req.body.players,
      position: req.body.position,
      simple_suit: req.body.simple_suit,
      detailed_suit: req.body.detailed_suit,
      showdown_cards: req.body.showdown_cards,
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
let heatmapModel = mongoose.model("heatmapModel", heatmapSchema, "heatmap");

/*** Export Model for use in App ***/
module.exports = heatmapModel;
