from django import template
register = template.Library()

import requests

@register.simple_tag
def random_joke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist,sexist,explicit"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()

    if response['type'] == 'twopart':
        setup = (response['setup'])
        delivery = (response['delivery'])
        return setup, delivery
    else:
        joke = (response['joke'])
        return joke

