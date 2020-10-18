#!/usr/bin/env sh
set -eu

/usr/bin/mosquitto_passwd -b /etc/mosquitto/conf.d/passwd ${MQTT_USER} ${MQTT_PASS}

envsubst '${MQTT_USER}' < /etc/mosquitto/conf.d/acl.template > /etc/mosquitto/conf.d/acl

exec "$@"
