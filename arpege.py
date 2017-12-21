

import requests
import time
import sys
import logging as log


class Arpege:

    def __init__(self):
        self.lat_min = None
        self.lat_max = None
        self.long_min = None
        self.long_max = None
        self.args = 'wgtprn'
        self.api = "http://195.154.231.142/grib/arpege?" \
            "x={long_min}&X={long_max}&y={lat_min}&Y={lat_max}&r={args}"

    def dwl(self, coordinates=(), path=None):
        """
        Method to download the grib file.
        Coordinates (x, X, y, Y) can be specified.
        """
        if not coordinates:
            if not self.lat_min and self.lat_max and self.long_min and self.long_max:
                raise ValueError("Lat min/max or long min/max is not defined")
        else:
            self.lat_min = coordinates[2]
            self.lat_max = coordinates[3]
            self.long_min = coordinates[0]
            self.long_max = coordinates[1]

        # Connect to API with the right URL endpoint
        log.debug("Connect to API: {}".format(self.api))
        print("Connect to API: {}".format(self.api))
        r = requests.get(self.api, stream=True)

        # Format file name with custom path, if specified
        if path:
            file_name = path + file_name
        file_name = "GRIB_Arpege_Lion_Corse_{}".format(
            time.strftime("%d%m%Y-%H%M%S")
        )
        log.debug("Write file: {}".format(file_name))

        # Open file and stream downloaded bits by 1024
        with open(file_name, 'wb') as f:
            loading_count = 0
            for chunk in r.iter_content(chunk_size=1024):
                if loading_count % 100 == 0:
                    sys.stdout.write("*")
                    sys.stdout.flush()
                f.write(chunk)
                loading_count += 1
            print("*")

    def set_zone(self, zone):
        """Transpose zone to (x,X,y,Y) coordinates"""
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
                lat_max  = self.lat_max,
                args     = self.args
            )
