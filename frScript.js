// Sample data for initial reviews
// const initialReviews = [
//     "Great software! Very user-friendly.",
//     "Found a bug in the latest update.",
//     "Excellent customer support."
// ];

document.addEventListener("DOMContentLoaded", function () {
    // Fetch and display initial reviews
    fetchReviews();

    // Set up event listener for submitting feedback
    document.getElementById("feedbackText").addEventListener("keydown", function (event) {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();
            submitFeedback();
        }
    });
});

// document.addEventListener("DOMContentLoaded", function () {
//     // Display initial reviews
//     displayReviews(initialReviews);
// });

function fetchReviews() {
    fetch("/api/feedback")
        .then(response => response.json())
        .then(reviews => displayReviews(reviews))
        .catch(error => console.error("Error fetching reviews:", error));
}


// function sendFetchRequest(method, url, data, callback) {
//     const options = {
//         method: method,
//         headers: {
//             "Content-Type": "application/json",
//         },
//     };

//     // Add request body if data is provided
//     if (data) {
//         options.body = JSON.stringify(data);
//     }

//     fetch(url, options)
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error(`HTTP Error: ${response.status}`);
//             }
//             return response.json();
//         })
//         .then(responseData => callback(null, responseData))
//         .catch(error => callback(error.message));
// }

// // Example usage:
// const Url = "http://127.0.0.1:5500/feedbackandreview.html";
// const requestData = { key: "value" };




function submitFeedback() {
    var feedbackText = document.getElementById("feedbackText").value;

    // Make a POST request to submit feedback
    fetch("/api/feedback", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: feedbackText }),
    })
    .then(response => response.json())
    .then(() => {
        // Fetch and display updated reviews after submission
        fetchReviews();
    })
    .catch(error => console.error("Error submitting feedback:", error));

    // Clear the input field
    document.getElementById("feedbackText").value = "";
}


    //initialReviews.push(feedbackText);

    // sendFetchRequest("POST", Url, feedbackText, function (error, responseData) {
    //     if (error) {
    //         console.error(error);
    //     } else {
    //         console.log(responseData);
    //     }
    // });
    
    // Clear the input field
    //document.getElementById("feedbackText").value = "";

    // Send data to the backend

    // fetch('/process', {
    //     method: method,
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({ feedbackText: feedbackText})
    // })
    // .then(response => response.json())
    // .then(data => {
    //     // Handle the response from the backend
    //     console.log(data);
    // })
    // .catch(error => {
    //     console.error('Error:', error);
    // });

    // Display the updated reviews
    //displayReviews(initialReviews);
//}

function displayReviews(reviews) {
    const reviewsList = document.getElementById("reviewsList");
    reviewsList.innerHTML = ""; // Clear previous reviews

    // Populate the reviews list
    reviews.forEach(review => {
        const li = document.createElement("li");
        li.textContent = review.text;
        reviewsList.appendChild(li);
    });
}

// function displayReviews(reviews) {
//     const reviewsList = document.getElementById("reviewsList");
//     reviewsList.innerHTML = ""; // Clear previous reviews

//     // Populate the reviews list
//     reviews.forEach(review => {
//         const li = document.createElement("li");
//         li.textContent = review;
//         reviewsList.appendChild(li);
//     });
// }
