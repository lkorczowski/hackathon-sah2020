# Hackhathon Start-in-Saclay 2020
Repo created for the Natural Language Processing Backend for the website https://euro-acouphenes.fr/ developed during
 the hackathon [Start-at-Home](https://www.start-at-home.fr/) 10-12 April 2020 @Start-in-Saclay.

This repo will no longer be developed as the project as moved to a new repository:
https://github.com/lkorczowski/Tinnitus-NLP

A short (48s) video presents some of the results in the diagnostic prediction of tinnitus patients using NLP LDA model:
[![Alt text](https://img.youtube.com/vi/Ly9OTCAmHKA/0.jpg)](https://www.youtube.com/watch?v=Ly9OTCAmHKA)


`app/app_API_predict.py` provides a flasks app that served as backend for https://euro-acouphenes.fr/ which was
 deployed on an independent server. It used a trained model to predict the diagnostic based on some free
 -text answers of the patients during the questionnaire.

## Installation
The following steps must be performed on a Anaconda prompt console, or 
alternatively, in a Windows command console that has executed the 
`C:\Anaconda3\Scripts\activate.bat` command that initializes the `PATH` so that
the `conda` command is found.

1. Checkout this repository and change to the cloned directory
   for the following steps.

    ```
    $ git clone git@github.com:lkorczowski/hackathon-sah2020.git
    $ cd hackathon-sah2020
    ```
    
2. Create a virtual environment with all dependencies.

    ```
    $ conda env create -f environment.yaml
    ```
    
3. Activate the environment and install this package (optionally with the `-e` 
    flag).

    ```
    $ conda activate sah-env
    $ pip install -e .
    ```

4. If you have a problem with a missing package, add it to the `environment.yaml`, then:
    ```
    $ conda env update --file environment.yaml
    ```