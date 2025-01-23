// Function to handle the CSV download
function downloadCSV() {
    // Get the data from the data-container element
    const dataContainer = document.getElementById("data-container");
    const columns = JSON.parse(dataContainer.getAttribute("data-columns"));
    const data = JSON.parse(dataContainer.getAttribute("data-data"));

    // Get the current date for the filename
    const today = new Date();
    const day = today.getDate().toString().padStart(2, '0');
    const month = today.toLocaleString('default', { month: 'short' });
    const year = today.getFullYear().toString().slice(2);

    // Construct the filename using the current date
    const fileName = `tagging_data_${day}_${month}_${year}.csv`;

    // Convert data to CSV format
    const csvContent = "data:text/csv;charset=utf-8," + 
        columns.join(",") + "\n" + 
        data.map(row => columns.map(column => row[column]).join(",")).join("\n");

    // Create a download link
    const encodedUri = encodeURI(csvContent);
    const downloadLink = document.createElement("a");
    downloadLink.setAttribute("href", encodedUri);
    downloadLink.setAttribute("download", fileName);
    document.body.appendChild(downloadLink);

    // Trigger the download
    downloadLink.click();
    document.body.removeChild(downloadLink);
}
