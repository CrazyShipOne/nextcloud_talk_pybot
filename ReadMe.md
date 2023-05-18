# 💬 👲 NC Bot - A Nextcloud Chat Bot

A simple standalone chat bot empowered by LLM services and AI models working with [Nextcloud](https://nextcloud.com) [Talk App](https://nextcloud.com/talk/).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](https://opensource.org/licenses/MIT)
![Python: Version](https://img.shields.io/badge/python-%3E%3D3.10-green)

## 🏃 Quick Start

### 💻 Linux

```bash
git clone https://github.com/CrazyShipOne/nextcloud_talk_pybot.git
cd nextcloud_talk_pybot
cp .env.example .env
pip install -r requirements.txt
./start.sh
```

> **Ensure edit .env by your credentials and tokens.**  refer to [.env / Docker Environment Variable](#envs)

### 🌅 docker
```bash
git clone https://github.com/CrazyShipOne/nextcloud_talk_pybot.git
cd nextcloud_talk_pybot
docker build -t crazyshipone/nextcloud_talk_pybot .
docker run -d \
    -n nextcloud_talk_pybot \
    --restart=always \
    # Add environment variable by -e ENV_NAME=ENV_VALUE
    # -e NC_BASE_URL=https://www.mynextcloud.com:8080
    crazyshipone/nextcloud_talk_pybot
```

> **Ensure add environment variables** refer to [.env / Docker Environment Variable](#envs)

## 📕 Configuration

### <a name="envs"></a> Docker Environment Variable / .env

#### Nextcloud:
`NC_BASE_URL`: **Required**. Base url of nextcloud endpoint. For example **https://www.mynextcloud.com:8080**.<br/>
`NC_USERNAME`: **Required**. User name of created bot.<br/>
`NC_PASSWORD`: **Required**. Password of created bot.<br/>

#### Poll:
`POLL_INTERVAL`: **Optional**. Message polling interval in seconds, **default: 5**.<br/>
`ONLY_NEW`: **Optional**. Set **True** to poll messages send after the bot is started, **False** to poll all unread messages, **default: True**.<br/>
`MAX_MESSAGE`: **Optional**. Maximum unread messages polled from one chat,  **default: 10**<br/>
#### Debug:
`LOG_LEVEL`: **Optional**. Output logging level,  **default: Info**<br/>

#### Chat History:
`MAX_CHAT_HISTORY`: **Optional**. Maximum chat history stored, set 0 to not store. Caution: Set to a large number will cost lots of tokens! **default: 0**<br/>
`HISTORY_STORAGE`: **Optional**. Storage to save chat history, values are below. **default: memory**<br/>
> `memory`: save in memory<br/>
> `redis`: save in redis

`REDIS_HOST`: **Required if `HISTORY_STORAGE` is 'redis'.** Redis host.<br/>
`REDIS_PORT`: **Optional**. Redis port. **default: 6379**<br/>
`REDIS_PASS`: **Optional**. Redis password.<br/>
`REDIS_DB`: **Optional**. Redis db number. **default: 0**<br/>

#### Plugins: 
Set if plugin will be used.

##### OpanAI
`OPENAI_API_KEY`: OpenAI's api key.

##### HuggingFace
`HFACE_TOEKN`: HuggingFace's token.


## 🚊 Usage

1. Register a new account for chat bot in Nextcloud
2. Start the agent with new account's credentails
3. Open a new chat and invite chat bot
4. Type `![plugin]:[function] message` to chat, for example `!openai:chat Who are you?`. Any message not start with **!** will be responded with a help message.


## ▶️ Road Map

* Add LLM plugins:
    * OpenAI (Partly finished)
    * Google Bard
    * Claude
    * Models on Huggingface
    * Models run on local machine
* Add Tool plugins:
    * Search result from google
    * Weather
* Add memory for LLM plugins
