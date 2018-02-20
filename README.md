Grib Downloader
===============

Command line script to download grib files from different sources on the web.

Two models are available:

* Arpege (from [Meteo France](http://www.meteofrance.com/)):
    * Definition: 0.1° (7,5km/6NM)
    * Validity: 4 days

* Arome (from [Meteo France](http://www.meteofrance.com/))
    * Definition: 0.025° (1,3km/1,5NM)
    * Validity: 2 days

* OpenWRF (from [OpenSkiron](http://openskiron.org/en/))
    * France zone:
        * Definition: 12km
        * Validity: 5 days
    * Lion, Nice zones:
        * Definition: 4km
        * Validity: 2 days


Installation
------------

* The script runs under python3, so make sure it is installed.
* Install dependencies:
```
$ pip3 install -r requirements.txt
```

Note: loading lib can be found at https://github.com/theeko74/loading


Getting Started
---------------

1. First, you need to choose a model between arpege or arome;
2. Then, you need to define a zone to download.

Examples:
```
$ ./grib.py meteofrance arome -z hyeres
```

```
$ ./grib.py meteofrance arome -c -2,1,42,45
```

```
$ ./grib.py openwrf -z france
```


Options
-------

* `-v` or `--verbose` activates verbose mode.
* `-z` or `--zone` defines a zone to download.
* `-c` or `--coordinates` defines by coordinates long_min, long_max, lat_min, lat_max a zone to download.
* `-h` or `--help` displays help.
