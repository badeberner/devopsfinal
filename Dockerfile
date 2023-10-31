FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install Flask
CMD ["python", "app.py"]


RUN apt-get update \
    && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable


RUN apt-get install -yqq unzip \
    && apt-get install -yqq libgconf-2-4


RUN apt-get clean && rm -rf /var/lib/apt/lists/* /var/cache/apt/*