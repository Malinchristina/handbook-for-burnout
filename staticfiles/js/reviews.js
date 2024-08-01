document.addEventListener('DOMContentLoaded', function () {
    var deleteModal = document.getElementById('deleteModal');
    var deleteForm = document.getElementById('deleteForm');

    deleteModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var deleteUrl = button.getAttribute('data-delete-url');
        deleteForm.setAttribute('action', deleteUrl);
    });
});

function ToEditReview(button) {
    const url = button.getAttribute('data-edit-url');
    window.location.href = url;
}