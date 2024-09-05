# **LAZADA ID REVIEWS**

![workflow status](https://github.com/daniel-satria/lazada-id-reviews/actions/workflows/main.yml/badge.svg)

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