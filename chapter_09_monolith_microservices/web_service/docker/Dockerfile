FROM ubuntu AS runtime-image


# Install Python, uwsgi and nginx
RUN apt-get update && apt-get install -y python3 nginx uwsgi uwsgi-plugin-python3 
RUN apt-get install -y python3-pip

# Add starting script and config
RUN mkdir -p /opt/server
ADD ./docker/uwsgi.ini /opt/server
ADD ./docker/nginx.conf /etc/nginx/conf.d/default.conf
ADD ./docker/start_server.sh /opt/server
RUN chmod +x /opt/server/start_server.sh

# Add and install requirements
ADD requirements.txt /opt/server
RUN pip3 install -r /opt/server/requirements.txt

# Add the source code
RUN mkdir -p /opt/code
ADD ./src/ /opt/code

WORKDIR /opt/code

# compile the static files
RUN python3 manage.py collectstatic --noinput

EXPOSE 8000
CMD ["/bin/bash", "/opt/server/start_server.sh"]
