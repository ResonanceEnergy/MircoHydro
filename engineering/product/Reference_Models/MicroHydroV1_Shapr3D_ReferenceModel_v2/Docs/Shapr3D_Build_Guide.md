# Build Guide — Shapr3D (Reference Model v2)

## Goal
Use **DXF_R12** sketches to build clean, editable Shapr3D bodies (revolve/extrude/pattern), while using **STL_Reference** meshes as visual overlays to confirm shape.

## Import settings
- **Units:** millimeters

## Step-by-step
### A) Import
1. Import **all DXFs** from `DXF_R12/`.
2. (Optional) Import **STLs** from `STL_Reference/` as reference bodies.

### B) Diffuser (hyperbolic-like)
1. Open `Diffuser_Profile_Revolve_HyperbolicLike.dxf` sketch.
2. Select the closed profile and **Revolve 360°** around the AXIS line.
3. Apply **Shell** = 3.0 mm.
4. Compare against `STL_Reference/Diffuser_Reference.stl` (optional overlay).

### C) Nozzle
1. Open `Nozzle_Profile_Revolve.dxf`.
2. Revolve 360° around axis.
3. Shell = 2.5 mm.

### D) Vane packs
For each angle DXF (10/20/30):
1. Extrude the vane rectangle by 18 mm.
2. **Pattern → Circular** about Z axis:
   - Count = 12
   - Angle = 360°
3. (Optional) Create a hub cylinder with diameter 18 and height 18.
4. Compare with `STL_Reference/VanePack_Reference_12x.stl`.

### E) Retainer
1. Open `RetainerCap_Sketch.dxf`.
2. Extrude OD circle to 5 mm.
3. Cut center + bolt circles **through-all**.
4. If you imported `STL_Reference/RetainerCap_HoleTools.stl`, you can also use those cylinders as reference locations.

## Export
- Export editable bodies as **STEP** from Shapr3D (best for downstream CAD/CAM).
