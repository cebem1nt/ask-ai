import google.generativeai as genai
import argparse, os, configparser
from colorama import Style, Fore

from rich.console import Console
from rich.markdown import Markdown

def get_key(dir='askai', file='key.ini') :
    config = configparser.ConfigParser()
    full_dir = os.path.expanduser(os.path.join('~', '.config', dir))
    config_file = os.path.join(full_dir, file)

    if os.path.exists(config_file):
        config.read(config_file)
    else:
        raise Exception('No config file. please run setup')

    if not config['KEY']:
        raise Exception(f'No key in config file: {config_file}')
    
    return config['KEY']['key']

def main(api_key, text_request):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(text_request)
    print('')
    print('\u2665')
    print('')
    
    try:
        response_md = Markdown(response.text)
        console = Console()
        console.print(response_md)

    except Exception as e:
        print(Fore.RED + f'{type(e).__name__}: {e}')

    print(Style.RESET_ALL) 

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Ask gemini anything you need in terminal')
    p.add_argument('text_request', nargs='+', help='Your text request')

    args = p.parse_args()
    API_KEY = get_key()
    
    if ' ' in API_KEY or len(API_KEY) < 15:
        raise Exception("Looks like a weird api key!")

    main(API_KEY, ' '.join(args.text_request))
