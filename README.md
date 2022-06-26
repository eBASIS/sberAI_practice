# Papers-Parse

This document is dedicated to the desctiption and purpose of the **Paper Parse** tool that is dedicated to the SciHub papers parsing, transofrming and analyzing of those with respect to the affilations and acknowledgement. 

## Table of content
- [General description](#general-description)
- [Proposed Solution](#proposed-solution)
- [Structure](#structure)
- [Acknowledgement](#acknowledgement)
- [Closing remarks](#contact-info)

## General description

First of all, we should say that there is a huge number of people that are writting the acrticles. But there's a huge problem of **TBD**

And all of these works are holded in Scihubm which is **TBD**

That's why we have realize that the people are needing the tool to find and prepare the data with the potential to its deeper analysis using ML tools and even visualization.

## Proposed solution

We were trying to design various approaches to resolve our problem. But we've found that the best way to di it would be to build a **set of scripts** that are written in Python and can do multiple tasks:

- for downloading articles from SciHub
- marking up articles and reoragnization of the outline structure (data preparation)
- extracting the necessary sections: affiliations, acknowldgements

All of these scripts are wrapped into the Unix package. We have passed the tests for the Ubuntu 20.04 LTS.

## Structure

The code in this repo consists of multipe directories, that's why you need to know alll about it:
- [**docker**](docker) – docker launch scripts and python env requirements
- [**data**](data) – directory for dataset
- [**grobid_requests.py**](grobid_requests.py) – wrapper over **Grobid** API
- [**recognize.py**](recognize.py) – example of using Tesseract
- [**sciHub_download.py**](sciHub_download.py) – extended [library](https://github.com/zaytoun/scihub.py/blob/master/scihub/scihub.py) for parsing affiliations and acnowledgements
- [**sciHub_parse.py**](sciHub_parse.py) – main script for iterating over dataset, loading articles and marking them 

## Acknowledgement
A Python parser for scientific PDF based on GROBID  
Grobid API wrapper based on *@titipata*'s [scipdf parser](https://github.com/titipata/scipdf_parser)  


SciHub parser based on *@allenai*'s [science parse](https://github.com/allenai/science-parse)

## Contact info
- Maintainer: [Yaroslav](github.com/atokagzx)
- Maintainer: [Tamara](github.com/Toma-Sin)
