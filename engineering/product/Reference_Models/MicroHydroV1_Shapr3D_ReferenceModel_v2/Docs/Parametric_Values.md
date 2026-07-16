# MicroHydroV1 — Shapr3D Reference Model v2 (Both DXF + 3D Reference)

This kit is generated from your source parameters file:
- `MicroHydroV1_FULL_Workspace/CAD/Params/params.json` (units: **mm**)

## What’s included
1) **DXF_R12/** — Shapr3D-safe DXFs (R12/AC1009, classic entities).
2) **STL_Reference/** — non-parametric visual reference meshes (fast import).

## Parameters (mm)
### Diffuser
- D_in = 32
- D_out = 82
- Length = 95
- Wall = 3.0
- ArcSagitta = 2

**Profile type:** hyperbolic-like cubic curve constrained by end diameters + midpoint bulge (rmid = (r1+r2)/2 + ArcSagitta).

### Nozzle
- D_inlet = 26
- D_throat = 9
- L_converge = 38
- L_straight = 12
- Wall = 2.5

### Vane pack
- OD = 88
- ID = 18
- Height = 18
- Thickness = 2
- Vane_Count = 12
- Angles = [10, 20, 30]

### Retainer
- OD = 92
- Thickness = 5
- Bolt_PCD = 84
- Bolt_Count = 4
- Center_Hole = 20
- Bolt Hole D (reference) = 6.0
