function ToEditActivity(button) {
    const url = button.getAttribute('data-edit-url');
    window.location.href = url;
}

function ToDeleteActivity(button) {
    const url = button.getAttribute('data-delete-url');
    const deleteConfirm = document.getElementById('deleteConfirm');
    deleteConfirm.setAttribute('href', url);
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    deleteModal.show();
}
