document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('myForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        // Process form submission here
        form.reset(); // Reset the form fields
    });
});
