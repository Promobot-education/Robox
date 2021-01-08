#
# Build: docker build --network="host" -t promobot_edu .
# docker run -it --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" -v /home/student/edu_env:/home/alek/edu_env promobot_edu
#

FROM ubuntu:xenial

LABEL maintainer alek.yum@yandex.ru


# download APT utils
RUN apt update && apt install -y \
    apt-transport-https apt-utils \
    && rm -rf /var/lib/apt/lists/*


RUN apt update && apt install -y ssh ssh-client git sudo setserial udev autoconf nano libceres-dev liblua5.2-dev


RUN git clone --single-branch --branch v3.1.6 https://github.com/stephane/libmodbus.git


RUN cd libmodbus && ./autogen.sh && ./configure && make install && cd /


RUN apt update && apt install --no-install-recommends -y \
    python-pip \
    python3-pip \
    python-serial \
    python-tk \
    python3-tk \
    python3-serial \
    python-matplotlib \
    python3-matplotlib \
    python-setuptools \
    python3-setuptools \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install -U pip --ignore-installed

#RUN pip install git+https://github.com/Promobot-education/Python_modules.git

#RUN pip3 install git+https://github.com/Promobot-education/Python_modules.git


# setup environment
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8


# install software
# Base software & libraries
RUN apt update && apt install -y \
    gcc-5 g++-5 wget tar openssh-client libva-drm1 \
    && rm -rf /var/lib/apt/lists/*

# Cmake
RUN wget https://cmake.org/files/v3.9/cmake-3.9.0-Linux-x86_64.tar.gz \
    && tar -xzvf cmake-3.9.0-Linux-x86_64.tar.gz --strip-components=1 -C /usr/local \
    && rm cmake-3.9.0-Linux-x86_64.tar.gz

RUN apt clean

# setup entrypoint
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

RUN useradd -s /bin/bash -d /home/student/ -G sudo -m student && yes "student" | passwd student

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]