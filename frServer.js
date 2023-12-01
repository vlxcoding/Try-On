// const express = require("express");
// const bodyParser = require("body-parser");

// const app = express();
// const port = 3000;

// // Middleware to parse JSON requests
// app.use(bodyParser.json());

// // Sample array to store feedback
// let feedbackList = [];

// // Endpoint to get feedback
// app.get("/feedback", (req, res) => {
//     res.json(feedbackList);
// });

// // Endpoint to submit feedback
// app.post("/feedback", (req, res) => {
//     const newFeedback = req.body.feedback;
//     feedbackList.push(newFeedback);
//     res.json({ message: "Feedback submitted successfully." });
// });

// // Start the server
// app.listen(port, () => {
//     console.log(`Server is running on port ${port}`);
// });

const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const http = require("http")
const fs = require("fs")
const fileContent = fs.readFileSync("feedbackandreview.html")

const server = http.createServer((req, res)=>{
    res.writeHead(200, {"Content-type " : "text/html"})
    res.end(fileContent)
})

const app = express();
const port = 3001;

app.use(bodyParser.json());

// Connect to MongoDB (replace 'your_database_url' with your actual MongoDB connection string)
mongoose.connect("mongodb+srv://cloviswallace:<SE2140dointoomuch>@clocluster01.f2esnvf.mongodb.net/?retryWrites=true&w=majority", { useNewUrlParser: true, useUnifiedTopology: true });

// Define a Feedback schema
const feedbackSchema = new mongoose.Schema({
    text: String,
});

// Create a Feedback model
const Feedback = mongoose.model("Feedback", feedbackSchema);

// Endpoint to get feedback
app.get("/api/feedback", async (req, res) => {
   ///try {
        //const feedbackList = await Feedback.find();
    res.json(Feedback);
   // } catch (error) {
    //    res.status(500).json({ message: error.message });
    //}
});

// Endpoint to submit feedback
app.post("/api/feedback", async (req, res) => {
    const newFeedback = req.body;
    feedbackList.push(newFeedback);
    res.json({ message: "Feedback submitted successfully." });
});

// Serve static files (HTML, CSS, JS)
app.use(express.static("public"));
//     const feedbackText = req.body.text;

//     try {
//         const newFeedback = new Feedback({ text: feedbackText });
//         await newFeedback.save();
//         res.status(201).json({ message: "Feedback submitted successfully." });
//     } catch (error) {
//         res.status(400).json({ message: error.message });
//     }
// });

// Start the server
// server.listen(port, "127.0.0.1", () => {
//     console.log(`Server is running on port ${port}`);
// });
