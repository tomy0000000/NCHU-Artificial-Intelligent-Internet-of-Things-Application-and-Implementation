function setupAccordion() {
  const bulmaCollapsibleInstances = bulmaCollapsible.attach(".is-collapsible");
  bulmaCollapsibleInstances.forEach((bulmaCollapsibleInstance) => {
    // Check if current state is collapsed or not
    bulmaCollapsibleInstance.on("after:expand", (event) => {
      let section_id = event.element.dataset.section_id;
      fetch(`/record/${section_id}`)
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          data.map((item) => {
            item.timestamp = moment(item.timestamp).fromNow();
          });
          drawChart(section_id, data);
        });
    });
  });
}

function drawChart(section_id, data) {
  let ctx = document.getElementById(`${section_id}-chart`).getContext("2d");
  let stackedLine = new Chart(ctx, {
    type: "line",
    data: { datasets: [{ data: data }] },
    options: {
      elements: {
        point: { borderColor: "rgb(75, 192, 192)" },
        line: { borderColor: "rgb(75, 192, 192)", fill: false, tension: 0.1 },
      },
      plugins: { legend: { display: false } },
      parsing: {
        xAxisKey: "timestamp",
        yAxisKey: "status",
      },
    },
  });
}

function ready() {
  setupAccordion();
}

if (document.readyState !== "loading") {
  ready();
} else {
  document.addEventListener("DOMContentLoaded", ready);
}
