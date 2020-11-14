# LMS
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
