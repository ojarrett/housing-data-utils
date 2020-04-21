# Overview
This repository is a collection of utilities and libraries for analyzing US Census housing start data. This
includes libraries and scripts to do the following:

* Syncing data files from the US Census building permit survey FTP site to a local directory
* Combining data files into Python Pandas data frames
* Libraries to do common analysis of housing data, such as ranking cities within a metro area by the number of houses built

# Setup

### Prerequisites
The Python libraries in this repository were tested with Python 3.6 but should work with any version of Python 3. The
prerequisites can be installed by running:

1) `python -m venv venv; source venv/bin/activate` (optional)
2) `pip install -r requirements.txt`

# Usage
### Housing data sync
Running housing_data_sync.py will automatically sync the data from the US Census FTP directory to a local directory, which
generally requires around 500 MB of free space. By default, the data is placed in the data subdirectory of the current working
directory.
`python src/sync/housing_data_sync.py ftp2.census.gov /econ/bps/Place/`
