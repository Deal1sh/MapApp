import requests
import sys
from io import BytesIO
from PIL import Image

def api(position, delta, map_is='map'):
    try:
        pos, delta = [], str(delta)
        for i in position:
            pos.append(str(i))
        map_api_server = 'https://static-maps.yandex.ru/1.x/'
        map_params = {
            'll' : ','.join(pos),
            'spn' : ','.join([delta, delta]),
            'l' : map_is
            }
        response = requests.get(map_api_server, params=map_params, verify=False)
        return Image.open(BytesIO(response.content))
    except:
        return