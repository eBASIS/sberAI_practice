# Papers-Parse

## Table of content
-  [General description](#general-description)
-  [Structure](#struct)
-  [Acknoledgement](#ackn)
-  [Closing remarks](#contact)

## General description <a name="general-description"></a>
A set of scripts for downloading articles from SciHub, marking up articles and extracting the necessary sections: affiliations, acknoldgements

The package was tested for the Ubuntu 20.04 LTS.

## Structure <a name="struct"></a>
- [**docker**](docker) – docker launch scripts and python env requirements
- [**data**](data) – directory for dataset
- [grobid_requests.py](grobid_requests.py) – wrapper over **Grobid** API
- [recognize.py](recognize.py) – example of using Tesseract
- [sciHub_download.py](sciHub_download.py) – extended [library](https://github.com/zaytoun/scihub.py/blob/master/scihub/scihub.py) for parsing affiliations and acnoledgements
- [sciHub_parse.py](sciHub_parse.py) – main script for iterating over dataset, loading articles and marking them 
## Acknoledgement <a name="ackn"></a>
A Python parser for scientific PDF based on GROBID.  
Grobid API wrapper based on *@titipata*'s [scipdf parser](https://github.com/titipata/scipdf_parser).  
SciHub parser based on *@allenai*'s [science parse](https://github.com/allenai/science-parse).
## Contact info <a name="contact"></a>
- Maintainer: [Yaroslav](github.com/atokagzx)
- Maintainer: [Tamara](github.com/Toma-Sin)
