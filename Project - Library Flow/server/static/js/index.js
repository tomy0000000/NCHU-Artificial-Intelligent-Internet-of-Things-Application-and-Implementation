function setupAccordion() {
  const bulmaCollapsibleInstances = bulmaCollapsible.attach(".is-collapsible");
  bulmaCollapsibleInstances.forEach((bulmaCollapsibleInstance) => {
    // Check if current state is collapsed or not
    let chart;
    let section_id = bulmaCollapsibleInstance.element.dataset.section_id;
    let container = document.getElementById(`${section_id}-chart-div`);
    bulmaCollapsibleInstance.on("before:expand", (event) => {
      fetch(`/record/${section_id}`)
        .then((response) => response.json())
        .then((data) => {
          console.log(data);

          // Clean up container
          container.querySelectorAll("*").forEach((n) => n.remove());

          // Place content based on data
          if (data.length > 0) {
            chart = drawChart(container, data);
          } else {
            placeNoDataNotification(container);
          }
        });
    });
    bulmaCollapsibleInstance.on("after:collapse", (event) => {
      // container.querySelectorAll("*").forEach((n) => n.remove());
      container.classList.remove("py-3");
      if (chart !== undefined) {
        chart.destroy();
      }
    });
  });
}

function placeNoDataNotification(container) {
  let notification = document.createElement("div");
  notification.classList.add("notification");
  notification.classList.add("is-info");
  notification.classList.add("is-light");
  notification.classList.add("mx-auto");
  notification.classList.add("my-auto");
  notification.style.width = "80%";
  notification.innerText = "No Data";
  container.appendChild(notification);
  container.classList.add("py-3");
}

function drawChart(container, data) {
  let ctx = document.createElement("canvas");
  ctx.classList.add("p-2");

  let chart = new Chart(ctx, {
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
      scales: { x: { type: "timeseries" } },
    },
  });
  container.appendChild(ctx);
  return chart;
}

function ready() {
  setupAccordion();
}

if (document.readyState !== "loading") {
  ready();
} else {
  document.addEventListener("DOMContentLoaded", ready);
}
