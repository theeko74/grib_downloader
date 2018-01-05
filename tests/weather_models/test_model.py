# Author: S.CARLIOZ <sylvain.carlioz@gmail.com>
# License MIT
# 2017

"""
Test file for Model abstract model.
"""

from weather_models.model import WeatherModel
from weather_models.arpege import Arpege
from weather_models.arome import Arome


class WeatherModelAbstract:

    def test_set_zone(self):
        self.WEATHER_MODEL.set_zone('hyeres')
        assert (
            self.WEATHER_MODEL.zone == 'hyeres' and
            self.WEATHER_MODEL.lat_min == 45 and
            self.WEATHER_MODEL.lat_max == 38 and
            self.WEATHER_MODEL.long_min == 1 and
            self.WEATHER_MODEL.long_max == 13
        )


class TestArpegeWeatherModel(WeatherModelAbstract):

    @classmethod
    def setup_class(cls):
        cls.WEATHER_MODEL = Arpege()


class TestAromeWeatherModel(WeatherModelAbstract):

    @classmethod
    def setup_class(cls):
        cls.WEATHER_MODEL = Arome()
