import requests
import json
from config import TOKEN, keys

class ConvertionException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(c_chto: str, c_kuda: str, c_kol_vo: str):
        if c_chto == c_kuda:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {c_chto}')
        try:
            chto_tiker = keys[c_chto]
        except KeyError:
            raise ConvertionException(f'Невозможно обработать валюту {c_chto}')
        try:
            kuda_tiker = keys[c_kuda]
        except KeyError:
            raise ConvertionException(f'Невозможно обработать валюту {c_kuda}')
        try:
            c_kol_vo = float(c_kol_vo)
        except ValueError:
            raise ConvertionException(f'Невозможно обработать количество {c_kol_vo}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={chto_tiker}&tsyms={kuda_tiker}')
        total = str(float(json.loads(r.content)[keys[c_kuda]])*c_kol_vo)
        return total