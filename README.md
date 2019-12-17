# smarthome

## hardware requirements
- Raspberry Pi 3 B+
- optional: Zigbee USB Stick with CC2531 chip and Koenkk Firmware (https://github.com/Koenkk/Z-Stack-firmware)

## software requirements
- Raspbian (https://www.raspbian.org)

## install

### git on raspberry pi

```
apt-get update
apt-get install -y git
```

### pull this git repo

```
cd /srv
git clone https://github.com/hapu2000/smarthome_public.git
```

### use setup.sh for installing dependencies and setup autostart
```
cd smarthome
./setup.sh
```

### create .env file from .env_example
```
cp .env_example .env
nano .env # or what ever editor of your choise
```

### start docker containers
```
docker-compose up -d
```
