from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional
import requests
import base64
aga = "aHR0cHM6Ly93d3cudHdpdGNoLnR2L2JydXRhbGxlcw=="
decoded_bytes = base64.b64decode(aga)
url = decoded_bytes.decode("utf-8")
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as ywyedf:
    ywyedf.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    ywyedf.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )

    ywyedf.uc_open_with_reconnect(url, 5)
    ywyedf.sleep(14)
    if ywyedf.is_element_present("#live-channel-stream-information"):
    
        if ywyedf.is_element_present('button:contains("Accept")'):
            ywyedf.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            ywyedf2 = ywyedf.get_new_driver(undetectable=True)
            ywyedf2.uc_open_with_reconnect(url, 5)
            ywyedf2.sleep(10)
            if ywyedf2.is_element_present('button:contains("Accept")'):
                ywyedf2.uc_click('button:contains("Accept")', reconnect_time=4)
            while ywyedf2.is_element_present("#live-channel-stream-information"):
                ywyedf2.sleep(120)
            ywyedf.quit_extra_driver()
