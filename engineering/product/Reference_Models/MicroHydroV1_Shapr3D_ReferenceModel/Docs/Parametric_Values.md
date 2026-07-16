# MicroHydroV1 — Shapr3D Reference Model (Parametric Values)

Source of truth: `MicroHydroV1_FULL_Workspace/CAD/Params/params.json` (units: **mm**).

## Diffuser (Revolve + Shell)
- D_in = **32**
- D_out = **82**
- Length = **95**
- Wall (shell) = **3**
- ArcSagitta = **2** (used to bulge mid-radius: r_mid = sqrt(((D_in/2 + D_out/2)/2)^2 + sag^2))

DXF: `DXF/Diffuser_Profile_Revolve.dxf`

## Nozzle (Revolve + Shell)
- D_inlet = **26**
- D_throat = **9**
- L_converge = **38**
- L_straight = **12**
- Wall (shell) = **2.5**

DXF: `DXF/Nozzle_Profile_Revolve.dxf`

## Vane Pack (Extrude + Circular Pattern)
- Outer_Diameter = **88**
- Inner_Hub_D = **18**
- Height (extrude) = **18**
- Vane_Thickness = **2**
- Vane_Count = **12**
- Angles (deg) = **10, 20, 30**

DXFs:
- `DXF/VanePack_Sketch_10deg.dxf`
- `DXF/VanePack_Sketch_20deg.dxf`
- `DXF/VanePack_Sketch_30deg.dxf`

## Retainer Cap (Extrude + Cut)
- OD = **92**
- Thickness (extrude) = **5**
- Bolt_PCD = **84**
- Bolt_Count = **4**
- Center_Hole = **20**
- Bolt hole diameter (reference) = **6.0** (from existing macro implementation)

DXF: `DXF/RetainerCap_Sketch.dxf`
