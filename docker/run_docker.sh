#!/bin/bash

xhost +local:docker || true

ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

echo "[!] your /workspace directory symlinked to: $ROOT_DIR" 
if [[ $1 = "--mac" ]] || [[ $1 = "-m" ]]
  then
  docker run  -ti --rm \
            -e DISPLAY=host.docker.internal:0 \
            -v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
            -e XAUTHORITY \
            -v /dev:/dev \
            -v $ROOT_DIR/:/workspace \
            --net=host \
            --privileged \
            --name ocr ocr-img
else
    docker run  -ti --rm \
                -e "DISPLAY" \
                -e "QT_X11_NO_MITSHM=1" \
                -v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
                -e XAUTHORITY \
                -v /dev:/dev \
                -v $ROOT_DIR/:/workspace \
                --net=host \
                --privileged \
                --name ocr ocr-img
fi