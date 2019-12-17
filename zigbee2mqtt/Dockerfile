FROM koenkk/zigbee2mqtt:latest
COPY data /app/data
ARG MQTT_USER
ARG MQTT_PASS
RUN sed -i \
    -e "s/MQTT_USER/${MQTT_USER}/" \ 
    -e "s/MQTT_PASS/${MQTT_PASS}/" \ 
    /app/data/configuration.yaml
