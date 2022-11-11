# Black_Dishes
Сервис хранения и обновления меню ресторана

### Локальное развертывание
1) установи зависимости `pip install -r requirements.txt`
2) запусти бд (можно прост юзануть `docker run -p 5432:5432 -e POSTGRES_USER=black_dishes -e POSTGRES_DB=black_dishes -e POSTGRES_PASSWORD=black_dishes --name black_dishes_pg postgres`)
3) создай суперюзера `python manage.py createsuperuser`
4) сделай миграции и заполни БД тестовыми данными `/bin/bash /home/alex7gnev/PycharmProjects/black_dishes/entrypoint.sh`
5) запусти тестовый сервер и авторизуйся(некоторые методы без JWT токенов не ответят) `python manage.py runserver`

### Инструкция к API
- `api/v1/foods` - отображает публичное меню ресторана в открытом доступе, работает по принципу ReadOnlyModelViewSet(https://www.django-rest-framework.org/api-guide/viewsets/#readonlymodelviewset), отвечает без JWT токенов(https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage)
- `api/v1/dishes` - метод для CRUD блюд в меню, работает по принципу ModelViewSet(https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset), отвечает через JWT токены
- `api/v1/categories` - метод для CRUD категорий в меню, работает по принципу ModelViewSet, отвечает через JWT токены


### Развертывание прод
1) построй сборку `docker-compose up --build`
2) создай суперюзера `sudo docker exec -it black_dishes_web bash -c "python manage.py createsuperuser"`
3) миграции и заполнение бд(если не надо почисти энтрипоинт)`sudo docker exec -it black_dishes_web bash -c "sh /src/entrypoint.sh"`


### Дзен проекта
Соблюдать порядок доки
