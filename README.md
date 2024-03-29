# LMS
[![Build Status](https://travis-ci.org/care1e55/LMS.svg?branch=develop)](https://travis-ci.org/care1e55/LMS)
[![codecov](https://codecov.io/gh/care1e55/LMS/branch/develop/graph/badge.svg)](https://codecov.io/gh/care1e55/LMS)


Проект с сервисом LMS по [заданию](https://gist.github.com/Invizory/c02fdadfbe4a33f00b10b50b20142587)

Для развертывания и тестирования решения локально понадобится docker, docker-compose версии 1.25.0 и httpie.
Пакеты могут быть установлены выполнением команд или следованиию рекомендации с официальных сайтов проектов:

```bash
sudo apt-get update
sudo apt install -y httpie
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo apt-get install     ca-certificates     curl     gnupg     lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo   "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose --version
```

Локально решение поднимается как docker-compose с парметрами подключения к БД. Все парметры кроме `POSTGRES_PASSWORD` могут быть выставлены по умолчанию. Требуется версия docker-compose 1.27.
Предварительно необходимо чтобы в среде присутсвовали переменные окружения для подключения в БД:
```bash
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
export POSTGRES_SCHEMA=postgres
export POSTGRES_PASSWORD=<password here>
```

```bash
docker-compose build --build-arg POSTGRES_PASSWORD="$POSTGRES_PASSWORD"
docker-compose up -d
```

Тесты запускаются при поднятом приложении из директории с проектом:
```bash
python -m unittest -v app/tests/controllers_test.py 
```

REST API реализовано на flask. В качестве ORM выбрано SQL Alchemy.

Решение представлено в виде docker-compose - имейджи приложения собираются на Travis 
и пушатся в публичный DockerHub: [LMS flask app](https://hub.docker.com/repository/docker/care1e55), [postgres](https://hub.docker.com/repository/docker/care1e55)

Сервис деплоится на Digital Ocean и доступен по адресу **http://188.166.68.217:5000**, например получиться информацию по профилю сутдента:

В случае тестирования локально адрес заменяется на localhost

Для использования сервиса предварительно необходимо активировать аккаунт по регистрационному, email и паролю в POST запросе:
```bash
http -f POST http://188.166.68.217:5000/register registration_code=code1 email=student1@example.com  password=student1
```

Должны увидеть в логах что запрос выполнен успешно и пользователь активирован:
```bash
HTTP/1.0 200 OK
Content-Length: 2
Content-Type: text/html; charset=utf-8
Date: Sun, 12 Dec 2021 09:44:40 GMT
Server: Werkzeug/2.0.2 Python/3.6.15

OK
```

После регистрации аутентификация по логину и паролю и получениее cookie с токеном
```bash
http --auth student1@example.com:student1 http://188.166.68.217:5000/get-auth-token
```

При тестировании через CLI cookie понадобится подставлять ко всем запроса вручную. Также не будет работать редирект. Например, посмотреть собственный профиль:
```bash
http http://188.166.68.217:5000/profile 'Cookie:token=<token>'
```

Редиректит на аналогичный эндпоинт:
```bash
http http://188.166.68.217:5000/profile/00000000-0000-0000-0000-000000000001 'Cookie:token=<token>'
```

DDL для создания сущностей и наполнение тестовыми данными приведено в `init.sql` котрый запускается в entrypoin 
контейнера. В качестве идентификаторов используется uuid4, который генерируется автоматичеки, если не задан. Сущности связаны через primary key -> foreign key constraint. К сожалению, пока нет раздиления на prod и test среды, поэтому все создается в схеме postgres по умолчанию.

Переменные окружения и секреты прописаны в Travis.

При сборке запускаются тесты и линтинг, но последний только показывает скор и места нарушений не останавливая сборку.


Очевидно, что реализация далека от идела и связано с тем, что фреймворк и подходы постигались в во время разработки, а не перед. Что, по моему мнению, можно сделать лучше:

 - [ ] Flask приложение может и должно деплоится с различными вариантами кофига development, prod, debug
 - [ ] Архитектурно в приложении фактически отсутствует слой представления, хотя, думаю, сами эндпоинты могут выступать в этой роли. Также часть функционала из controllers могло бы быть инкапсулировано в models.
 - [ ] Генерация токена и аутентификация сделана "костыльно" и не безопасно, без использования таблицы с сессиями. Лучше использовать JWT и логику сессий с персистентностью.
 - [ ] Отсутвует документация на api, докстринги и комментарии
 - [ ] Не используется typing для python
 - [ ] Таблицы связываются через query в контроллерах, хотя связи могли бы быть прописаны в модели
 - [ ] Отсутвет exception handling на различные виды ошибок
 - [ ] Код дублируется и часть логики могла быть вынесена в кастомные декораторы flask
 - [ ] Пароли не хешируются
 - [ ] В целом архитектурные принципы, ООП, DRY и KISS не выдержены в должной мере.
 - [ ] Линтер подтверждает наличие code smells и нарушение конвенций
 - [ ] Не весь функционал по спецификации реализован
