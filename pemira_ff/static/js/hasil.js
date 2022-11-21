const oke = () => {
    console.log("oke");
}

const chart = (type) => {
    const ctx = document.getElementById("chart");

    Chart.defaults.font.size = 16;

    if(type == "bem") type = "ketua-bem";
    else type = "anggota-bpm";

    $.get(`/hasil/${type}/get/`, (data) => {
        var cArr = Object.entries(data);
        cArr = cArr.sort((a, b) => b[1] - a[1]);
        const cNames = cArr.map((c) => c[0]);
        const cVotes = cArr.map((c) => c[1]);

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: cNames,
                datasets: [{
                    label: '# of Votes',
                    data: cVotes,
                    borderWidth: 1,
                    backgroundColor: '#F46521',
                    borderColor: '#150C34'
                }],
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
            },
        });
    });
}