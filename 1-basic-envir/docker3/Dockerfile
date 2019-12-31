FROM python:3.7.5-slim
WORKDIR /usr/src/app
RUN python -m pip install \
        parse \
        realpython-reader
COPY headlines.py .
CMD ["python", "headlines.py"]