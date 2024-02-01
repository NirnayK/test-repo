console.log(document)
document.addEventListener('DOMContentLoaded', function () {

    let myDataMeta = document.querySelector('#my_data');

    let jsonData = JSON.parse(myDataMeta.getAttribute('data'));

    let chartCanvas = document.getElementById('myChart');

    new Chart(chartCanvas, {
        type: 'bar',
        data: {
            labels: jsonData.labels,
            datasets: [{
                label: 'Count',
                data: jsonData.counts,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
