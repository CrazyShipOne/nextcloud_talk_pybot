# NC Bot - A Nextcloud Chat Bot

A simple standalone chat bot working with [Nextcloud](https://nextcloud.com) [Talk App](https://nextcloud.com/talk/).

## Quick Start

### Linux

```bash
git clone https://github.com/CrazyShipOne/nextcloud_talk_pybot.git
cd nextcloud_talk_pybot
cp .env.example .env
#ensure edit .env by your credentials and tokens
pip install -r requirements.txt
./start.sh
```

### docker
```bash
git clone https://github.com/CrazyShipOne/nextcloud_talk_pybot.git
cd nextcloud_talk_pybot
docker build -t crazyshipone/nextcloud_talk_pybot .
docker run -d \
    -n nextcloud_talk_pybot \
    --restart=always \
    crazyshipone/nextcloud_talk_pybot
```

## Basic Configuration

### .env / Docker Environment 

|Name | Type  | Default | 
| :-- | :-- | :-- |
|1|1|1
