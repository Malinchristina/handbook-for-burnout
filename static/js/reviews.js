// Wait for the DOM to fully load before executing the script

document.addEventListener('DOMContentLoaded', function () {
    var deleteModal = document.getElementById('deleteModal');
    var deleteForm = document.getElementById('delete-form');

    // Show the delete modal when the delete button is clicked
    deleteModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var deleteUrl = button.getAttribute('data-delete-url');

        // Set the action of the delete form to the delete URL
        deleteForm.setAttribute('action', deleteUrl);
    });
});
