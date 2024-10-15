function getColorClass(depth) {
    if (depth < 50) {
        return 'depth-green';
    } else if (depth >= 50 && depth < 100) {
        return 'depth-yellow';
    } else if (depth >= 100 && depth < 150) {
        return 'depth-orange';
    } else {
        return 'depth-red';
    }
}

function fetchDataAndUpdate() {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            console.log('Fetched data:', data); // Add this line to log the data
            const tableBody = document.getElementById('data-table');
            tableBody.innerHTML = ''; // Clear the old table rows

            data.forEach(item => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.date.split(' ')[0]}</td>
                    <td>${item.time}</td>
                    <td class="${getColorClass(item.depth)}">${item.depth ? item.depth.toFixed(2) : 'N/A'}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
}

// Polling every 10 seconds
setInterval(fetchDataAndUpdate, 10000); // 10,000 ms = 10 seconds

// Initial load
document.addEventListener('DOMContentLoaded', fetchDataAndUpdate);
