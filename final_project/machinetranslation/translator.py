'''
Created By Raghav Atreya
    # en-de selects the IBM-provided base model for English-to-German translation
    # source language code
    # target language code
    # English --> en
    # french --> fr

'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv('apikey')
url = os.getenv('url')


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_spanish(text):
    '''
    This function return english to spanish translation
    '''
    translation = language_translator.translate(
        text=text,
        model_id='en-es').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation['translations'][0]['translation']



def spanish_to_english(text):
    '''
    This function return spanish to english translation
    '''
    translation = language_translator.translate(
        text=text,
        model_id='es-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation['translations'][0]['translation']

def english_to_french(text):
    '''
    This function return english to french
    translation
    '''
    translation = language_translator.translate(
        text=text,
        model_id='en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation['translations'][0]['translation']


def french_to_english(text):
    '''
    This function return french to
    english translation
    '''
    translation = language_translator.translate(
        text=text,
        model_id='fr-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation['translations'][0]['translation']


if __name__ == '__main__':
    print(english_to_french("""Lingvanex"""))
    print(french_to_english('raghav est un bon garçon'))
