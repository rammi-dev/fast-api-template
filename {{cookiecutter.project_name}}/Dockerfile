# Select one of the base image https://gitlab.com/danisco-nutrition-and-biosciences/lighthouse/automation/images/python-base-images
FROM registry.gitlab.com/danisco-nutrition-and-biosciences/lighthouse/automation/images/python-base-images/python-3.11/mssql:v0.0.1
RUN pip config set global.extra-index-url https://gitlab.com/api/v4/groups/13299895/-/packages/pypi/simple
RUN pip config set global.trusted-host gitlab.com

# fix encoding issues
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# select TZ for the docker image
ENV TZ=Europe/Copenhagen
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# copy application files to image
WORKDIR /{{cookiecutter.project_name}}

COPY . /{{cookiecutter.project_name}}/

# For local development  docker build --secret id=netrc,src=<path to you secrets>.netrc -t monitor_test .
# .netrc is standard secret file in linux. There is similar solution for windows
# Reference: https://gitlab.com/gitlab-org/gitlab/-/issues/350582

# making stdout unbuffered (any non empty string works)
ENV PYTHONUNBUFFERED="non_empty_string"

RUN --mount=type=secret,id=netrc,dst=/kaniko/.netrc echo Install dependencies\
     && mkdir -p /root/ \
     && ln -s /kaniko/.netrc /root/.netrc 2>/dev/null || : \
     && python -m pip install --upgrade pip \
     && pip install -r requirements.txt \
     && pip install .
