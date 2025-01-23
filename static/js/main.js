document.addEventListener("DOMContentLoaded", () => {
    // Select error notification container
    const errorNotification = document.getElementById("error-notification");
    const examDropdown = document.getElementById("exam-dropdown");
    const questionIdsInput = document.getElementById("question-ids");

    // Add event listener for exam dropdown change
    if (examDropdown) {
        examDropdown.addEventListener("change", () => {
            if (errorNotification) {
                errorNotification.style.display = "none";
            }
        });
    }

    // Add event listener for input in Question IDs field
    if (questionIdsInput) {
        questionIdsInput.addEventListener("input", () => {
            if (errorNotification) {
                errorNotification.style.display = "none";
            }
        });
    }
});
