const express = require("express");
const mongoose = require("mongoose");
require("dotenv").config();

// Dev Dependencies
const cors = require("cors");

const app = express();

// Middleware
app.use(cors()); // Dev only
app.use(express.json()); // Parse JSON bodies

// Connect to MongoDB
const uri = process.env.MONGO_URI;
mongoose
  .connect(uri, {})
  .then(() => console.log("Connected to MongoDB..."))
  .catch((err) => console.error("Could not connect to MongoDB...", err));

// Routes
let routes = require("./routes");
app.use("/", routes);

// Define the port
const port = process.env.PORT || 8080;
app.listen(port, () => console.log(`Listening on port ${port}...`));
