# RTD-Module-Design
# 🧪 Single-Channel RTD Input System (Pt100 / Pt1000) – Python Driver

This repository contains the firmware implementation for a single-channel RTD (Resistance Temperature Detector) input module, designed to support both Pt100 and Pt1000 sensors using the MAX31865 RTD-to-digital converter over SPI.

---

## 📌 Overview

This project is part of a hardware/firmware challenge focused on:
- Precision temperature sensing using RTDs.
- Clean SPI communication with MAX31865.
- Scalable design supporting both Pt100 and Pt1000.
- Embedded best practices: low-noise design, high-temperature resilience, and first-principles approach.

---

## Design Highlights

- **Sensor Support**: Supports both Pt100 (100Ω @ 0°C) and Pt1000 (1000Ω @ 0°C) RTDs.
- **SPI Interface**: Communicates with MAX31865 via hardware SPI.
- **Noise Mitigation**: RC filtering, shielded layout, and digital averaging.
- **Self-Heating Control**: One-shot mode sampling to reduce heat from bias current.
- **High Temp Reliability**: All components selected to withstand >101°C.

---

## File Structure

| File             | Description |
|------------------|-------------|
| `rtd_reader.py`   | Python driver to initialize SPI, read raw RTD data, and compute temperature. |
| `README.md`       | This file – project overview and usage. |
| `schematic.png`   | (Optional) Exported schematic of the RTD input module circuit. |

---

## Requirements

- Python 3.x
- Linux SBC (e.g., Raspberry Pi)
- SPI enabled (`sudo raspi-config`)
- Install SPI library:  
  ```bash
  pip install spidev
