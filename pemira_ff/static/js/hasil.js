const oke = () => {
    console.log("oke");
}

const chart = (type) => {
    const ctx = document.getElementById("chart");

    Chart.defaults.font.size = 16;

    if(type == "bem") type = "ketua-bem";
    else type = "anggota-bpm";

    $.get(`/hasil/${type}/get/`, (data) => {
        const cNames = Object.keys(data);
        const cVotes = cNames.map((c) => data[c]);

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: cNames,
                datasets: [{
                    label: '# of Votes',
                    data: cVotes,
                    borderWidth: 1,
                    backgroundColor: '#FC7723',
                    borderColor: '#000'
                }]
            },
            options: {
                indexAxis: 'y',
                barPercentage: 0.3,
                responsive: true,
                maintainAspectRatio: false,
                scales:{
                    x: {
                        title: {
                            display: true,
                            text: 'Jumlah Pemilih',
                        },
                    }
                }
            }
        });
    });
}