FROM python:3

ADD src /src

CMD [ "python", "-m", "unittest", "discover", "-s", "Tests"]

