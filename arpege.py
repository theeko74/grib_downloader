

import requests
import time
import sys
import logging as log

log.basicConfig(level=log.DEBUG)

class Arpege:

    def __init__(self):
        self.lat_min = None
        self.lat_max = None
        self.long_min = None
        self.long_max = None
        #self.args = 'wgtprn'
        self.api = "http://195.154.231.142/grib/arpege?" \
            "x={long_min}&X={long_max}&y={lat_min}&Y={lat_max}&r={args}"

    def dwl(self):
        if not self.lat_min and self.lat_max and self.long_min and self.long_max:
            raise ValueError("Lat min/max or long min/max is not defined")


        log.debug("Connect to API: {}".format(self.api))
        print("Connect to API: {}".format(self.api))
        r = requests.get(self.api, stream=True)
        file_name = "GRIB_Arpege_Lion_Corse_{}".format(
            time.strftime("%d%m%Y-%H%M%S")
        )
        log.debug("Write file: {}".format(file_name))
        loading_count = 0
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if loading_count % 100 == 0:
                    sys.stdout.write("*")
                    sys.stdout.flush()
                f.write(chunk)
                loading_count += 1
            print("*")

    def set_zone(self, zone):
        if zone == 'hyeres':
            log.debug("Set zone: Hyères")
            self.lat_min = 45
            self.lat_max = 38
            self.long_min = 1
            self.long_max = 13
            self.api = self.api.format(
                long_min = self.long_min,
                long_max = self.long_max,
                lat_min  = self.lat_min,
                lat_max  = self.lat_max
                args     = self.args
            )
