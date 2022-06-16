#!/bin/bash
ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

docker run  -ti --rm \
            -e XAUTHORITY \
            -v /dev:/dev \
            -p 8070:8070 \
            -p 8071:8071 \
            --privileged \
            --name grobid grobid-img