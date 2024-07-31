function ToEditReview(button) {
    const url = button.getAttribute('data-edit-url');
    window.location.href = url;
}