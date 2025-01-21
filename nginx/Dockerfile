FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/

RUN apt update && apt install -y nano
#
#RUN mkdir -p /root/.ssh && \
#    echo "$(cat /run/secrets/ssh-key)" > /root/.ssh/id_rsa && \
#    chmod 0600 /root/.ssh/id_rsa \