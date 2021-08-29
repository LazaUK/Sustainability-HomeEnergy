# Sustainability - Measuring energy consumption at home
This is my contribution to the open source project, based on the original idea from my Microsoft colleagues Anurag Peshne and Chris Templeman to measure *energy consumption from home for the work-related activities*.
> **Note:** This solution has been built and tested in Python 3.8.

## Pre-requisites: 
For this tutorial, you would need the following hardware and software components:
- Kasa Smart Wi-Fi Strip or Plug. See the [TP-Link Web site](https://www.tp-link.com/uk/home-networking/smart-plug/hs100) for available models that support *Energy Monitoring*. For testing purposes, I'm using Kasa Mini Smart Plug (**KP115**);
- Computer with the Internet connectivity and pre-installed Python 3.x;
- Azure subscription to provision backend cloud resources.

## Step 0 - Client Setup
1. Download content of this repo;
2. Install python-kasa library, either by using pip command as shown below or manually as described on this [PyPi](https://pypi.org/project/python-kasa/) Web page:
```
pip install python-kasa
```
3. Install Azure IoT Device SDK for Python as described on this [PyPi](https://pypi.org/project/azure-iot-device/) Web page:
```
pip install azure-iot-device
```

## Step 1 - Azure IoT Hub configuration

1. Deploy Azure IoT Hub resource in your Azure subscription;
2. In Azure IoT Hub, add new IoT device corresponding to your SmartPlug using "Add Device" under Explorers -> IoT devices:
![Step1a](/images/Step1a.png)
3. Open newly created IoT device record and copy one of its connection strings (either primary or secondary:
![Step1b](/images/Step1b.png)
4. Open downloaded DemoKasa.py file and update the value of the CONNECTION_STRING variable with the copied connection string from the previous action above:
![Step1c](/images/Step1c.png)

## Step 2 - Azure Stream Analytics configuration

1. Deploy Azure Stream Analytics job resource in your Azure subscription;
2. Add Azure IoT Hub from Step 1 above as a stream input for your Azure Stream Analytics job:
![Step2a](/images/Step2a.png)

