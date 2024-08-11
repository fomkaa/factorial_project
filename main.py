import requests  # Модуль для обработки URL
import math, re


def factorial (a):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    body={'number': a}
    link='https://qa-test.emcd.io/factorial'
    if isinstance(a, int) == False :
        return 'Please enter an integer'
    try:
        full_page = requests.post(link, data=body, headers=headers)
        full_page.raise_for_status()
        data = full_page.json()
        try:
            math.isinf(data['answer'])
        except OverflowError:
            data['answer']='Infinity'
        return data['answer']
    except requests.exceptions.HTTPError as errh:
        if full_page.status_code == 500:
            print("Server error: 500 Internal Server Error")
            return '500'
        else:
            print(f"HTTP Error: {errh}")

def get_elements(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    try:
        full_page = requests.get(link, headers=headers)
        full_page.raise_for_status()
        data = full_page.text
        #print(data)
        return data
    except requests.exceptions.HTTPError as errh:
        if full_page.status_code == 500:
            print("Server error: 500 Internal Server Error")
    return

def extract_links(text):
    pattern = r'href="([^"]+)">([^<]+)</a>'
    return re.findall(pattern, text)

def hand_fact(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result
