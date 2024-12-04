document.getElementById('registerForm').addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevent form submission from reloading the page

    // Gather form data
    const formData = {
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
    };

    try {
        // Send POST request to Flask server
        const response = await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        // Parse response
        const result = await response.json();

        // Display response message
        const responseMessage = document.getElementById('responseMessage');
        if (response.ok) {
            responseMessage.textContent = result.message; // Success message
            responseMessage.style.color = 'green';
        } else {
            responseMessage.textContent = result.error; // Error message
            responseMessage.style.color = 'red';
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('responseMessage').textContent = 'An error occurred.';
    }
});
