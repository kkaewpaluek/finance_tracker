function formatTable(){
    const tableRows = document.querySelectorAll('.ft-table-format tr');

    tableRows.forEach(row => {
        const rawAmountCell = row.querySelector('[data-column="rawAmount"]');
        const enabledCell = row.querySelector('[data-column="enabled"]'); // Select cell within the current row
        console.log('this is format table.');

        if(rawAmountCell){
            const rawAmountValue = parseFloat(rawAmountCell.textContent.trim());

            // Format the value under rawAmount column to a general accounting format (comma, two decimals)
            const formattedAmount = new Intl.NumberFormat('en-US', {
                style: 'decimal',
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            }).format(rawAmountValue);

            // Update the cell text with formatted value
            rawAmountCell.textContent = formattedAmount;

            // Apply color formatting rawAmount column based on the value
            // green if > 0
            // gray if = 0
            // red if < 0
            if (rawAmountValue > 0) {
                rawAmountCell.classList.add("text-success"); // Green
            } else if (rawAmountValue === 0) {
                rawAmountCell.classList.add("text-secondary"); // Gray
            } else if (rawAmountValue < 0) {
                rawAmountCell.classList.add("text-danger"); // Red
            }
        }

        // Formating the disable item
        if(enabledCell){
            if (enabledCell.textContent.trim() === 'False') { // Use jQuery methods for text content
                if (!row.classList.contains('row_disabled')) { // Check if the row doesn't already have the 'table_disabled' class
                    row.classList.add('row_disabled'); // Add class using jQuery
                    console.log('added');
                }
            }
            else {
                row.classList.remove('row_disabled');
            }
        }
    });

}

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