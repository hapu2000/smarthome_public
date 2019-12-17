apt-get update
apt-get install -y python3-pip python3-dev apt-transport-https ca-certificates software-properties-common

curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh

pip3 install docker-compose

# /etc/systemd/system/docker-compose-smarthome.service

cat <<'EOF' >> /etc/systemd/system/docker-compose-smarthome.service
[Unit]
Description=Docker Compose Application Home Assistant
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/srv/smarthome
ExecStart=/usr/local/bin/docker-compose up -d
ExecStop=/usr/local/bin/docker-compose down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
EOF

systemctl enable docker-compose-smarthome
