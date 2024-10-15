function getColorClass(length) {
    if (length < 50) {
        return 'depth-green';
    } else if (length >= 50 && length < 100) {
        return 'depth-yellow';
    } else if (length >= 100 && length < 150) {
        return 'depth-orange';
    } else {
        return 'depth-red';
    }
}

function showNotification(message) {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.classList.add('show');

    // Hide notification after 3 seconds
    setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
}

function fetchDataAndUpdate() {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            console.log('Fetched data:', data); // This line logs fetched data

            const tableBody = document.getElementById('data-table');
            tableBody.innerHTML = ''; // Clear the old table rows

            // Filter out non-numeric and empty entries
            const filteredData = data.filter(item => {
                const numericLength = parseFloat(item.length);
                return !isNaN(numericLength);  // Only include if length is a valid number
            });

            // Populate the table with filtered data
            filteredData.forEach(item => {
                const row = document.createElement('tr');
                const lengthValue = parseFloat(item.length).toFixed(2); // Parse and format the length value
               
                row.innerHTML = `
                    <td>${item.date.split(' ')[0]}</td>
                    <td>${item.time}</td>
                    <td class="${getColorClass(lengthValue)}">${lengthValue}</td>
                `;
                tableBody.appendChild(row);
            });

            // Show the notification popup when data updates
            showNotification('Data Updated');
        })
        .catch(error => console.error('Error fetching data:', error));
}

// Polling every 10 seconds
setInterval(fetchDataAndUpdate, 10000); // 10,000 ms = 10 seconds

// Initial load
document.addEventListener('DOMContentLoaded', fetchDataAndUpdate);