# Two-Model Comparison — Perfectly Tuned vs Off-the-Shelf

**Date:** 2026-07-18 · **Method:** both models run through the calibrated MOC digital bench (`tools/design/ram_moc_sim.py`) at an identical site: 100 mm ram, 1.5 m fall, 15 m drive pipe, headstock +9 m (r = 6). Ratios are the trustworthy output; absolutes await bench correlation (±10% gate).

## The two builds

| | **Model T — tuned** | **Model C — off-the-shelf** |
|---|---|---|
| Drive pipe | steel sch40 (wave speed ~1,337 m/s) | PVC sch40 (wave speed ~407 m/s) |
| Waste valve | machined, 8 mm stroke, weight tuned (swept) | swing-check, ~25 mm sloppy stroke, untuned weight |
| Snifter | 1.0 mm check-valve type | plain drilled hole (leaks spike energy) |
| Wheel | quality Pelton (0.75) | plastic kit wheel (0.65) |
| Powertrain BOM (CAD, est.) | **~$2,300** (+$150 self-tuning option) | **~$1,200** |

## Simulated results (identical water)

| Metric | Model T | Model C | T/C |
|---|---|---|---|
| Ram efficiency (D'Aubuisson) | **0.634** | **0.249** | **2.5×** |
| Delivery to headstock | 0.22 L/s (19,000 L/day) | 0.13 L/s (11,200 L/day) | 1.7× |
| Electric output | ~12 W | ~6 W | **1.95×** |
| Annual energy | ~102 kWh | ~52 kWh | — |

The dominant killers of Model C, in order: **PVC's low wave speed** (weak pressure spike — exactly Watt's 1975 warning, now reproduced by our own transient model), the sloppy long-stroke valve (wastes drive water per cycle), and the leaking snifter. Tuning and materials together are worth **roughly a doubling of output from the same water.**

## Is the juice worth the squeeze? — the honest, split verdict

**For WATER delivery: yes, decisively.** The tuned unit lifts ~19,000 L/day vs ~11,200 — for a cistern, herd, or garden that's the difference between adequate and short, from identical water rights. And steel-vs-PVC is also a *lifespan* verdict: PVC fatigues under water hammer; field PVC rams die young while steel rams run decades. For the ram-alone water product (Rife/AIDFI market), build tuned, always.

**For WATTS at pico scale: marginal — and that's a real business finding.** The ~$1,100 tuning premium buys ~50 kWh/yr at this size: $17–50/yr even at remote prices → 20–60 year payback on the premium alone. At the 300 mm/bank scale the same ratio yields ~×6 the absolute delta per bank (≈480 kWh/yr per 55 W recovered), improving premium payback to ~6–17 years — better, still not stunning.

**Therefore the product logic:**
1. **Ram-alone (water SKU): tuned build only.** The delivery doubling is the product.
2. **Entry power SKU: a hybrid spec** — steel drive pipe + check-valve snifter (the two cheap, high-leverage tuned elements: ~$700 of the premium buys most of the doubling) with commodity valve internals; full machined-valve tuning reserved for banks and premium units.
3. **The self-tuning module (+$150)** earns its keep not by adding peak efficiency but by *holding* it — the field-drift the literature documents (lab 65–70% vs field-typical 50–60%) is worth more than the last point of bench tuning. It belongs on banks and water-critical installs first.

## Caveats (stated, per canon)

Absolutes at 100 mm scale are conservative and unvalidated (the sim's valve-mass scaling is a heuristic; manufacturer 4" tables run somewhat higher); the T/C *ratio* is robust because both models share the physics and the calibration. Both models still operate at r = 6 where the sim is anchored. Physical bench correlation remains the gate before any of these numbers faces a customer.

**Next:** re-run this comparison at 300 mm and as a 6-ram bank (B-Standard scale) once the drive-pipe length sweep (sim queue #1) lands — the L/D study may shift both models' absolute outputs materially.
