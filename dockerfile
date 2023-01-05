FROM ubuntu:focal

LABEL maintainer="Lei Mao <dukeleimao@gmail.com>"

ARG PROTOBUF_VERSION=21.12
ARG PROTOBUF_PYTHON_VERSION=4.21.12
ARG NUM_JOBS=4

ENV DEBIAN_FRONTEND noninteractive

# Install package dependencies
RUN apt update && \
    apt install -y --no-install-recommends \
        build-essential \
        software-properties-common \
        autoconf \
        automake \
        libtool \
        pkg-config \
        ca-certificates \
        wget \
        git \
        curl \
        vim \
        gdb \
        valgrind \
        nano \
        cmake && \
    apt clean

# C++ Runtime
RUN cd / && \
    apt install -y autoconf automake libtool curl make g++ unzip && \
    wget https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOBUF_VERSION}/protobuf-all-${PROTOBUF_VERSION}.tar.gz && \
    tar xvzf protobuf-all-${PROTOBUF_VERSION}.tar.gz && \
    rm -rf protobuf-all-${PROTOBUF_VERSION}.tar.gz && \
    cd protobuf-${PROTOBUF_VERSION} && \
    ./configure && \
    make -j${NUM_JOBS} && \
    make check -j${NUM_JOBS} && \
    make install -j${NUM_JOBS} && \
    ldconfig

# Python Runtime
RUN apt update && \
    apt install -y --no-install-recommends \
        python3 \
        python3-dev \
        python3-pip \
        python3-setuptools && \
    apt clean

RUN cd /usr/local/bin && \
    ln -sf /usr/bin/python3 python && \
    ln -sf /usr/bin/pip3 pip && \
    python3 -m pip install --upgrade pip setuptools wheel

RUN python3 -m pip install tzdata==2022.5

RUN cd /protobuf-${PROTOBUF_VERSION}/python && \
    python setup.py build && \
    python setup.py test && \
    python setup.py install && \
    python -m pip install .

WORKDIR /root
