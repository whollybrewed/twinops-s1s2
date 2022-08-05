FROM python:3.9

LABEL maintainer="a.lee@student.tue.nl"

RUN python -m pip install --upgrade pip
RUN pip3 install OMSimulator --upgrade

COPY initiate_models.py /orchestration
COPY s1.ssp /orchestration

WORKDIR /orchestration  

EXPOSE 9092

ENTRYPOINT ["python"] 

CMD ["initiate_models.py"]
