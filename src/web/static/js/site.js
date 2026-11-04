// Copy buttons on query blocks.
document.addEventListener("click", (e) => {
  const b = e.target.closest("button.copy");
  if (!b) return;
  navigator.clipboard.writeText(b.parentElement.querySelector("code").innerText).then(() => {
    b.textContent = "Copied"; setTimeout(() => (b.textContent = "Copy"), 1200);
  });
});
