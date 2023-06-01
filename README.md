### **Foodgram**/ _Продуктовый помощник_

### Описание

**«Продуктовый помощник»** - это сайт, на котором пользователи могут _публиковать_ рецепты, добавлять чужие рецепты в _избранное_ и _подписываться_ на публикации других авторов. Сервис **«Список покупок»** позволяет пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.
 
### Функционал

- Рецепты на всех страницах **сортируются** по дате публикации (новые — выше)
- Работает **фильтрация** по тегам, в том числе на странице избранного и на странице рецептов одного автора
- Работает **пагинатор** (в том числе при фильтрации по тегам)
- Для **авторизованных** пользователей:
  * Доступна **главная страница**
  * Доступна **страница другого пользователя**
  * Доступна **страница отдельного рецепта**
  * Доступна страница **«Мои подписки»**:
    1. Можно подписаться и отписаться на странице рецепта
    2. Можно подписаться и отписаться на странице автора
    3. При подписке рецепты автора добавляются на страницу «Мои подписки» и удаляются оттуда при отказе от подписки
  * Доступна страница **«Избранное»**:
    1. На странице рецепта есть возможность добавить рецепт в список избранного и удалить его оттуда
    2. На любой странице со списком рецептов есть возможность добавить рецепт в список избранного и удалить его оттуда
  * Доступна страница **«Список покупок»**:
    1. На странице рецепта есть возможность добавить рецепт в список покупок и удалить его оттуда
    2. На любой странице со списком рецептов есть возможность добавить рецепт в список покупок и удалить его оттуда
    3. Есть возможность выгрузить файл (.pdf) с перечнем и количеством необходимых ингредиентов для рецептов из «Списка покупок»
    4. Ингредиенты в выгружаемом списке не повторяются, корректно подсчитывается общее количество для каждого ингредиента
  * Доступна страница **«Создать рецепт»**:
    1. Есть возможность опубликовать свой рецепт
    2. Есть возможность отредактировать и сохранить изменения в своём рецепте
    3. Есть возможность удалить свой рецепт
  * Доступна и работает форма **изменения пароля**
  * Доступна возможность **выйти из системы** (разлогиниться)
- Для **неавторизованных** пользователей:
  * Доступна **главная страница**
  * Доступна **страница отдельного рецепта**
  * Доступна и работает **форма авторизации**
  * Доступна и работает **система восстановления пароля**
  * Доступна и работает **форма регистрации**
- **Администратор** и **админ-зона**:
  * Все модели выведены в админ-зону
  * Для модели пользователей включена **фильтрация** по имени и email
  * Для модели рецептов включена **фильтрация** по названию, автору и тегам
  * На админ-странице рецепта отображается общее число добавлений этого рецепта в избранное
  * Для модели ингредиентов включена **фильтрация** по названию

### Технологии

- Python 3.7
- Django 2.2.19
- Django Rest Framework 3.13.1
- PostgreSQL 13.0
- gunicorn 20.0.4
- nginx 1.21.3

### Контейнер

- Docker
- Docker Compose

### Проект развернут по адресу:

- http:// . . . 
- http:// . . . /admin - страница администратора
- http:// . . . /redoc - документация API

### Локальная установка

Клонируйте репозиторий и перейдите в него в командной строке:
```sh
git clone https://github.com/DmitryOstrovskiy/foodgram-project-react.git && cd foodgram-project-react
```
Перейдите в директорию с файлом _Dockerfile_ и запустите сборку образа:
```sh
cd backend && docker build -t <DOCKER_USERNAME>/foodgram:<tag> .
```
Перейдите в директорию с файлом _docker-compose.yaml_:
```sh
cd ../infra
```
Создайте .env файл:
```sh
#.env
DB_ENGINE=<django.db.backends.postgresql>
DB_NAME=<имя базы данных postgres>
DB_USER=<пользователь бд>
DB_PASSWORD=<пароль>
DB_HOST=<db>
DB_PORT=<5432>
SECRET_KEY=<секретный ключ проекта django>
```
Запустите контейнеры:
```sh
docker-compose up -d --build
```
После успешного запуска контейнеров выполните миграции в проекте:
```sh
docker-compose exec backend python manage.py makemigrations users
```
```sh
docker-compose exec backend python manage.py makemigrations recipes
```
```sh
docker-compose exec backend python manage.py migrate
```
Создайте суперпользователя:
```sh
docker-compose exec backend python manage.py createsuperuser
```
Соберите статику:
```sh
docker-compose exec backend python manage.py collectstatic --no-input
```
Наполните БД заготовленными данными:

- Ингредиенты:
```sh
docker-compose exec backend python manage.py importcsv --filename ingredients.csv --model_name Ingredient --app_name recipes
```
- Теги:
```sh
docker-compose exec backend python manage.py importcsv --filename tags.csv --model_name Tag --app_name recipes
```
Создайте дамп (резервную копию) базы данных:
```sh
docker-compose exec backend python manage.py dumpdata > fixtures.json
```
Для остановки контейнеров и удаления всех зависимостей воспользуйтесь командой:
```sh
docker-compose down -v
```

### Примеры запросов

**GET**: http://127.0.0.1:8000/api/users/  
Пример ответа:
```json
{
  "count": 123,
  "next": "http://127.0.0.1:8000/api/users/?page=4",
  "previous": "http://127.0.0.1:8000/api/users/?page=2",
  "results": [
    {
      "email": "testuser@yandex.ru",
      "id": 0,
      "username": "test.user",
      "first_name": "Test",
      "last_name": "User",
      "is_subscribed": false
    }
  ]
}
```

**POST**: http://127.0.0.1:8000/api/users/  
Тело запроса:
```json
{
  "email": "testuser@yandex.ru",
  "username": "test.user",
  "first_name": "Test",
  "last_name": "User",
  "password": "Qwerty123"
}
```
Пример ответа:
```json
{
"email": "testuser@yandex.ru",
"id": 0,
"username": "test.user",
"first_name": "Test",
"last_name": "User"
}
```

**GET**: http://127.0.0.1:8000/api/recipes/  
Пример ответа:
```json
{
  "count": 123,
  "next": "http://127.0.0.1:8000/api/recipes/?page=4",
  "previous": "http://127.0.0.1:8000/api/recipes/?page=2",
  "results": [
    {
      "id": 0,
      "tags": [
        {
          "id": 0,
          "name": "Завтрак",
          "color": "#E26C2D",
          "slug": "breakfast"
        }
      ],
      "author": {
        "email": "testuser@yandex.ru",
        "id": 0,
        "username": "test.user",
        "first_name": "Test",
        "last_name": "User",
        "is_subscribed": false
      },
      "ingredients": [
        {
          "id": 0,
          "name": "Картофель отварной",
          "measurement_unit": "г",
          "amount": 1
        }
      ],
      "is_favorited": true,
      "is_in_shopping_cart": true,
      "name": "string",
      "image": "http://127.0.0.1:8000/media/recipes/images/image.jpeg",
      "text": "string",
      "cooking_time": 1
    }
  ]
}
```

### Автор - Дмитрий Островский
