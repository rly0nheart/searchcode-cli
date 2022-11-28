# searchcode-cli

![searchcode-cli_banner](https://user-images.githubusercontent.com/74001397/203441377-ad53a2ab-16d6-42b3-bbec-542c9ed43534.png)

[![Upload Python Package](https://github.com/rly0nheart/searchcode-cli/actions/workflows/python-publish.yml/badge.svg)](https://github.com/rly0nheart/searchcode-cli/actions/workflows/python-publish.yml) [![CodeQL](https://github.com/rly0nheart/searchcode-cli/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/searchcode-cli/actions/workflows/codeql.yml)

Command line client for Searchcode.com

# Installation
## PyPI
searchcode-cli can be installed from pypi using the command:
```
pip install searchcode-cli
```
## Docker
Alternatively, you can pull the docker container from dockerhub by running the command:
```
docker pull rly0nheart/searchcode-cli
```
## Build From Source
Or if you wish to build searchcode-cli from source, you can follow these steps:

**1. Clone the repository**
```
git clone https://github.com/rly0nheart/searchcode-cli
```
**2. Move to searchcode-cli directory**
```
cd searchcode-cli
```
**3. Build the .whl file**
Before you start building the .whl, you should first install the build package (if you dont already have it)
```
pip install build
```
Once the build package is installed, you can now run the following command to start building:
```
python -m build
```
**4. Installing .whl**
When building is complete, you will now run the following command to install the built .whl
```
pip install dist/*.whl
```
This will look for a file with the .whl extension and install it

### Note
> On Windows, you will have to explicitly write the full filename of the .whl after dist\ 
# Usage
## PyPI Package
To get started with searchcode-cli, you can use the -h/--help flag, this will return the help message and basic usage
```
searchcode --help
```
## Docker Container
```
docker run -it rly0nheart/searchcode-cli --help
```

# About SearchCode
Read more about searchcode [here](https://searchcode.com/about/)

# Donations
If you would like to donate, you could Buy Me A Coffee using the button below

<a href="https://www.buymeacoffee.com/189381184" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Your support will be much appreciated!😊
