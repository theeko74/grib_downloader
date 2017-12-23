#!/usr/bin/env python3

# Author: S.CARLIOZ <sylvain.carlioz@gmail.com>
# License MIT
# 2017

"""
Main file for GRIB downloader script.

Author: S.CARLIOZ <sylvain.carlioz@gmail.com>
License: MIT
2017
"""

import argparse
import sys
import logging

from weather_models.arome import Arome
from weather_models.arpege import Arpege


def main():
    """
    Main function that runs the script.
    """

    # Parse command line arguments
    parser = argparse.ArgumentParser()

    # Mandatory argument
    parser.add_argument('weather_model', help="Define a model")

    # Optional arguments
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Switch to verbose mode")

    # Mutually exclusive optional arguments
    zone_arg = parser.add_mutually_exclusive_group(required=True)
    zone_arg.add_argument('-z', '--zone',
                          help="Define a zone to download")
    zone_arg.add_argument('-c', '--coordinates',
                          help="Define coordinates of a zone to download." \
                          " Format: x,X,y,Y")
    args = parser.parse_args()

    # Verbose mode
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

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
        model.dwl()
        return sys.exit(0)

    if args.coordinates:
        # Coordinates are defined
        model.dwl(coordinates=args.coordinates.split(','))
        return sys.exit(0)


if __name__ == '__main__':
    main()
