#
# @dockerfile Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

FROM python:3.8-alpine3.16

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /
COPY AT19_CONVERTER/. /

RUN apk add gcc libc-dev libffi-dev
RUN pip install cryptography
RUN pip install -r requirements.txt
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev \
    libressl-dev libffi-dev
RUN apk add exiftool
RUN apk add ffmpeg
RUN apk --update add imagemagick
RUN apk update && apk add tesseract-ocr=3.04.01-r1 --repository=http://dl-cdn.alpinelinux.org/alpine/v3.6/community

EXPOSE 5000
CMD ["python3", "CONVERTER/src/com/jalasoft/converter/main.py", "ffmpeg", "libmagickwand", "tesseract"]
