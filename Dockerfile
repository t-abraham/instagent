FROM python:3.9-slim

LABEL DEVELOPERS="Tahasanul Ibrahim"

RUN apt-get update && apt-get upgrade -y
RUN apt-get install procps tzdata sudo nano bash locales -y && locale-gen "en_US.UTF-8"

#Python
COPY /gitclone/app/requirements.txt /home/app/requirements.txt
RUN pip3 install -r /home/app/requirements.txt

ENV \
# Email settings enviornments
	LANG=en_US.UTF-8 \
	LANGUAGE=en_US.UTF-8 \
	LC_ALL=en_US.UTF-8 \
	
# Email settings enviornments
	MAIL_USERNAME=REPLACE_MAIL_USERNAME \
	MAIL_PASSWORD=REPLACE_MAIL_PASSWORD \
	MAIL_SERVER=REPLACE_MAIL_SERVER \
	MAIL_PORT=REPLACE_MAIL_PORT \

# MySQL settings enviornments
	MYSQL_DATABASE_HOST=REPLACE_MYSQL_DATABASE_HOST \
	MYSQL_DATABASE_USER=REPLACE_MYSQL_DATABASE_USER \
	MYSQL_DATABASE_PASS=REPLACE_MYSQL_DATABASE_PASS \
	MYSQL_DATABASE_NAME=REPLACE_MYSQL_DATABASE_NAME \

# MQTT settings enviornments
	MQTT_BROKER_HOST=REPLACE_MQTT_BROKER_HOST

# Copy GitLab repository 
COPY /gitclone/app /home/app
RUN ls /home/app
	
#Setting Up Services
RUN chmod +x /home/app/entry.sh
ENTRYPOINT ["/home/app/entry.sh"]
