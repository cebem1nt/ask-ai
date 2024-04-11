import argparse, os
import google.generativeai as genai
from key import API_KEY
from colorama import Style, Fore

def main(api_key, text_request):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(text_request)
    print('\n \u2665 \n')
    print(Fore.GREEN+ response.text)
    print(Style.RESET_ALL) 

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Ask gemini anything you need in your console')
    p.add_argument('text_request', nargs='+', help='Your text request')

    args = p.parse_args()
    script_path = os.path.dirname(os.path.abspath(__file__))

    if not API_KEY:
        raise Exception("API key not found")
    
    elif ' ' in API_KEY or len(API_KEY) < 15:
        raise Exception("Looks like a weird api key!")

    main(API_KEY, ' '.join(args.text_request))
