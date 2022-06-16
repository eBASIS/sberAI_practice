FROM ubuntu:20.04

LABEL Yaroslav Savelev "y.savelev@edu.misis.ru"

# Timezone Configuration
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt install -y apt-utils \
                                         lsb-release \
                                         gnupg2 \
                                         net-tools \
                                         build-essential \
                                         wget \
                                         unzip \
                                         curl \
                                         git \
                                         nano 

## install GROBID
RUN apt update && apt install -y default-jre
WORKDIR /grobid-install
RUN wget https://github.com/kermitt2/grobid/archive/0.7.1.zip && unzip "0.7.1.zip"
WORKDIR /grobid-install/grobid-0.7.1
RUN ./gradlew clean install
#ENTRYPOINT ./gradlew run --stacktrace