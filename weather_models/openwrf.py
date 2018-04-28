# Author: S.CARLIOZ <sylvain.carlioz@gmail.com>
# License MIT
# 2017

"""
OpenWRF class module.
"""

import os
import logging as log
from wx import Yield

import requests
from bs4 import BeautifulSoup

import loadingbar


class OpenWrf:

    def __init__(self, zone):
        self.zone = zone.lower()
        self.url = 'http://openskiron.org/en/openwrf'
        self.endpoint = None

    def get_endpoint(self):
        """
        Search in web page from OpenSkiron the URL to download the correct
        GRIB file based on the indicated zone.
        """
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'html.parser')
        for link in soup.find_all('a'):
            endpoint = link.get('href')
            if endpoint:
                if self.zone in endpoint.lower():
                    return endpoint

    def dwl(self, path=None, loadingBarGUI=None):
        """
        Launch the download of the GRIB file, and save it in current directory
        or in another path, if specified.
        """
        # Get the file name from the web page
        self.endpoint = self.get_endpoint()
        log.debug("Endpoint URL is: {}".format(self.endpoint))

        # Download the GRIB file
        # with loading bar indicator
        # and save it to the correct path

        # Format filename
        if path:
            if path[-1] == '/':
                filename = path
            else:
                filename = path + '/'
        else:
            filename = os.getcwd() + '/'
        filename = filename + 'GRIB_' + self.endpoint.split('/')[-1]
        log.debug("Write file at: {}".format(filename))

        # Connect to endpoint
        log.debug("Connect to API: {}".format(self.endpoint))
        r = requests.get(self.endpoint, stream=True)
        tot_size = r.headers.get('content-length')
        if tot_size:
            # Convert str to int
            tot_size = int(tot_size)
        else:
            # Default file size of 13MB
            tot_size = 13 * 1000000

        # Loading bar
        lb = loadingbar.InternetLoadingBar(tot_size)
        log.debug("Start to download")
        log.debug("Total file size is {}".format(tot_size))
        chunk_len = 0
        with open(filename, 'wb') as grib_file:
            for chunk in r.iter_content(chunk_size=1024):
                lb.update(len(chunk))
                if loadingBarGUI:
                    # Use the GUI loading bar if specified
                    chunk_len += len(chunk)
                    self.loading_gui(chunk_len, tot_size, loadingBarGUI)
                grib_file.write(chunk)
            lb.done()

        print("GRIB downloaded.")
        print(">> {}".format(filename))

    def loading_gui(self, chunk_len, tot_size, loadingBarGUI):
        loadingBarGUI.Update(chunk_len/tot_size*100)
        Yield()
