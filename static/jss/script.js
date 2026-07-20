// Auto hide alerts
setTimeout(function () {

    let alerts = document.querySelectorAll(".alert");

    alerts.forEach(function(alert){

        let bsAlert = bootstrap.Alert.getOrCreateInstance(alert);

        bsAlert.close();

    });

},4000);


// Sidebar Toggle

const toggle = document.getElementById("sidebarToggle");

if(toggle){

    toggle.addEventListener("click",function(){

        document.querySelector(".sidebar").classList.toggle("show");

    });

}
const ctx = document.getElementById("employeeChart");

if (ctx) {

    new Chart(ctx, {

        type: "bar",

        data: {

            labels: ["HR", "IT", "Sales", "Finance"],

            datasets: [{

                label: "Employees",

                data: [12, 20, 8, 10],

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    display: false

                }

            }

        }

    });

}