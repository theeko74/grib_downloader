GRIB DOWNLOADER
===============

Command line script to download grib files from Meteo France's servers.
Two models are available:
    * Arpege  0.1°      7,5km   4 days
    * Arome   0.025°    1,3mk   2 days


INSTALLATION
------------

* The script runs under python3, so make sure it is installed.
* Install dependencies:
```
$ pip3 install -r requirements.txt
```


GETTING STARTED
---------------

1. First, you need to choose a model between arpege or arome;
2. Then, you need to define a zone to download.

Examples:
```
$ ./grib.py arome -z hyeres
```

```
$ ./grib.py arome -c -2,1,42,45
```


OPTIONS
-------

* `-v` or `--verbose` activates verbose mode.
* `-z` or `--zone` defines a zone to download.
* `-c` or `--coordinates` defines by coordinates long_min, long_max, lat_min, lat_max a zone to download.
* `-h` or `--help` displays help.
