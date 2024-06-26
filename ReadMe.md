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
**Required python version >= 3.11**. It's easy to manage environment with [miniconda](https://docs.anaconda.com/free/miniconda/index.html), [venv](https://docs.python.org/3/library/venv.html) or any other favorite tools.
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
`NC_USERNAME`: **Required**. User name of created bot account.<br/>
`NC_PASSWORD`: **Required**. Either user password or app password of created bot account.<br/>

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

##### Google Gemini
`GOOGLE_API_KEY`: Google project's api key.

##### Azure OpanAI
`AZURE_OPENAI_API_KEY`: OpenAI's api key.
`AZURE_OPENAI_ENDPOINT`: Endpoints of Azure project.
`OPENAI_API_VERSION`: Api version of response.
`AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`: Deployment name of model of Azure project.

##### HuggingFace
`HFACE_TOEKN`: HuggingFace's token.

##### BedRock
Set environment variable as same as using boto3 library. Minimum envs are:<br/>
`AWS_ACCESS_KEY_ID`: Access key.<br/>
`AWS_SECRET_ACCESS_KEY`: Secret Key.<br/>
`AWS_DEFAULT_REGION`: Region of the model.<br/>
Also use !bedrock:set_model_id if not using default Claude 3 Haiku model.


## 🚊 Usage

1. Register a new account for chat bot in Nextcloud
2. Start the agent with new account's credentails
3. Open a new chat and invite chat bot
4. Type `![plugin]:[function] message` to chat, for example `!openai:chat Who are you?`. Any message not start with **!** will be responded with a help message.


## ▶️ Road Map

* Add LLM plugins:
    * OpenAI✅
    * Azure OpenAI✅
    * Google Gemini✅
    * Claude✅(By AWS BedRock)
    * Models on Huggingface✅
    * Anthropic✅
    * Models run on local machine
* Add Tool plugins:
    * Search result from google
    * Weather
* Add memory for conversation✅
