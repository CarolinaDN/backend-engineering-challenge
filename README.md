# Backend Engineering Challenge

Python version: 3.9.8

This project contains the following folders:  
```
├── requirements
├── unbabel_app
│   ├── taks
│   │   ├── dataload.py : first step to load given input.
│   │   ├── cleandata.py : cleans, resamples and aggregates data.
│   │   ├── moving_avg.py : calculations related to moving average.
│   │   ├── output.py : last step to save the data.
│   │   ├── orchestrator: call the functions from the python scripts in the relevant order.
│   ├── tests
│   │   ├── generate_data.py : script used to create more sample data.
│   │   ├── src : tests created for the tasks.
├── Other files were created to have a functional cli project.
```


## How To Run

Clone repo and move to dir **backend-engineering-challenge**.

Create virtual environment, activate it and install requirements: `pip install -r requirements/requirements.txt`

To run the tests use: `python -m unittest unbabel_app`.

To run the app this is the basic command: `python unbabel_cli.py --input_file events.json`.

```
python unbabel_cli.py --help
usage: unbabel_cli.py [-h] --input_file INPUT_FILE [--window_size WINDOW_SIZE] [--nr_words NR_WORDS]

optional arguments:
  -h, --help            show this help message and exit
  --input_file INPUT_FILE
                        Path to input file
  --window_size WINDOW_SIZE, -ws WINDOW_SIZE
                        Window size in minutes. Defaults to 10
  --nr_words NR_WORDS   If True it will return the moving average of words with window size defined. Defaults to False 
```

## First Steps
- Inital checks on data: 
  - There seems to be some correlation between nb of words and duration.
  - Easier to work with a pandas dataframe than a json file.
- Define project layout.
- Create virtual environment.
- Setup requirements with pip-compile (pip==21.3.1 and pip-tools==6.4.0) and install them.
- Checks that will be necessary: input file and window size.
- Setup project.
- Add on: moving average of number of words using given window size.


## Difficulties:
- Resample not obtaining the correct closed values.
  - Tested with label="left" and closed="right"
  - Tried different pandas versions
  - Tested xarray
  - Implemented a fix that check the first timestamp and the resample

## Considerations for next steps:
- More checks
- Add more things to .gitignore (.json files)
- Could have more docstrings
- Add logs
- Are there filters and other checks on data that should be considered according to the business? For example: client_name, source_language, target_language, or event_name. Should be discussed with people more familiar with the data and use cases of the application.
- More tests for each function and integration test
