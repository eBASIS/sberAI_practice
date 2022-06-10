ARG from

FROM ${from}

LABEL Yaroslav Savelev "y.savelev@edu.misis.ru"

# Timezone Configuration
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt install -y apt-utils \
                                         lsb-release \
                                         mesa-utils \
                                         gnupg2 \
                                         net-tools \
                                         build-essential \
                                         wget \
                                         unzip \
                                         curl \
                                         git \
                                         mc \
                                         vim \
                                         nano \
                                         ffmpeg 


## GUI tunnel from docker
RUN dpkg --add-architecture i386 && \
    apt update && apt install -y --no-install-recommends \
        libxau6 libxau6:i386 \
        libxdmcp6 libxdmcp6:i386 \
        libxcb1 libxcb1:i386 \
        libxext6 libxext6:i386 \
        libx11-6 libx11-6:i386 && \
    rm -rf /var/lib/apt/lists/*

## python deps
RUN apt update && apt install -y python3-pip
RUN python3 -m pip install --upgrade pip
ADD docker/requirements.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements.txt

## apt deps
RUN apt update && apt install -y install \
                                        poppler-utils \
                                        tesseract-ocr \
                                        libtesseract-dev

WORKDIR /workspace