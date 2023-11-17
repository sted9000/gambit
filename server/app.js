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
mongoose
  .connect(process.env.MONGO_URI, {})
  .then(() => console.log("Connected to MongoDB..."))
  .catch((err) => console.error("Could not connect to MongoDB...", err));

// Serve Vue.js static files
app.use(express.static(path.join(__dirname, '../client/dist')));

// Handle SPA for Vue.js routing
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../client/dist/index.html'));
});

// Routes
let routes = require("./routes");
app.use("/", routes);

// Define the port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Listening on port ${PORT}...`));
