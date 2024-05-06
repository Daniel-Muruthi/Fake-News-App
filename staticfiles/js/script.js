document.getElementById('newsForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var newsInput = document.getElementById('newsInput').value;
    fetch('/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: newsInput }),
    })
    .then(response => response.json())
    .then(data => {
        Swal.fire({
            title: 'Prediction',
            text: data.prediction,
            icon: 'info',
            confirmButtonText: 'OK'
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// ////////subscription success alert //////////

// Execute the code when the document is ready
document.addEventListener('DOMContentLoaded', function() {
    // Select the form and attach a submit event handler
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Perform AJAX request
        var xhr = new XMLHttpRequest();
        var formData = new FormData(this);
        xhr.open('POST', this.action, true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    // Display success message if response indicates success
                    if (response.success) {
                        Swal.fire({
                            icon: 'success',
                            title: 'Success!',
                            text: 'Your message has been sent successfully!',
                        });
                        // Reset the form
                        document.getElementById('contactForm').reset();
                    } else {
                        // Display error message if response indicates failure
                        Swal.fire({
                            icon: 'error',
                            title: 'Oops...',
                            text: 'There was an error processing your request. Please check the form and try again.',
                        });
                    }
                } else {
                    // Display error message if AJAX request fails
                    console.error(xhr.responseText);
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'There was an error processing your request. Please try again later.',
                    });
                }
            }
        };
        xhr.send(formData);
    });
});


