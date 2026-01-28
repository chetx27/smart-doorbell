# Privacy-Preserving AI Doorbell (PPAD)

## Overview
The Privacy-Preserving AI Doorbell (PPAD) is an edge-computing surveillance solution designed to prioritize individual privacy while maintaining residential security. The system utilizes real-time Computer Vision (CV) to detect human presence and automatically anonymizes facial data through localized spatial filtering.

## Key Features
* **Dynamic Face Anonymization:** Real-time application of Gaussian blurring to facial Regions of Interest (ROI) to ensure compliance with privacy standards such as GDPR and CCPA.
* **Spatio-Temporal Tracking:** Implements dwell-time monitoring to differentiate between transient passersby and potential loitering incidents.
* **Visual Telemetry:** Integrated on-screen display (OSD) provides real-time tracking timers and security status indicators.
* **Edge Optimization:** Designed for high-performance execution on standard CPU hardware using the MediaPipe and CVZone backends.

## Technical Stack
* **Language:** Python 3.12
* **Vision Engine:** OpenCV (Open Source Computer Vision Library)
* **ML Framework:** MediaPipe (BlazeFace model)
* **Logic Framework:** CVZone for streamlined object tracking and ROI manipulation

## Mathematical Implementation
The system captures video frames and extracts facial coordinates. To ensure identity protection, a kernel-based Gaussian blur is applied to the extracted ROI using the following distribution:

$$G(x, y) = \frac{1}{2\pi\sigma^2}e^{-\frac{x^2 + y^2}{2\sigma^2}}$$

This methodology ensures that security presence is logged while sensitive biometric identity data remains obfuscated.

## Installation and Deployment

### 1. Repository Initialization
''bash
git clone [https://github.com/chetx27/smart-doorbell.git](https://github.com/chetx27/smart-doorbell.git)
cd smart-doorbell

2. Dependency Installation
Bash
pip install opencv-python cvzone mediapipe

Here is the updated README.md content. I have removed all emojis, standardized the headings, and refined the language to meet professional software engineering documentation standards.

Markdown
# Privacy-Preserving AI Doorbell (PPAD)

## Overview
The Privacy-Preserving AI Doorbell (PPAD) is an edge-computing surveillance solution designed to prioritize individual privacy while maintaining residential security. The system utilizes real-time Computer Vision (CV) to detect human presence and automatically anonymizes facial data through localized spatial filtering.

## Key Features
* **Dynamic Face Anonymization:** Real-time application of Gaussian blurring to facial Regions of Interest (ROI) to ensure compliance with privacy standards such as GDPR and CCPA.
* **Spatio-Temporal Tracking:** Implements dwell-time monitoring to differentiate between transient passersby and potential loitering incidents.
* **Visual Telemetry:** Integrated on-screen display (OSD) provides real-time tracking timers and security status indicators.
* **Edge Optimization:** Designed for high-performance execution on standard CPU hardware using the MediaPipe and CVZone backends.

## Technical Stack
* **Language:** Python 3.12
* **Vision Engine:** OpenCV (Open Source Computer Vision Library)
* **ML Framework:** MediaPipe (BlazeFace model)
* **Logic Framework:** CVZone for streamlined object tracking and ROI manipulation

## Mathematical Implementation
The system captures video frames and extracts facial coordinates. To ensure identity protection, a kernel-based Gaussian blur is applied to the extracted ROI using the following distribution:

$$G(x, y) = \frac{1}{2\pi\sigma^2}e^{-\frac{x^2 + y^2}{2\sigma^2}}$$

This methodology ensures that security presence is logged while sensitive biometric identity data remains obfuscated.
