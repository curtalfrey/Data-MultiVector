// static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    // Get references to password and confirm password fields
    const passwordField = document.querySelector("#password");
    const confirmPasswordField = document.querySelector("#confirm_password");
    
    // Get reference to the password confirmation message
    const passwordConfirmationMessage = document.querySelector("#password-confirmation-message");
    
    // Function to validate password confirmation
    function validatePasswordConfirmation() {
        const password = passwordField.value;
        const confirmPassword = confirmPasswordField.value;
        
        if (password === confirmPassword) {
            passwordConfirmationMessage.textContent = "Passwords match";
            passwordConfirmationMessage.style.color = "green";
        } else {
            passwordConfirmationMessage.textContent = "Passwords do not match";
            passwordConfirmationMessage.style.color = "red";
        }
    }
    
    // Add event listeners to password and confirm password fields
    passwordField.addEventListener("input", validatePasswordConfirmation);
    confirmPasswordField.addEventListener("input", validatePasswordConfirmation);
});
