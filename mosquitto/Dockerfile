FROM alpine:3.12
RUN apk add --no-cache mosquitto gettext
COPY src/etc/mosquitto /etc/mosquitto
COPY ./docker-entrypoint.sh /
EXPOSE 1883
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/sbin/mosquitto", "-c", "/etc/mosquitto/mosquitto.conf"]
