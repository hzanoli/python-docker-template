FROM python:3.9 as build

# Creates the python env to 
ENV VIRTUAL_ENV=/pack-env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
 
COPY requirements.txt /requirements/ 
RUN pip install -r /requirements/requirements.txt

COPY . /pack
RUN pip install -e /pack

ENTRYPOINT [ "pack" ]

FROM python:3.9-slim as production
ENV VIRTUAL_ENV=/pack-env
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --from=build /pack /pack
COPY --from=build /pack-env ${VIRTUAL_ENV}

ENTRYPOINT [ "pack" ]