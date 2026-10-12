document.addEventListener("DOMContentLoaded", () => {
    const rows = document.querySelectorAll(".professional-table tbody tr");

    rows.forEach((row) => {
        row.addEventListener("focusin", () => row.classList.add("row-focused"));
        row.addEventListener("focusout", () => row.classList.remove("row-focused"));
    });
});
