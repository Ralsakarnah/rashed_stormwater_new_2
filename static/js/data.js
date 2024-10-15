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

            data.forEach(item => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.date.split(' ')[0]}</td>
                    <td>${item.time}</td>
                    <td class="${getColorClass(item.length)}">${item.length ? item.length.toFixed(2) : 'N/A'}</td>
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
