# LMS
[![Build Status](https://travis-ci.org/care1e55/LMS.svg?branch=develop)](https://travis-ci.org/care1e55/LMS)
[![codecov](https://codecov.io/gh/care1e55/LMS/branch/develop/graph/badge.svg)](https://codecov.io/gh/care1e55/LMS)


Проект с сервисом LMS по [заданию](https://gist.github.com/Invizory/c02fdadfbe4a33f00b10b50b20142587)


Локально решение поднимается как docker-compose с парметрами подключения к БД. Все парметры кроме `POSTGRES_PASSWORD` могут быть выставлены по умолчанию. Требуется версия docker-compose 1.27:
```bash
docker-compose build --build-arg POSTGRES_PASSWORD="$POSTGRES_PASSWORD"
docker-compose up -d
```

Тесты запускаются при поднятом приложении. Предварительно необходимо чтобы в среде присутсвовали переменные окуржения для подключения в БД:
```bash
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
export POSTGRES_SCHEMA=postgres
export POSTGRES_PASSWORD=<password here>
```

```bash
python -m unittest -v app/tests/controllers_test.py 
```

REST API реализовано на flask. В качестве ORM выбрано SQL Alchemy.

Решение представлено в виде docker-compose - имейджи приложения собираются на Travis 
и пушатся в публичный DockerHub: [LMS flask app](care1e55/lms-app), [postgres](care1e55/lms-db)

Сервис деплоится на Digital Ocean и доступен по адресу **http://188.166.116.10:500**, например получиться информацию по профилю сутдента:

Аутентификация по логину и паролю и получениее cookie с токеном
```bash
http --auth 00000000-0000-0000-0000-000000000001:student1 http://188.166.116.10:5000/get-auth-token
```

При тестировании через CLI cookie понадобится подставлять ко всем запроса вручную. Также не будет работать редирект. Например, посмотреть собственный профиль:
```bash
http http://188.166.116.10:5000/profile 'Cookie:token=eyJhbGciOiJIUzUxMiIsImlhdCI6MTYxMDc5NTE4NywiZXhwIjoxNjEwNzk4Nzg3fQ.eyJ1c2VyX2lkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxIn0.C8D6tSjHxxuHt__6Xj9CbeSpCC490xE2hsHwN1QO5ug9fc2TgmsE1jpQGxTVF8Uh_X7IV9nhoAC4L1U_d6hwTw'
```

Редиректит на аналогичный эндпоинт:
```bash
http http://188.166.116.10:5000/profile/00000000-0000-0000-0000-000000000001 'Cookie:token=eyJhbGciOiJIUzUxMiIsImlhdCI6MTYxMDc5NTE4NywiZXhwIjoxNjEwNzk4Nzg3fQ.eyJ1c2VyX2lkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxIn0.C8D6tSjHxxuHt__6Xj9CbeSpCC490xE2hsHwN1QO5ug9fc2TgmsE1jpQGxTVF8Uh_X7IV9nhoAC4L1U_d6hwTw'
```

DDL для создания сущностей и наполнение тестовыми данными приведено в `init.sql` котрый запускается в entrypoin 
контейнера. В качестве идентификаторов используется uuid4, который генерируется автоматичеки, если не задан. Сущности связаны через primary key -> foreign key constraint. К сожалению, пока нет раздиления на prod и test среды, поэтому все создается в схеме postgres по умолчанию.

Переменные окружения и секреты прописаны в Travis.

При сборке запускаются тесты и линтинг, но последний только показывает скор и места нарушений не останавливая сборку.




TODO:
 - [ ] fix (some) linting errors
 - [x] Docker compose
 - [ ] Дореализовать функционал по спецификации
 - [x] Logging, sessions, cookies
 - [x] убрать дублирования кода
 - [x] Добавить codecov, pylint, CI
 - [ ] POST/PUT/DELETE тесты
 - [x] Разнести контролленры по файлам?
