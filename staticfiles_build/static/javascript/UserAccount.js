document.addEventListener('DOMContentLoaded', function () {
    const searchBox = document.querySelector('#search-box');
    const tableBody = document.querySelector('#data-table tbody');
    const rows = tableBody.querySelectorAll('tr');

    searchBox.addEventListener('input', function () {
        const query = this.value.toLowerCase();

        rows.forEach((row) => {
            const nameCell = row.querySelector('td:nth-child(1)').textContent.toLowerCase();
            const placeCell = row.querySelector('td:nth-child(2)').textContent.toLowerCase();
            const blockCell = row.querySelector('td:nth-child(3)').textContent.toLowerCase();
            const dateCell = row.querySelector('td:nth-child(4)').textContent.toLowerCase();
            const pnameCell = row.querySelector('td:nth-child(5)').textContent.toLowerCase();
            const pweightCell = row.querySelector('td:nth-child(6)').textContent.toLowerCase();

            if (
                nameCell.includes(query) ||
                placeCell.includes(query) ||
                blockCell.includes(query) ||
                dateCell.includes(query) ||
                pnameCell.includes(query) ||
                pweightCell.includes(query) 
                

            ) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });
});