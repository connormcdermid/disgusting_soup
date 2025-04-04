# syntax=docker/dockerfile:1

FROM python:3
ADD main.py .
ADD Course.py .
ADD Day.py .
ADD mainPage.py .
ADD netcode.py .
ADD README.md .
ADD requirements.txt .
ADD timetable.py .
RUN pip install -r requirements.txt
CMD ["python", "./mainPage.py"]
