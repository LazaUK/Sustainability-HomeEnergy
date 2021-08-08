"""
  Kasa SmartPlug e-meter retrieval, streaming telemetry to the Azure backend
  Author: Laziz Turakulov
  Last update: August 2021
"""

import asyncio
from kasa import Discover
from kasa import SmartPlug

# [LT] - Performing dicovery operation
devices = asyncio.run(Discover.discover())

# <Commented out>
# [LT] - Looping through the key-values pairs, discovered by the Kasa scan 
# for addr, dev in devices.items():
#     asyncio.run(dev.update())
#     print(f"{addr} >> {dev}")

# [LT] - Retrieving IP address and connecting to the first SmartPlug
targetIP = list(devices.keys())[0]
myPlug = SmartPlug(targetIP)
asyncio.run(myPlug.update())

# <Commented out>
# [LT] - Retrieving SmartPlug's hardware details
# print("SmartPlug HW: " + str(myPlug.hw_info))
# print("E-meter available: " + str(myPlug.has_emeter))

# [LT] - This month's stats
print("-----------------------------------------------------------------------------")
print("SmartPlug - this month's stats: " + str(asyncio.run(myPlug.get_emeter_daily())))

# [LT] - This year's stats
print("-----------------------------------------------------------------------------")
print("SmartPlug - this year's stats: " + str(asyncio.run(myPlug.get_emeter_monthly())))

# [LT] - Streaming real-time e-meter telemetry
print("-----------------------------------------------------------------------------")
print("SmartPlug - real-time telemetry: " + str(myPlug.emeter_realtime))
print("-----------------------------------------------------------------------------")