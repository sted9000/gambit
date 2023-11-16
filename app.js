const express = require("express");
const mongoose = require("mongoose");

// Dev Dependencies
const cors = require("cors");

const app = express();

// Middleware
app.use(cors()); // Dev only
app.use(express.json()); // Parse JSON bodies

// Connect to MongoDB
mongoose
  .connect("mongodb://localhost:27017/gambitPLO", {})
  .then(() => console.log("Connected to MongoDB..."))
  .catch((err) => console.error("Could not connect to MongoDB...", err));

// Routes
let routes = require("./routes/index.js");
app.use("/", routes);

// Define the port
const port = process.env.PORT || 8080;
app.listen(port, () => console.log(`Listening on port ${port}...`));
