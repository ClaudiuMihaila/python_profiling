FROM ubuntu:latest

RUN apt-get update \
    && apt-get -y install autoconf automake autotools-dev g++ pkg-config \
    python-dev python-pip python3-dev python3-pip libtool make git

RUN git clone https://github.com/uber/pyflame.git ~/pyflame \
    && cd ~/pyflame && ./autogen.sh && ./configure && make
ENV PATH="/root/pyflame/src:${PATH}"

RUN git clone https://github.com/brendangregg/FlameGraph.git ~/flamegraph
ENV PATH="/root/flamegraph:${PATH}"
