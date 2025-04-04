// Import dependencies
const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');

// Initialize app
dotenv.config();
const app = express();

// Middleware
app.use(express.json()); // For JSON body parsing
app.use(cors()); // Enable CORS for frontend connection

// Default Route
app.get('/', (req, res) => {
    res.send('AI-Based Student Assessment Backend is Running 🚀');
});

// Server Port
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
