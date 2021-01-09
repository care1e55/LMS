# LMS
[![Build Status](https://travis-ci.org/care1e55/LMS.svg?branch=develop)](https://travis-ci.org/care1e55/LMS)
[![codecov](https://codecov.io/gh/care1e55/LMS/branch/develop/graph/badge.svg)](https://codecov.io/gh/care1e55/LMS)


Проект с сервисом LMS по [заданию](https://gist.github.com/Invizory/c02fdadfbe4a33f00b10b50b20142587)

REST API реализовано на flask. В качестве ORM выбрано SQL Alchemy.

DDL для создания сущностей приведено в init.sql. В качестве идентификаторов используется uuid4, который генерируется автоматичеки, если не задан. Сущности связаны через primary key -> foreign key constraint.

TODO:
 - [ ] fix (some) linting errors
 - [x] Docker compose
 - [ ] Дореализовать функционал по спецификации
 - [ ] Logging, sessions, cookies
 - [x] убрать дублирования кода
 - [x] Добавить codecov, pylint, CI
 - [ ] POST/PUT/DELETE тесты
 - [x] Разнести контролленры по файлам?
