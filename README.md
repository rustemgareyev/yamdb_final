# Учебный проект yamdb_final 

### Описание проекта
Yamdb_final это учебный проект, в котором реализована API сервиса, 
на котором можно размещать произведения, каталогизировать их, 
комментировать и подписываться на интересных авторов. 

### Авторы проекта
Именно этот вариант сборки собирало три человека, я — Гареев Рустем, Андрей Орлов и Татьяна Комарова. Все мы студенты Яндекс.Практикума. 

### Как развернуть проект локально
Проект упакован в Докер, запускается командой
    docker-compose up -d
Для того, чтобы команда выполнилась необходимо установить Docker, сделать это можно на официально сайте https://www.docker.com.
Далее необходимо выполнить миграции командой
    sudo docker-compose exec web python manage.py migrate
После этого создать суперпользователя, используя команду
    sudo docker-compose exec web python manage.py createsuperuser
И наконец, собрать статику командой
    sudo docker-compose exec web python manage.py collectstatic --no-input

### Ссылка на проект
Развернутый проект доступен по ссылке http://84.201.167.152


### Статус workflow
![example workflow](https://github.com/rustemgareyev/yamdb_final/actions/workflows/yamdb_workflow/badge.svg)
