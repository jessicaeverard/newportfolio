from django import template
register = template.Library()

import requests

@register.simple_tag
def random_joke():
    url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=racist,sexist,explicit"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()

    if response['type'] == 'twopart':
        raw_setup = (response['setup'])
        raw_delivery = (response['delivery'])
        setup = raw_setup.strip()
        delivery = raw_delivery.strip()
        return setup + " " + delivery
    else:
        result = (response['joke'])
        joke = result.strip()
        return joke

@register.simple_tag
def current_london_weather():
    url = "http://api.weatherapi.com/v1/forecast.json?key=a8e94f5f4c3a4e9bab5122529220806&q=London"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()

    current_weather = (response['current'])
    return (current_weather['temp_c'])