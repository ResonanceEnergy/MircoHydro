# Build Guide — Shapr3D (MicroHydroV1 Reference Model)

All dimensions are **mm**.

## 1) Import DXFs
In Shapr3D: **File → Import** → select all DXFs in the `DXF/` folder.

## 2) Diffuser
1. Open `Diffuser_Profile_Revolve.dxf` sketch.
2. Ensure the vertical line on layer `AXIS` is your revolve axis.
3. Select the closed profile region and **Revolve 360°** around the axis.
4. Apply **Shell** with thickness = **3 mm**.

## 3) Nozzle
1. Open `Nozzle_Profile_Revolve.dxf`.
2. Revolve the closed profile 360° around the axis.
3. Shell with thickness = **2.5 mm**.

## 4) Vane Packs
For each angle (10, 20, 30 deg):
1. Open the corresponding `VanePack_Sketch_XXdeg.dxf`.
2. Select the vane rectangle and **Extrude** height = **18 mm**.
3. Use **Pattern → Circular**:
   - Axis: Z through origin
   - Count: **12**
   - Angle: **360°**
4. (Optional) Add a hub cylinder (inner diameter 18 and height 18) if desired.

## 5) Retainer Cap
1. Open `RetainerCap_Sketch.dxf`.
2. Extrude the outer disk to thickness **5 mm**.
3. Cut the center hole and bolt holes through-all.

## 6) Export
When done: **Export → STEP** for each body or as a combined assembly.
