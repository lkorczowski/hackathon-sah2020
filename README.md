# cleandata
Repo created for the Natural Language Processing Backend for the website https://euro-acouphenes.fr/ developed during
 the hackathon Start-at-Home 10-12 April 2020 @Saclay-Start-up.

I will no longer be developed as the project as moved to a new repository
https://github.com/lkorczowski/Tinnitus-NLP

## Installation
The following steps must be performed on a Anaconda prompt console, or 
alternatively, in a Windows command console that has executed the 
`C:\Anaconda3\Scripts\activate.bat` command that initializes the `PATH` so that
the `conda` command is found.

1. Checkout this repository and change to the cloned directory
   for the following steps.

    ```
    $ git clone git@github.com:lkorczowski/cleandata.git
    $ cd cleandata
    ```
    
2. Create a virtual environment with all dependencies.

    ```
    $ conda env create -f environment.yaml
    ```
    
3. Activate the environment and install this package (optionally with the `-e` 
    flag).

    ```
    $ conda activate cleandata-env
    $ pip install -e .
    ```

4. If you have a problem with a missing package, add it to the `environment.yaml`, then:
    ```
    $ conda env update --file environment.yaml
    ```