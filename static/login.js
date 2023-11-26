// Login Function
const MY_SERVER = "https://dgango-supermarker.onrender.com/";

const login = async () => {
    try {
        const res = await axios.post(MY_SERVER + "login/", {
            "username": username.value,
            "password": password.value
        });
        console.log(res.data.access);
        console.log({"username": username.value , "password": password.value});
        sessionStorage.setItem("token", res.data.access);
        const user = parseJwt(res.data.access).username;
        successMessage.innerHTML = `<h1>Welcome, ${user}!</h1>`;
        successMessage.innerHTML = "";

        // Redirect to the main page after a successful login
        window.location.href = "index.html";
    } catch (error) {
        if (error.response && error.response.status === 401) {
            successMessage.innerHTML = "Invalid username or password. Please try again.";
        } else if (error.response && error.response.status === 500) {
            successMessage.innerHTML = "Server error. Please try again later.";
        } else {
            successMessage.innerHTML = "An unexpected error occurred. Please try again.";
        }
        successMessage.innerHTML = "";
    }
};

// Signup Function
const signup = async () => {
    try {
        const res = await axios.post(MY_SERVER + "register", {
            "username": signupUsername.value,
            "password": signupPassword.value
        });
        console.log(res.data.detail);
        // Clear previous feedback
        signupFeedback.innerHTML = "";
        // Show success message or perform other actions
        signupGreat.innerHTML = `<h1>Registration successful!</h1>`;

        // Redirect to the main page after a successful signup
        window.location.href = "index.html";
    } catch (error) {
        // Check if it's a 400 Bad Request with a specific error message
        if (error.response && error.response.status === 400 && error.response.data.detail) {
            // Display the specific error message to the user
            signupFeedback.innerHTML = error.response.data.detail;
        } else {
            // Display a generic error message for other types of errors
            signupFeedback.innerHTML = "An error occurred during registration. Please try again.";
        }
        // Clear any success message
        signupGreat.innerHTML = "";
    }
};

// JWT Parsing Function
function parseJwt(token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}