FROM alpine:latest
RUN apk add mosquitto
COPY src/etc/mosquitto /etc/mosquitto
ARG MQTT_USER
ARG MQTT_PASS
RUN /usr/bin/mosquitto_passwd -b /etc/mosquitto/conf.d/passwd ${MQTT_USER} ${MQTT_PASS}
RUN sed -i -e "s/MQTT_USER/${MQTT_USER}/" /etc/mosquitto/conf.d/acl
CMD /usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf
EXPOSE 1883
