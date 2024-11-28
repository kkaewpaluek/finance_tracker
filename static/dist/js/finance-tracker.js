function successToast(messageText) {
    // Create toast HTML and append it to the body
    let toastHtml = `
        <div class="toast-container position-fixed top-0 start-50 translate-middle-x p-3">
            <div id="successToast" class="toast align-items-center text-bg-success border-0" role="alert" aria-live="assertive" aria-atomic="true" data-bs-autohide="true" data-bs-delay="4000">
                <div class="d-flex">
                    <div class="toast-body">
                        ${messageText}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        </div>
    `;

    // Append toast to body
    $('body').append(toastHtml);

    // Show toast notification
    let toastEl = document.getElementById('successToast');
    let toast = new bootstrap.Toast(toastEl);
    toast.show();

    // Optionally, remove the toast element after it disappears
    toastEl.addEventListener('hidden.bs.toast', function () {
        $(toastEl).closest('.toast-container').remove(); // Remove the toast container
    });
}

function failToast(messageText) {
    // Create toast HTML and append it to the body
    let toastHtml = `
        <div class="toast-container position-fixed top-0 start-50 translate-middle-x p-3">
            <div id="failToast" class="toast align-items-center text-bg-danger border-0" role="alert" aria-live="assertive" aria-atomic="true" data-bs-autohide="true" data-bs-delay="6000">
                <div class="d-flex">
                    <div class="toast-body">
                        ${messageText}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        </div>
    `;

    // Append toast to body
    $('body').append(toastHtml);

    // Show toast notification
    let toastEl = document.getElementById('failToast');
    let toast = new bootstrap.Toast(toastEl);
    toast.show();

    // Optionally, remove the toast element after it disappears
    toastEl.addEventListener('hidden.bs.toast', function () {
        $(toastEl).closest('.toast-container').remove(); // Remove the toast container
    });
}