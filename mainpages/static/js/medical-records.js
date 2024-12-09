    // Function to update button text based on the form fields
function updateButtonText() {
    const diagnosis = document.getElementById('diagnosis').value;
    const treatment = document.getElementById('treatment').value;
    const prescription = document.getElementById('prescription').value;
    const amount = document.getElementById('amount').value;
    const notes = document.getElementById('notes').value;
    const nextVisit = document.getElementById('next_visit').value;
    const dueDate = document.getElementById('due_date').value;

    const saveButton = document.getElementById('saveButton');
    
    // Check conditions and update button text accordingly
    if (diagnosis || treatment || prescription) {
        if (amount) {
            saveButton.textContent = 'Save Medical Record & Bill';
        } else {
            saveButton.textContent = 'Save Medical Record';
        }
    } else if (amount) {
        saveButton.textContent = 'Save Bill';
    } else {
        saveButton.textContent = 'Save';
    }
}

// Add event listeners to fields to update the button text when values change
document.getElementById('diagnosis').addEventListener('input', updateButtonText);
document.getElementById('treatment').addEventListener('input', updateButtonText);
document.getElementById('prescription').addEventListener('input', updateButtonText);
document.getElementById('amount').addEventListener('input', updateButtonText);
document.getElementById('notes').addEventListener('input', updateButtonText);
document.getElementById('next_visit').addEventListener('input', updateButtonText);
document.getElementById('due_date').addEventListener('input', updateButtonText);

// Call the function once to initialize button text based on the current field values
updateButtonText();
