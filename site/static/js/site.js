// Copy buttons on query blocks.
document.addEventListener("click", (e) => {
  const b = e.target.closest("button.copy");
  if (!b) return;
  navigator.clipboard.writeText(b.parentElement.querySelector("code").innerText).then(() => {
    b.textContent = "Copied"; setTimeout(() => (b.textContent = "Copy"), 1200);
  });
});

// Shade the scores in tables inside [data-heat]: one fixed scale, from pale red at 40% or less,
// through amber at 75%, to green at 100%. A cell is shaded only when it holds one percentage,
// alone or after a condition's name ("84%", "R1 csv 84%", "93% (+12)"), or one range of scores,
// shaded by its middle ("98–100%"); differences, intervals and cells with two scores are left alone.
const STOPS = [[40, 4, 75, 89], [75, 42, 90, 85], [100, 135, 45, 82]];  // score, hue, saturation, lightness
function shade(v) {
  v = Math.max(40, Math.min(100, v));
  const i = v <= 75 ? 0 : 1, [a, b] = [STOPS[i], STOPS[i + 1]], f = (v - a[0]) / (b[0] - a[0]);
  const mix = (k) => a[k] + f * (b[k] - a[k]);
  return `hsl(${mix(1).toFixed(0)}, ${mix(2).toFixed(0)}%, ${mix(3).toFixed(0)}%)`;
}
document.querySelectorAll("[data-heat] td").forEach((td) => {
  const text = td.textContent.trim();
  if ((text.match(/%/g) || []).length !== 1) return;
  const m = text.match(/^(?:[A-Za-z0-9+_-]+\s+){0,2}(\d{1,3})(?:–(\d{1,3}))?%(?:\s|$)/);
  if (m) td.style.background = shade(m[2] ? (+m[1] + +m[2]) / 2 : +m[1]);
});
