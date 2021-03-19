from invoke import task

pipenv_install = "pipenv install --dev"


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

@task
def build_image(ctx, tags="digdir/fdk-portal-monitoring:latest", staging=False):
    if staging:
        ctx.run(pipenv_install)
    gen_requirements = "pipenv lock -r >requirements.txt"
    ctx.run(gen_requirements)
    tag = ""
    for t in tags.split(","):
        tag = tag + ' -t ' + t

    print("building image with tag " + tag)
    build_cmd = "docker build . " + tag
    ctx.run(build_cmd)