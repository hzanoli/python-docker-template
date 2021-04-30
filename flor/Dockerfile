FROM python:3.9 as build

# Creates the python env to build the package
ENV VIRTUAL_ENV=/flor-env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
 
COPY requirements.txt /requirements/ 
RUN pip install -r /requirements/requirements.txt

COPY . /flor
RUN pip install -e /flor

ENTRYPOINT [ "flor" ]

FROM python:3.9-slim as production
ENV VIRTUAL_ENV=/flor-env
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --from=build /flor /flor
COPY --from=build /flor-env /flor-env

ENTRYPOINT [ "pack" ]