# ShotSense: Real-Time Gunshot Detection System

![System Overview](media/image1.jpg)

## 🎯 Overview
ShotSense is an FPGA-based system that detects gunfire direction using microphone arrays and thermal imaging. Developed for DRDO under Smart India Hackathon 2024, it provides soldiers with instant threat localization in combat scenarios.

## ⚡ Key Features
- **Real-time detection** with <50ms latency
- **8-microphone array** for 360° coverage
- **Thermal camera fusion** for distance estimation
- **VGG19 CNN** for 98% classification accuracy
- **FPGA processing** for battlefield reliability
- **Intuitive LCD display** with threat vector

## 🛠️ Technical Stack
### Hardware
- Xilinx Artix-7 FPGA
- MEMS microphone array
- FLIR Lepton thermal sensor
- 4.3" Tactical LCD display

### Software
- Verilog HDL for signal processing
- Python/TensorFlow for VGG19 model
- Triangulation algorithms (TDOA)
- Custom bandpass filters (3kHz center)

## 📊 Performance Metrics
| Parameter | Specification |
|-----------|--------------|
| Detection Range | 300m (urban), 800m (open) |
| Angular Accuracy | ±2° |
| Response Time | <100ms |
| False Positive Rate | <0.5% |
