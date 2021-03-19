# fdk-portal-monitoring
fdk-portal-monitoring will monitor fdk-portal (prod) by navigating through all search hits and visit all details pages.

## Developing
### Setup
```
% pyenv local 3.9.0 # python version
% pip install pipenv    # package management tool
% pip install invoke    # a task execution tool & library
% pipenv install --dev  # install packages from Pipfile including dev
```
#### Env variables:
```
CHROME_PATH
FDK_PORTAL_HOST=https://data.norge.no
SKIP_HEADLESS_MODE=1
```

### Running the service locally
```
PyCharm: specify environment variables in "run configurations":
PYTHONUNBUFFERED=1;CHROME_PATH=<PATH_TO_LOCAL_CHROME_DRIVER>;FDK_PORTAL_HOST=https://data.norge.no
```

### Running the service locally in docker
```
% docker-compose up -d

or specify env variable:
% docker-compose run -e FDK_PORTAL_HOST='https://data.norge.no' app
```

###Formatting and linting
Black for formatting and flake8 for linting.

```
% invoke format
```
```
% invoke lint
```
