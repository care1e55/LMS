# LMS
[![Build Status](https://travis-ci.org/care1e55/LMS.svg?branch=develop)](https://travis-ci.org/care1e55/LMS)
[![codecov](https://codecov.io/gh/care1e55/LMS/branch/develop/graph/badge.svg)](https://codecov.io/gh/care1e55/LMS)


Проект с сервисом LMS по [заданию](https://gist.github.com/Invizory/c02fdadfbe4a33f00b10b50b20142587)


Локально решение поднимается как docker-compose с парметрами подключения к БД. Все парметры кроме `POSTGRES_PASSWORD` могут быть выставлены по умолчанию. Требуется версия docker-compose 1.27:
```bash
docker-compose build --build-arg POSTGRES_PASSWORD="$POSTGRES_PASSWORD"
docker-compose up -d
```

Тесты запускаются при поднятом приложении:
```bash
python -m unittest -v app/tests/controllers_test.py 
```

REST API реализовано на flask. В качестве ORM выбрано SQL Alchemy.

Решение представлено в виде docker-compose - имейджи приложения собираются на Travis 
и пушатся в публичный DockerHub: [LMS flask app](care1e55/lms-app), [postgres](care1e55/lms-db)

Сервис деплоится на Digital Ocean и доступен по адресу **http://188.166.116.10:500**, например получиться информацию по профилю сутдента:
```
curl http://188.166.116.10:5000/profile/00000000-0000-0000-0000-000000000001
```

DDL для создания сущностей и наполнение тестовыми данными приведено в `init.sql` котрый запускается в entrypoin 
контейнера. В качестве идентификаторов используется uuid4, который генерируется автоматичеки, если не задан. Сущности связаны через primary key -> foreign key constraint. К сожалению, пока нет раздиления на prod и test среды, поэтому все создается в схеме postgres по умолчанию.

Переменные окружения и секреты прописаны в Travis.

При сборке запускаются тесты и линтинг, но последний только показывает скор и места нарушений не останавливая сборку.




TODO:
 - [ ] fix (some) linting errors
 - [x] Docker compose
 - [ ] Дореализовать функционал по спецификации
 - [ ] Logging, sessions, cookies
 - [x] убрать дублирования кода
 - [x] Добавить codecov, pylint, CI
 - [ ] POST/PUT/DELETE тесты
 - [x] Разнести контролленры по файлам?
