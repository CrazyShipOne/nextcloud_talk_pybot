import requests
import json
import ncbot.config as ncconfig


headers = {
    'OCS-APIRequest':'true',
    'Accept':'application/json',
    'Content-Type':'application/json'
    }


def get_response(uri,params=None):
    url = ncconfig.cf.base_url + check_uri_prefix(uri)
    if params:
        url = add_query_params(url, params)
    response = requests.get(url=url, auth=(ncconfig.cf.username, ncconfig.cf.password), headers=headers)
    return response_check(response, uri)


def post_response(uri, data):
    url = ncconfig.cf.base_url + check_uri_prefix(uri)
    json_data = json.dumps(data)
    response = requests.post(url=url, auth=(ncconfig.cf.username, ncconfig.cf.password), data=json_data, headers=headers)
    return response_check(response, uri, data)


def put_response(uri, data):
    url = ncconfig.cf.base_url + check_uri_prefix(uri)
    json_data = json.dumps(data)
    response = requests.put(url=url, auth=(ncconfig.cf.username, ncconfig.cf.password), data=json_data, headers=headers)
    return response_check(response, uri, data)


def response_check(response, uri, json_data='{}'):
    ret = ''
    if response.status_code >= 400:
        raise Exception(f"requests to {uri} failed, status code is {response.status_code}, data:\n{json_data}")
    if len(response.content) != 0:
        ret = response.json()
    return ret


def check_uri_prefix(uri: str):
    if not uri.startswith('/'):
        uri =  '/' + uri
    return uri


def add_query_params(url, params):
    # Check if the URL already has query string parameters
    if "?" in url:
        # If so, append the new parameters to the existing ones
        url = url + "&" + "&".join("{}={}".format(k, v) for k, v in params.items())
    else:
        # If not, add the new parameters as the first query string parameter
        url = url + "?" + "&".join("{}={}".format(k, v) for k, v in params.items())

    return url
