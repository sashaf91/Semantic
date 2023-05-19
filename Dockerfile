FROM pypy:latest
WORKDIR /app
COPY . /app
RUN pip install spacy
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download en_core_web_md
CMD python semantics.py