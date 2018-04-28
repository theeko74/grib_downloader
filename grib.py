#!/usr/bin/env python3

# Author: S.CARLIOZ <sylvain.carlioz@gmail.com>
# License MIT
# 2017

"""
Main file for GRIB downloader script.
"""

__author__ = 'Sylvain Carlioz'
__version__ = '1.0'

import argparse
import sys
import logging

from weather_models.arome import Arome
from weather_models.arpege import Arpege
from weather_models.openwrf import OpenWrf


def call_meteofrance(args):
    """
    Run the download of GRIB files from Meteo France.
    """
    # Create WeatherModel object based on the selected model
    if args.weather_model == 'arpege':
        model = Arpege()
    elif args.weather_model == 'arome':
        model = Arome()
    else:
        raise parser.error(
            "weather_model is invalid. Please select 'arome' or 'arpege' as a" \
            " valid weather model"
        )

    # Action based on arguments passed
    if args.zone:
        # A zone is defined
        alright = model.set_zone(args.zone)
        if alright > 0:
            raise parser.error("Wrong zone. Options are: hyeres")
        model.dwl(path=args.output)
        return sys.exit(0)

    if args.coordinates:
        # Coordinates are defined
        model.dwl(coordinates=args.coordinates.split(','))
        return sys.exit(0)


def call_openwrf(args):
    """
    Run the download of openwrf GRIB files from OpenWRF.
    """
    if not args.zone:
        args.zone = 'france'
    openwrf = OpenWrf(args.zone)
    openwrf.dwl(path=args.output)


def main():
    """
    Main function that runs the script.
    """

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="Select the weather model sources:")

    # Optional arguments
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Switch to verbose mode")
    parser.add_argument('-o', '--output', help="Location to save the GRIB file")

    # MeteoFrance models
    meteofrance = subparsers.add_parser("meteofrance",
                                        help="Select Meteo France models")
    meteofrance.add_argument('weather_model',
                             help="Select a weather model from MeteoFrance." \
                             "Options are: arpege (0.1°/4days), arome" \
                             "(0.025°/2days)")

    # Mutually exclusive optional arguments for choising zone
    zone_arg = meteofrance.add_mutually_exclusive_group(required=True)
    zone_arg.add_argument('-z', '--zone',
                          help="Select a zone to download: hyeres, lion-sardaigne")
    zone_arg.add_argument('-c', '--coordinates',
                          help="Define coordinates of a zone to download" \
                          " Format: x,X,y,Y")
    meteofrance.set_defaults(func=call_meteofrance)

    # OpenWRF model
    openwrf = subparsers.add_parser("openwrf", help="Select OpenWRF model")
    openwrf.add_argument('-z', '--zone',
                         help="Select a zone to download. Options are: france" \
                         "(12km), lion (4km), nice (4km)")
    openwrf.set_defaults(func=call_openwrf)

    # Parse arguments
    args = parser.parse_args()

    # Verbose mode
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    # Run the appropriate function
    try:
        args.func(args)
    except AttributeError:
        parser.error("Wrong or unspecified weather model.")


if __name__ == '__main__':
    main()
