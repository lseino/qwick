# creating dockerfile with python3 official image to run scraper application
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#copy the scraper python script
COPY scraper.py .

CMD [ "python", "./scraper.py" ]