import requests
from secret_token import KEY_lingvo

# Translator https://developers.lingvolive.com/ru-ru/Help

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = KEY_lingvo  # key from lingvolive.com
headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)


def lingvo_translator(word, from_what, on_which):
    if auth.status_code == 200:
        token = auth.text

        while True:
            # word = input('input word: ')
            if word:
                headers_translate = {'Authorization': 'Bearer  ' + token}
                params = {'text': word,
                          'srcLang': from_what,
                          'dstLang': on_which,
                          }
                translate_request = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
                translate_dict = translate_request.json()
                try:
                    return translate_dict.get('Translation').get('Translation')
                except:
                    return 'Мы не знаем такого слова :(('

    else:
        return 'Error'
