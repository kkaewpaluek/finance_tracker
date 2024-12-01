function formatTable(){
    const tableRows = $('.ft-table-format tr');

    tableRows.each(function () {
        const row = $(this);

        const categoryCell = row.find('[data-column="category"]');
        const categoryTypeCell = categoryCell.data('categorytype'); // Use .data() for data attributes
        const rawAmountCell = row.find('[data-column="rawAmount"]');
        const enabledCell = row.find('[data-column="enabled"]');

        if (rawAmountCell.length) {
            const rawAmountValue = parseFloat(rawAmountCell.text().trim());

            // Format the value under rawAmount column to a general accounting format (comma, two decimals)
            const formattedAmount = new Intl.NumberFormat('en-US', {
                style: 'decimal',
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            }).format(rawAmountValue);

            // Update the cell text with formatted value
            rawAmountCell.text(formattedAmount);

            // Apply color formatting rawAmount column based on the categoryType and value
            if ('Saving' === categoryTypeCell) {
                rawAmountCell.addClass('text-primary'); // Blue
            } else {
                if (rawAmountValue > 0) {
                    rawAmountCell.addClass('text-success'); // Green
                } else if (rawAmountValue === 0) {
                    rawAmountCell.addClass('text-gray-500'); // Gray
                } else if (rawAmountValue < 0) {
                    rawAmountCell.addClass('text-danger'); // Red
                }
            }
        }

        // Formatting the disabled item
        if (enabledCell.length) {
            if (enabledCell.text().trim() === 'False') {
                if (!row.hasClass('row_disabled')) {
                    row.addClass('row_disabled');
                }
            } else {
                row.removeClass('row_disabled');
            }
        }
    });

}

/* function formatInputToAccounting(inputElement) {
    let value = inputElement.value.replace(/,/g, ''); // Remove existing commas
    if (!value) return; // If there's no value, return early
    const number = parseFloat(value);
    
    if (!isNaN(number)) {
        inputElement.value = number.toLocaleString('en-US', { 
            style: 'decimal', 
            minimumFractionDigits: 2, 
            maximumFractionDigits: 2 
        });
    }
} */

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



class NumberInputFormatter {
    constructor(selectorOrElement, onChangeCallback, options={}) {
        // Check if selectorOrElement is a jQuery object or a string selector
        this.$input = selectorOrElement instanceof jQuery ? selectorOrElement : $(selectorOrElement);
        this.onChangeCallback = onChangeCallback;

        // Set initial values to 0 if undefined
        this.$input.val(this.$input.val() || 0).data('realvalue', this.$input.data('realvalue') || 0);

        this.options = options;

        if (this.options.int){
            this.max_digit = 0;
            this.min_digit = 0;
        }
        else{
            // Sanitize min/max digit
            this.max_digit = Math.min(this.options.max_digit ?? 2, 2);
            this.min_digit = Math.min(this.options.min_digit ?? 2, this.max_digit);
        }



        // Set up event handlers
        this.initEventHandlers();
    }

    initEventHandlers() {
        // Allow only numeric input with number-related keys
        this.$input.on('keydown', (event) => {
            // Allow: backspace, delete, tab, escape, and other navigation keys
            if ([46, 8, 9, 27].includes(event.keyCode) ||
                // Allow: Ctrl/cmd+A, Ctrl/cmd+C, Ctrl/cmd+V, Ctrl/cmd+X
                (event.keyCode === 65 && (event.ctrlKey || event.metaKey)) ||
                (event.keyCode === 67 && (event.ctrlKey || event.metaKey)) ||
                (event.keyCode === 86 && (event.ctrlKey || event.metaKey)) ||
                (event.keyCode === 88 && (event.ctrlKey || event.metaKey)) ||
                // Allow: home, end, left, right
                (event.keyCode >= 35 && event.keyCode <= 39)) {
                return;
            }

            // Allow: numbers and number-related characters (-, ., e)
            if ((event.key >= '0' && event.key <= '9') || event.key === '-' || event.key === '.') {
                return;
            }


            // if Enter
            if (event.keyCode === 13){
                this.formatAndSetRealValue();
                if (typeof this.onChangeCallback === 'function') {
                    this.onChangeCallback(this.$input);
                }
            }

            // Prevent other keys
            event.preventDefault();
        });

        // Trigger change callback on blur if a callback is provided
        this.$input.on('blur', () => {

            this.formatAndSetRealValue();

            if (typeof this.onChangeCallback === 'function') {
                this.onChangeCallback(this.$input);
            }
        });


        //display realvalue when click
        this.$input.on('click', () => {
            let value = this.$input.data('realvalue');
            this.$input.val(value).select();
        });
    }

    formatAndSetRealValue() {
        const rawValue = this.$input.val().replace(/[^0-9.-]/g, '');
        const realValue = parseFloat(rawValue).toFixed(this.options.int? 0 : 2); // Retain the full precision

        if (!isNaN(realValue)) {
            // Set the data-realvalue attribute
            this.$input.data('realvalue', realValue);

            // Format to 2 decimal places with commas
            const formattedValue = parseFloat(realValue).toLocaleString('en-US', {
                minimumFractionDigits: this.min_digit,
                maximumFractionDigits: this.max_digit
            });

            this.$input.val(formattedValue);
        } else {
            this.$input.val('0');
            this.$input.data('realvalue', '0');
        }
    }


    setValue(floatValue, trigger = false) {


        const rawValue = String(floatValue).replace(/[^0-9.-]/g, '');

        if (!isNaN(rawValue)) {
            // Set the data-realvalue attribute to the exact float value
            this.$input.data('realvalue', parseFloat(rawValue).toFixed(this.options.int? 0 : 2));

            // Format the float value to 2 decimal places with commas
            const formattedValue = parseFloat(rawValue).toLocaleString('en-US', {
                minimumFractionDigits: this.min_digit,
                maximumFractionDigits: this.max_digit
            });

            // Update the input field with the formatted value
            this.$input.val(formattedValue);

            // Trigger the change callback if provided
            if (typeof this.onChangeCallback === 'function' && trigger) {
                this.onChangeCallback(this.$input);
            }
        }
    }
}



