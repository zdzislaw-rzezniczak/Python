import requests
import json

CLIENT_ID = ""
CLIENT_SECRET = ""
TOKEN_URL = "https://allegro.pl/auth/oauth/token"


def get_access_token():
    try:
        data = {'grant_type': 'client_credentials'}
        access_token_response = requests.post(TOKEN_URL, data=data, verify=False,
                                              allow_redirects=False, auth=(CLIENT_ID, CLIENT_SECRET))
        tokens = json.loads(access_token_response.text)
        access_token = tokens['access_token']
        return access_token
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_main_categories(token):
    try:
        url = "https://api.allegro.pl/sale/categories"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        main_categories_result = requests.get(url, headers=headers, verify=False)
        return main_categories_result
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_product(token):
    try:
        url = "https://api.allegro.pl/sale/products"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        params = {
            "phrase": "Dell",
        }
        product = requests.get(url, headers=headers, verify=False, params=params)
        return product
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def main():
    access_token = get_access_token()
    # print("access token = " + access_token)
    # categories = get_main_categories(access_token)
    # print(categories.json())
    products = get_product(access_token)
    print(products.json())


if __name__ == "__main__":
    main()
