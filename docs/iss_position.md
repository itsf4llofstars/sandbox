# Web Scrape the ISS current Latitude and Longitude

```python3
#!/usr/bin/env python3
import datetime
import os
import re
from urllib.request import urlopen

write_resp = False

with urlopen("http://api.open-notify.org/iss-now.json") as resp:
    response = resp.read()

response = response.decode("utf-8").rstrip()

test_string = '{"message": "success", "timestamp": 1695191518, "iss_position": {"longitude": "29.3387", "latitude": "-51.6141"}}'

iss_lat_lon = re.compile(r"\"iss.*")
iss_deg = re.compile(r"-?\d{,3}\.\d{,4}")

lon_re = re.compile(r"\"longitude\":\s\"-?\d{,3}\.\d{,4}\"")
lat_re = re.compile(r"\"latitude\":\s\"-?\d{,3}\.\d{,4}\"")

lat_coord = ""

if re.search(iss_lat_lon, response):
    lat_lon = re.search(iss_lat_lon, response).group()
    lon = re.search(lon_re, lat_lon).group()
    lat = re.search(lat_re, lat_lon).group()
    lon_coord = re.search(iss_deg, lon).group()
    lat_coord = re.search(iss_deg, lat).group()
    lat_lon_deg = f"{lat_coord}, {lon_coord}"

strf_now = datetime.datetime.now().strftime("%x %X")
lat_lon_deg = strf_now + " " + lat_lon_deg
print(lat_lon_deg)

if write_resp:
    filename = os.path.expanduser(
        os.path.join("~", "python", "datetime_mod", "iss_lat_lon.txt")
    )

    with open(filename, "a", encoding="utf-8") as write:
        write.write(lat_lon_deg)
        write.write("\n")
```
