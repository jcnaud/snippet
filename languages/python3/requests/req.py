# coding: utf-8

import requests
import traceback

def main():
    # URL+Query
    url = "https://example:443/chemin/86"
    querystring = {
        "name":"toto",
        "key":["home","office"] # Multi values
        }
    # Headers
    headers = {
        'accept-encoding': "gzip",
        'accept': "application/json"
        }
    # Body
    payload = ""

    try:
        rep = requests.request(
            "DELETE",
            url,
            data=payload,
            headers=headers,
            params=querystring,
            allow_redirects=True,  # Allow redirection by default (Better)
            timeout=10)  # Time out in seconde
    except requests.exceptions.RequestException as e: # Générale exception
        #traceback.print_exc()
        raise

    # rep.status_code
    # rep.headers['content-type']
    # rep.encoding
    # rep.text
    # rep.json()
    # rep.history # List of redirection
    print(rep.text)

if __name__ == '__main__':
    main()
