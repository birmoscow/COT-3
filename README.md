ДЗ 3

Используется minio object storage. 

Пользователь стандартный, minioadmin : minioadmin

Токен доступа получается в начале, можно запустить docker compose, однако после надо обновить токен в file_uploader.py

Пытался ограничить место с помощью ограничений для контейнера, не пошло... ограничение только в настройках бакета

Данные загружаются из локальной папки с мемами, на всякий прикрепил zip архив (вроде не всё залилось из-за ограничения в кол-во файлов), используется скрипт на питоне.

a. Удивительно, но даже при переполнении бакета файлы продолжаются заливаться до какого-то момента
![alt text](https://github.com/birmoscow/COT-3/blob/main/srv.jpeg)
![alt text](https://github.com/birmoscow/COT-3/blob/main/srv2.jpeg)

b. В клиент прилетает ошибка и скрипт сворачивается
![alt text](https://github.com/birmoscow/COT-3/blob/main/cl.jpeg)
