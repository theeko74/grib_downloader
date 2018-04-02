# Author: S.CARLIOZ <sylvain.carlioz@gmail.com>
# License MIT
# 2017

"""
Arome class module.
"""

from .model import MeteoFranceModel


class Arome(MeteoFranceModel):

    def __init__(self):
        super().__init__()
        self.api = "http://195.154.231.142/grib/arome?" \
            "x={long_min}&X={long_max}&y={lat_min}&Y={lat_max}&r={args}"
