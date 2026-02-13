# 10kW Flagship PMSG Generator Design

## Overview
- **Type:** Permanent Magnet Synchronous Generator (PMSG)
- **Rated Power:** 10 kW continuous, 15 kW peak
- **Speed:** 200 RPM (low-speed direct-drive)
- **Efficiency:** >90% (target 92%)
- **Cooling:** Water-jacketed
- **Voltage:** 3-phase AC, rectified to 48V DC bus

## Key Specifications
- **Torque:** 477 N·m at rated power (scaled from 7kW design)
- **Pole Pairs:** 8 (16 poles total)
- **Slots:** 18 (3 per phase)
- **Magnets:** NdFeB N42, ~20.5 kg total mass (scaled)
- **Winding:** 90 turns per coil, AWG 8 wire
- **Copper Mass:** ~115 kg (scaled)
- **Dimensions:** Rotor diameter ~0.6m, length ~0.35m (estimated)

## Design Equations
- Voltage: \( V_{phase} = N \Phi \omega \)
- Torque: \( T = \frac{3}{2} p \Phi I_q \)
- Efficiency: Copper losses + core losses < 10%

## Scaled Calculations for 10kW
**Torque Requirement:**
$$T = \frac{P}{\omega} = \frac{10000 \, \text{W}}{200 \times 2\pi / 60} = 477 \, \text{N·m}$$

**Electromagnetic Torque:**
$$T = \frac{3}{2} p \Phi I_q$$

**Flux Requirement (assuming same I_q = 15A):**
$$\Phi = \frac{2T}{3 p I_q} = \frac{2 \times 477}{3 \times 8 \times 15} = 2.65 \, \text{Wb}$$

**Magnet Sizing (scaled):**
- Flux per pole: 2.65 / 8 = 0.33 Wb
- Pole area: 0.33 / 0.8 = 0.41 m² per pole
- Dimensions: Arc 0.18m, width 0.09m, thickness 0.012m
- Mass per magnet: ~1.3 kg
- Total mass: 16 × 1.3 = 20.5 kg

**Copper Mass (scaled):**
$$m_{copper} = 81 \times \frac{10}{7} \approx 115 \, \text{kg}$$

## Thermal Modeling
**Heat Generation:**
- Copper losses: 3 × I²R ≈ 800W (at 10kW output)
- Core losses: ~300W
- Total waste heat: ~1.1kW

**Cooling System:**
- Water jacket: Flow rate 5 L/min, ΔT = 10°C
- Heat transfer: Q = mCpΔT = 5 × 4186 × 10 ≈ 209kJ/min (sufficient for 1.1kW)
- Inlet temp: <40°C river water
- Outlet: <50°C

**Sensors:** Thermocouples at stator, magnets; shutdown at 80°C

## Component Sourcing
- **Magnets:** NdFeB N42 from China (e.g., Alibaba) - $25/kg bulk
- **Copper Wire:** AWG 8 enameled from suppliers like MWS Wire
- **Stator Core:** Amorphous metal laminations for low losses
- **Bearings:** Ceramic hybrid for low friction
- **Housing:** Stainless 316L, machined

## Integration with Arduino Controls
- **Sensors:** RPM, voltage, current, temperature
- **Control:** MPPT algorithm for max power point tracking
- **Interface:** I2C/SPI for data logging
- **Safety:** Over-speed protection, emergency stop

## Prototype Testing Plan
1. **Bench Test:** No-load, load testing up to 10kW
2. **Efficiency Measurement:** Dynamometer setup
3. **Thermal Validation:** Heat run at full load
4. **Durability:** 1000-hour run-in
5. **Field Pilot:** Install in microhydro site

## Cost Estimate
- Magnets: $500
- Copper: $1,150
- Core: $800
- Bearings/Housing: $1,000
- Total: ~$4,000 (prototype)