FROM continuumio/miniconda3

RUN mkdir /app

WORKDIR /app

COPY . .

#RUN conda create -n env python=3.6
RUN conda env create -f environment.yaml

RUN echo "source activate cleandata-env" > ~/.bashrc

RUN RUN conda init bash

RUN conda activate cleandata-env
#RUN pip install -e .


RUN conda env update --file environment.yaml
ENV PATH /opt/conda/envs/env/bin:$PATH