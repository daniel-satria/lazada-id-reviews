# **LAZADA ID REVIEWS**

![workflow status](https://github.com/daniel-satria/lazada-id-reviews/actions/workflows/ci.yaml/badge.svg)
![workflow status](https://github.com/daniel-satria/lazada-id-reviews/actions/workflows/cd-staging.yaml/badge.svg)
![workflow status](https://github.com/daniel-satria/lazada-id-reviews/actions/workflows/cd-push-registry.yaml/badge.svg)
![workflow status](https://github.com/daniel-satria/lazada-id-reviews/actions/workflows/cd-production.yaml/badge.svg)
![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdaniel-satria%2Flazada-id-reviews%2Frefs%2Fheads%2Fmain%2Fpackage.json&query=%24.scikit-learn&logo=scikitlearn&label=scikitlearn&link=https%3A%2F%2Fpypi.org%2Fproject%2Fscikit-learn%2F1.4.1.post1%2F)
![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdaniel-satria%2Flazada-id-reviews%2Frefs%2Fheads%2Fmain%2Fpackage.json&query=%24.mlflow&logo=MLflow&label=MLflow&link=https%3A%2F%2Fpypi.org%2Fproject%2Fmlflow%2F2.9.2%2F)
![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdaniel-satria%2Flazada-id-reviews%2Frefs%2Fheads%2Fmain%2Fpackage.json&query=%24.Flask&logo=Flask&label=Flask&link=https%3A%2F%2Fpypi.org%2Fproject%2FFlask%2F3.0.2%2F)




Steps:
+ Select **Use this template** > **Create a new repository**. This menu is in the top right corner of this repository.
+ Edit `setup.py` and define your project repository.
    + Edit the [README.md](README.md) file's **workflow status** badge with the name of your repository.
    + Renaming `src/MLProject` to your project.
+ Create virtual environment

    ```bash
    virtualenv .venv -p /usr/bin/python3.10
    ```
  **Note:** You can use any Python version, as long the Python packages in `requirements.txt` are supported. Because of the Python packages in `requirements.txt` were declared without describe the version.
+ Activate the virtual environment

    ```bash
    source .venv/bin/activate
    ```

+ Install package.

    ```bash
    pip install -r requirements.txt
    ```

+ enable the environment variables.

    ```bash
    cp .env.example .env
    ```