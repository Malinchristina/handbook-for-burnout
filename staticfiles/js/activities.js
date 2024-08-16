function ToEditActivity(button) {
    const url = button.getAttribute('data-edit-url');
    window.location.href = url;
}

function ToDeleteActivity(button) {
    const deleteUrl = button.getAttribute('data-delete-url');
    const deleteForm = document.getElementById('delete-form');
    deleteForm.action = deleteUrl;
    const deleteModal = new bootstrap.Modal(document.getElementById(
        'deleteModal'));
    deleteModal.show();
}
