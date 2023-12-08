<a id="anchor"></a>
<div align=center>

  # Проект Трекер развития

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
  ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
  ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
  
</div>

## Описание проекта

Проект для образовательной платформы Яндекс Практикум.

Этот проект добавляет новый функционал к сервису карьерный трекер. Благодаря этому проекту можно узнать свой текущий уровень навыков и грейд, посмотреть список навыков необходимых для развития, ознакомится с рекомендациями курсов, проектами Мастерской и ресурсами Базы знаний.

Пользователям доступна возможность выбора специальности и прохождение теста, чтобы узнать текущий уровень навыков, а также ознакомиться с рекомендациями, чтобы в дальнейшем повысить свой уровень компетенций.

Кроме того, на основе выбранной специальности и результатах пройденного теста формируются рекомендации на курсы яндекс практикума, проекты мастерской и ресурсы базы знаний.

Для доступа к функционалу требуется пройти бесплатную регистрацию.

### Технологии

[**Backend**](https://github.com/Hackaton-development-tracker/tracker-backend)

* Python 3.9.10
* Django 4.2
* djangorestframework 3.14.0


### Инфраструктура: 

* Docker
* NGINX
* GUNICORN
* база даннных POSTGRESQL

### Основные библиотеки:

- аутентификация Djoser
- документация drf-yasg

### Запуск проекта:

1. Клонировать проект на машину одним из способов:
> SSH
> ```
> git clone git@github.com:Hackaton-development-tracker/tracker-backend.git
> ```

> HTTPS
> ```
> git clone https://github.com/Hackaton-development-tracker/tracker-backend.git
> ```

> GitHub CLI
> ```
> git clone gh repo clone Hackaton-development-tracker/tracker-backend
> ```
#### Боевой режим (PostgtreSQL):
1. В корневой дирректории создать файл с переменными окружения `.env` и наполнить его по шаблону:
```
DB_NAME=tracker_db
DB_USER=admin
DB_PASSWORD=admin
DB_PORT=5432
ENVIRONMENT=production
```
2. Из корневой дирректории запустить сборку приложения:
```bash
sudo docker-compose up -d --build
```
3. Создать учетную запись администратора
```bash
sudo docker-compose exec app python manage.py createsuperuser
```
4. Сервис будет доступен по адресу `http://<ip remote server>:8000/admin/`

#### Режим тестирования (SQLite):
1. В корневой дирректории создать файл с переменными окружения `.env` и наполнить его по шаблону:
```
DB_NAME=tracker_db
DB_USER=admin
DB_PASSWORD=admin
DB_PORT=5432
ENVIRONMENT=testing
```
2. Из корневой дирректории с файлом Dockerfile запустить сборку образа Docker:
> <span style="color:#1E90FF">**Note:**</span> <span style="color:#FFFF00">**В режиме тестирования сборка ведется на основе Dockerfile.testing без поддержки psycopg2 для PostgreSQL**</span>
```bash
sudo docker build -t <app name> -f Dockerfile.testing . 
```
1. Запустить контейнер с приложением командой:
```bash
sudo docker run -p 8000:8000 -d --name <container name> <image name> 
```
1. Сервис будет доступен по адресу `http://localhost:8000/admin/`

### Документация

Доступна после запуска сервиса:

**swagger** - `http://localhost:8000/swagger/`  
**redoc** - `http://localhost:8000/redoc/`

## Сервис разрабатывали:
<details>
<summary>
<h4>Backend</h4>
</summary>

<br>

**Форов Александр** 

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)

**Павел Смирнов**

[![Telegram Badge](https://img.shields.io/badge/-B1kas-blue?style=social&logo=telegram&link=https://t.me/B1kas)](https://t.me/B1kas) [![Yamail Badge](https://img.shields.io/badge/baksbannysmirnov@yandex.ru-FFCC00?style=flat&logo=ycombinator&logoColor=red&link=mailto:baksbannysmirnov@yandex.ru)](mailto:baksbannysmirnov@yandex.ru)

</details>

_[Вверх](#anchor)_
