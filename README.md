# LMS
[![Build Status](https://travis-ci.org/care1e55/LMS.svg?branch=cov_and_lint)](https://travis-ci.org/care1e55/LMS)
[![codecov](https://codecov.io/gh/care1e55/LMS/branch/cov_and_lint/graph/badge.svg)](https://codecov.io/gh/care1e55/LMS)


Проект с сервисом LMS по [заданию](https://gist.github.com/Invizory/c02fdadfbe4a33f00b10b50b20142587)

REST API реализовано на flask. В качестве ORM выбрано SQL Alchemy.

DDL для создания сущностей приведено в init.sql. В качестве идентификаторов используется uuid4, который генерируется автоматичеки, если не задан. Сущности связаны через primary key -> foreign key constraint.

TODO:
 - [ ] Docker compose
 - [ ] Дореализовать функционал по спецификации
 - [ ] Logging, sessions, cookies
 - [ ] убрать дублирования кода
 - [ ] Добавить codecov, pylint, CI
 - [ ] POST/PUT/DELETE тесты
 - [ ] Разнести контролленры по файлам?
