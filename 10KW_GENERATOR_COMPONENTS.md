# 10kW Generator Component Breakdown

**Date:** February 13, 2026  
**Design:** PMSG Direct-Drive, 10kW @ 200 RPM  
**Status:** Detailed Specification Ready  

---

## 🔧 COMPONENT SPECIFICATIONS

### **1. Rotor Assembly**
**Function:** Houses permanent magnets, rotates with turbine shaft  
**Specifications:**
- **Diameter:** 0.6m
- **Length:** 0.35m
- **Material:** Mild steel hub with magnet retention rings
- **Magnets:** 16 × NdFeB N42 blocks (20.5kg total)
  - Dimensions: 180mm arc × 90mm width × 12mm thick
  - Magnetization: Radial, N42 grade
  - Retention: Epoxy bonded + stainless steel bands
- **Balance:** Dynamic balance to ISO 1940 G1.0
- **Weight:** ~35kg total

**Sourcing:** Custom from magnet suppliers (e.g., China NdFeB manufacturers)  
**Cost:** $500 (magnets) + $200 (assembly) = $700

---

### **2. Stator Assembly**
**Function:** Generates AC voltage through electromagnetic induction  
**Specifications:**
- **Slots:** 18 (3 per phase)
- **Windings:** 90 turns per coil, AWG 8 copper wire
- **Core:** Amorphous metal laminations (0.2mm thick)
  - Stack length: 0.3m
  - Inner diameter: 0.62m
  - Outer diameter: 0.8m
- **Insulation:** Class H (180°C) with vacuum impregnation
- **Phases:** 3-phase, star-connected
- **Weight:** ~45kg (copper 25kg + core 20kg)

**Sourcing:** Custom wound by motor manufacturers  
**Cost:** $1,500 (windings) + $800 (core) = $2,300

---

### **3. Bearings**
**Function:** Support rotor, minimize friction  
**Specifications:**
- **Type:** Hybrid ceramic ball bearings
- **Size:** 6312 (60mm bore × 130mm OD × 31mm width)
- **Quantity:** 2 (one at each end)
- **Load Rating:** C3 clearance, 60kN dynamic
- **Lubrication:** Grease-packed, sealed
- **Expected Life:** 50,000 hours at rated load

**Sourcing:** SKF or equivalent  
**Cost:** $200/pair

---

### **4. Shaft**
**Function:** Transmits torque from turbine to rotor  
**Specifications:**
- **Material:** 316L stainless steel
- **Diameter:** 60mm
- **Length:** 0.8m (including coupling)
- **Keyway:** 18mm × 5mm (DIN 6885)
- **Surface Finish:** Ra 0.8μm
- **Torsional Stiffness:** >10,000 N·m/rad

**Sourcing:** Machined from bar stock  
**Cost:** $150

---

### **5. Housing & Cooling System**
**Function:** Contains assembly, provides cooling  
**Specifications:**
- **Material:** Cast aluminum or stainless steel
- **Dimensions:** 1.0m diameter × 0.5m length
- **Cooling:** Water jacket (5L capacity)
  - Flow rate: 5 L/min
  - Inlet temp: <40°C
  - Pressure drop: <0.5 bar
- **Seals:** Viton O-rings, IP65 rated
- **Mounting:** 4 × M16 bolts, vibration-isolated

**Sourcing:** Cast or machined  
**Cost:** $600 (housing) + $200 (cooling) = $800

---

### **6. Electrical Connections**
**Function:** Power output and control signals  
**Specifications:**
- **Power Cables:** 3 × 10mm² copper, 5m length
- **Connector:** IP68 rated junction box
- **Sensors:** 
  - Temperature: 3 × PT100 (stator, bearings, magnets)
  - Speed: Hall effect sensor
  - Vibration: Accelerometer
- **Grounding:** Dedicated earth terminal

**Sourcing:** Standard electrical components  
**Cost:** $150

---

## 📊 ASSEMBLY SEQUENCE

1. **Stator Installation:** Mount stator in housing, secure with dowels
2. **Rotor Assembly:** Attach magnets to rotor hub, balance
3. **Bearing Installation:** Press bearings into end bells
4. **Shaft Insertion:** Install rotor on shaft, align with stator
5. **Housing Closure:** Seal housing, install cooling system
6. **Electrical:** Connect windings, install sensors
7. **Testing:** No-load rotation, insulation resistance check

## 🧪 QUALITY CONTROL

- **Dimensional:** ±0.1mm tolerance
- **Electrical:** Insulation resistance >100MΩ
- **Magnetic:** Flux density measurement
- **Balance:** <1g·mm residual unbalance
- **Thermal:** Heat run test at 120% load

## 💰 TOTAL COST BREAKDOWN

| Component | Cost |
|-----------|------|
| Rotor | $700 |
| Stator | $2,300 |
| Bearings | $200 |
| Shaft | $150 |
| Housing/Cooling | $800 |
| Electrical | $150 |
| **Total** | **$4,300** |

**Note:** Prototype costs; volume production ~$2,500/unit