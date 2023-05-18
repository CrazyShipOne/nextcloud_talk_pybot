import ncbot.command.base as base
import requests
import ncbot.config as ncconfig

plugin_name = 'hface'

API_URL = "https://api-inference.huggingface.co/models/"
headers = {"Authorization": f"Bearer {ncconfig.cf.hf_token}"}


@base.command(plname=plugin_name, funcname='t0',desc="Chat with bigscience's T0 model")
def llama(userid, username, input):
    model_name = 'bigscience/T0_3B'
    return api_call(input, model_name)


def api_call(input, model_name):
    actual_url = API_URL + model_name
    payload = {'inputs':input}
    response = requests.post(actual_url, headers=headers, json=payload)
    return response.json()
    