

from model import WeatherModel


class Arpege(WeatherModel):

    def __init__(self):
        super().__init__()
        self.api = "http://195.154.231.142/grib/arpege?" \
            "x={long_min}&X={long_max}&y={lat_min}&Y={lat_max}&r={args}"
