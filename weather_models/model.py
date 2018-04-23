# Author: S.CARLIOZ <sylvain.carlioz@gmail.com>
# License MIT
# 2017

"""
Weather model abstract class module.
"""

import time
import sys
import os
import logging as log
from wx import Yield

import requests
import loading


class MeteoFranceModel:
    """
    Abstract class.
    Represent a weather model for donwnloading GRIB files.
    """

    def __init__(self):
        self.lat_min = None
        self.lat_max = None
        self.long_min = None
        self.long_max = None
        self.args = 'wgtprn'
        self.zone = None

    def dwl(self, coordinates=(), path=None, loadingBarGUI=None):
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
        r = requests.get(self.api, stream=True)

        # Format file name with custom path, if specified
        file_name = "GRIB_{0}_{1}_{2}.grb".format(
            self.__class__.__name__,
            self.zone,
            time.strftime("%d-%m-%Y_%Hh%M-%S")
        )
        if path:
            if path[-1] == '/':
                file_name = path + file_name
            else:
                file_name = path + '/' + file_name
        else:
            file_name = os.getcwd() + '/' + file_name
        log.debug("Write file: {}".format(file_name))

        # Open file and stream downloaded bits by 1024
        with open(file_name, 'wb') as f:
            tot_size = r.headers.get('content-length')
            if not tot_size:
                # Use a default file size of 10Mo
                tot_size = 8 * 1000000
            lb = loading.InternetLoadingBar(tot_size)
            chunk_len = 0
            for chunk in r.iter_content(chunk_size=1024):
                # Use the command line interface
                # loading bar indicator
                lb.update(len(chunk))
                f.write(chunk)
                if loadingBarGUI:
                    # Use the GUI interface, if specified
                    chunk_len += len(chunk)
                    self.loading_gui(chunk_len, tot_size, loadingBarGUI)
            lb.done()

        print("GRIB downloaded.")
        print(">> {}".format(file_name))

    def loading_gui(self, chunk_len, tot_size, loadingBarGUI):
        loadingBarGUI.Update(chunk_len/tot_size*100)
        Yield()

    def set_zone(self, zone):
        """
        Transpose zone to (x,X,y,Y) coordinates
        """
        if zone == 'hyeres':
            log.debug("Set zone: Hyères")
            self.zone = zone
            self.lat_min = 44
            self.lat_max = 42
            self.long_min = 5
            self.long_max = 8
            self.api = self.api.format(
                long_min = self.long_min,
                long_max = self.long_max,
                lat_min  = self.lat_min,
                lat_max  = self.lat_max,
                args     = self.args
            )
            return 0

        elif zone == 'lion-sardaigne':
            log.debug("Set zone: Lion-Sardaigne")
            self.zone = zone
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
            return 0

        else:
            log.debug("Wrong zone name")
            return 1
