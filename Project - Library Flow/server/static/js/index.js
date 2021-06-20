async function getRecords(section_id) {
  try {
    response = await fetch(`/record/${section_id}`);
    return response.json();
  } catch (error) {
    console.error(error);
  }
}

async function getPredictRecords(section_id) {
  try {
    response = await fetch(`/predict_record/${section_id}`);
    return response.json();
  } catch (error) {
    console.error(error);
  }
}

function setupAccordion() {
  const bulmaCollapsibleInstances = bulmaCollapsible.attach(".is-collapsible");
  bulmaCollapsibleInstances.forEach((bulmaCollapsibleInstance) => {
    // Check if current state is collapsed or not
    let chart;
    let section_id = bulmaCollapsibleInstance.element.dataset.section_id;
    let container = document.getElementById(`${section_id}-chart-div`);
    bulmaCollapsibleInstance.on("before:expand", async (event) => {
      records = await getRecords(section_id);
      predict_records = await getPredictRecords(section_id);
      console.log(records);

      // Clean up container
      container.querySelectorAll("*").forEach((n) => n.remove());

      // Place content based on data
      if (records.length > 0) {
        chart = drawChart(container, records, predict_records);
      } else {
        placeNoDataNotification(container);
      }
    });
    bulmaCollapsibleInstance.on("after:collapse", (event) => {
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

function drawChart(container, data, predict_data) {
  let ctx = document.createElement("canvas");
  ctx.classList.add("p-2");

  let chart = new Chart(ctx, {
    type: "line",
    data: {
      datasets: [
        { data: data },
        { data: [data[0], predict_data[0]] },
        { data: predict_data, borderDash: [5, 5] },
      ],
    },
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
      scales: {
        x: { type: "time", time: { unit: "minute" } },
      },
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
