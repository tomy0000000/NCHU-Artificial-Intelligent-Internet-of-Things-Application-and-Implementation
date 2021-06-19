function setupAccordion() {
  const bulmaCollapsibleInstances = bulmaCollapsible.attach(".is-collapsible");
}

if (document.readyState != "loading") {
  setupAccordion();
} else {
  document.addEventListener("DOMContentLoaded", setupAccordion);
}
