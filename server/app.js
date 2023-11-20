const express = require("express");
const mongoose = require("mongoose");
const path = require("path");
require("dotenv").config();

// Dev Dependencies
const cors = require("cors");

const app = express();

// Middleware
app.use(cors()); // Dev only
app.use(express.json()); // Parse JSON bodies

// Connect to MongoDB
// .connect(process.env.MONGO_URI, {})
mongoose
  .connect(
    "mongodb+srv://gambit-user:XACkRv57F5RQ4gig@gambit-free.zcqjmlq.mongodb.net/gambitPLO?retryWrites=true&w=majority",
    {}
  )
  .then(() => console.log("Connected to MongoDB..."))
  .catch((err) => console.error("Could not connect to MongoDB...", err));

// Serve Vue.js static files
app.use(express.static(path.join(__dirname, "../client/dist")));

// Handle SPA for Vue.js routing
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "../client/dist/index.html"));
});

// Routes
let routes = require("./routes");
app.use("/", routes);

// Define the port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Listening on port ${PORT}...`));
