from invoke import task

#pipenv_install = "pipenv install --dev"


@task
def format(ctx):
    pipenv_run_isort = "pipenv run isort ./src/"
    ctx.run(pipenv_run_isort)
    pipenv_run_black = "pipenv run black ./src/"
    ctx.run(pipenv_run_black)

@task
def lint(ctx):
    pipenv_run_flake8 = "pipenv run flake8 ./src/"
    ctx.run(pipenv_run_flake8)

@task
def safety(ctx):
    gen_requirements = "pipenv lock -r >requirements.txt"
    ctx.run(gen_requirements)
    pipenv_run_safety = "pipenv run safety check --file=./requirements.txt"
    ctx.run(pipenv_run_safety)