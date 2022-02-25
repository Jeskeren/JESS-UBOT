# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# JES-USERBOT
# GLEDEK-USERBOT
#
#YA UDH IYA PEPEK

RUN git clone -b JESS-UBOT https://github.com/Jeskeren/JESS-UBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Jeskeren/JESS-UBOT/JESS-UBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
