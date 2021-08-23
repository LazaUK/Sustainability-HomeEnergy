# Sustainability - Measuring energy consumption at home
This is my contribution to the open source project, based on the original idea from my Microsoft colleagues Anurag Peshne and Chris Templeman to measure *energy consumption from home for the work-related activities*.
> **Note:** This solution was built and tested with Python 3.8.

## Pre-requisites: 
For this tutorial, you would need the following hardware and software components:
- Kasa Smart Wi-Fi Strip or Plug. See the [TP-Link Web site](https://www.tp-link.com/uk/home-networking/smart-plug/hs100) for available models that support *Energy Monitoring*. For testing purposes, I'm using Kasa Mini Smart Plug (**KP115**);
- Computer with the Internet connectivity and pre-installed Python 3.x;
- Azure subscription to provision backend cloud resources.

## Step 0 - Setup
1. Download content of this repo;
2. Install python-kasa library, either by using pip command as shown below or manually as described on [PyPi](https://pypi.org/project/python-kasa/) Web page:
```
pip install python-kasa
```
3. Install Azure IoT Device SDK for Python as described on [PyPi](https://pypi.org/project/azure-iot-device/) Web page:
```
pip install azure-iot-device
```


<TBC>
