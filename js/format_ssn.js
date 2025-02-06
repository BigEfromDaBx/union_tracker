function formatSSN(input) {
    // Remove all non-digit characters
    let ssn = input.value.replace(/\D/g, '');

    // Apply formatting
    if (ssn.length > 5) {
        ssn = ssn.replace(/(\d{3})(\d{2})(\d{0,4})/, '$1-$2-$3');
    } else if (ssn.length > 3) {
        ssn = ssn.replace(/(\d{3})(\d{0,2})/, '$1-$2');
    }

    // Update the input value
    input.value = ssn;
}