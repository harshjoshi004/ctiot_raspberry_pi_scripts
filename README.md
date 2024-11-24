# BLE Advertising Scripts for Personalized Shop Advertisements

## Overview

This repository contains Python scripts designed to implement **Bluetooth Low Energy (BLE) advertising** for specific shops. The scripts enable Raspberry Pi devices to broadcast advertisements to nearby BLE-compatible devices, making use of the **Bluetooth stack**. These advertisements are tailored to promote specific businesses, leveraging BLE for proximity-based marketing.

## Scripts

### 1. `babajuice.py`

- **Purpose**: Broadcasts BLE advertisements for the "Baba Juice Shop."
- **Advertising Data**:
  - Includes the shop's name (`baba`) encoded as a **Complete Local Name**.
  - Uses Eddystone UUID for compatibility.
- **Advertising Interval**: Configured to a 30ms interval for frequent broadcasts.
- **Key Features**:
  - Promotes a juice and snacks shop.
  - Supports quick detection by BLE devices within range.

### 2. `laundry.py`

- **Purpose**: Broadcasts BLE advertisements for "Campus Laundry."
- **Advertising Data**:
  - Includes the shop's name (`laundry`) encoded as a **Complete Local Name**.
  - Uses Eddystone UUID for compatibility.
- **Advertising Interval**: Configured to a 30ms interval for consistent visibility.
- **Key Features**:
  - Highlights a premium laundry service.
  - Targets users seeking eco-friendly and quick turnaround services.

## How It Works

1. **Initialize BLE Adapter**:
   - Disables and re-enables the Bluetooth adapter to ensure a clean state.
   - Configures advertising parameters, including interval, type, and channel map.

2. **Set Advertising Data**:
   - Encodes the shop name into the advertising packet.
   - Includes relevant flags and UUID for device compatibility.

3. **Start Advertising**:
   - Enables BLE advertising with the configured data.
   - Keeps the advertising process running in a loop.

4. **User Interaction**:
   - Users within BLE range can scan using apps like **nRF Connect** to detect and view the shop's advertisement.

5. **Error Handling**:
   - Handles exceptions, such as failed commands or user interruptions, to ensure graceful termination or recovery.

## Running the Scripts

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
