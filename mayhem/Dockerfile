# Build Stage
FROM fuzzers/atheris:2.0.7-python3.9

ADD . /src
WORKDIR /src
RUN python3 -m pip install . && \
	python3 -c "import nltk; nltk.download('punkt')" && \
	pip cache purge
RUN python3 -m pip install numpy

CMD ["/src/mayhem/fuzz_lang.py"]
