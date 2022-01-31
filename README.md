# Pipeline

# Idea
We should be able to eaisly switch models used in the main model e.g. in the `GlossTranslationModel`, for instance, by giving a different path to a model

We want to eaisly switch datasets (e.g. just change import) `train.py` and final model should be quite simple. Everything more complicated should be moved to submodels e.g. a transfomer model should not be implemented in the main model. Instead we would prefer to load it `models/transfomers/fake_transfomer`

Submodels should be reusable: key variables should be variables (e.g. `input_size`)

Main model is written in PyTorch Lightning for easier training. But for inference we will load it like a normal PyTorch model.

# Environment setup

To create reproducible environment create virtual environment using venv and requirements defined.
In terminal run:
`make venv`

When you install new library, please add it to the list in `requirements.txt` file so we can avoid dependency conflicts or failed build.

# Example train.py run

`python3 train.py --data /dih4/dih4_2/hearai/data/frames/pjm --gpu 1`


# Style

For style formatting the `black` library is used as default.
If you want to check whether your code matches style requirements, in terminal run:
`make format-check`
If you want to apply changes to your code formatting style, in terminal run:
`make format-apply`

To check code quality with linter, in terminal run:
`make lint`
Currently `pylint` is default linter with access to train.py and models/ (all files are evaluated altogether, if you want to test your specific file, try: `pylint yourfile.py`)

# How to setup logging with neptune.ai
- go to your neptune.ai account and get your API token
- in terminal add your personal token to environmental variables
`export NEPTUNE_API_TOKEN = "<your_token>"`
- go to your neptune.ai account and get your project name
- in terminal add your project name to environmental variables
`NEPTUNE_PROJECT_NAME = "<your_workspace/your_project_name>"`
- if you want to make sure that your credentials are saved properly, you can use `printenv`
- to run training with neptune logger initialized, add `--neptune` flag, i.e. `python3 train.py --neptune`


# Project organization
------------

    ├── LICENSE
    ├── README.md
    |         <- The top-level README for developers using this project.
    ├── data_preprocessing <- scripts for dataset preprocessing, e.g. to convert all datasets to the same format
    │   
    ├── datasets          <- scripts for data loading. One file per dataset
    │
    ├── models            <- scripts for PyTorch models. One file per model
    │
    ├────────── feature_extractors  <- scripts for feature extraction models: e.g. CNN or GCN. Takes a sequence of video frames or coordinates as inputs
    │
    ├────────── transformers        <- scripts for transformers models: e.g. BERT. Takes representation extracted by feature_extractors as input
    │
    ├── notebooks          <- jupyter notebooks.
    │   
    ├── utils              <- source code with useful functions
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`

------------

