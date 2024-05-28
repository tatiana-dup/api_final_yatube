## Описание проекта:

Этот проект представляет собой API для управления публикациями и подписками. Он использует Django и Django REST Framework для реализации функционала. Аутентификация пользователей настроена по JWT-токену с использованием Djoser.
Авторизованные пользователи могут создавать публикации, оставлять комментарии и подписываться на других пользователей.
Неавторизованным пользователям доступен просмотр публикаций, сообществ, к которым могут относиться публикации, и комментариев.
Изменять и удалять публикации и комменатрии могут только их авторы.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:tatiana-dup/api_final_yatube.git
```

```
cd api_final_yatube/
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры запросов:

### Получение всех публикаций
```
GET /api/v1/posts/
```

### Создание публикации
```
POST /api/v1/posts/
Content-Type: application/json
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

### Получение публикации
```
GET /api/v1/posts/{id}/
```

### Получение всех комментариев к публикации
```
GET /api/v1/posts/{post_id}/comments/
```

### Добавление комментария к публикации
```
POST /api/v1/posts/{post_id}/comments/
Content-Type: application/json
{
    "text": "string"
}
```

### Получение комментария
```
GET /api/v1/posts/{post_id}/comments/{id}/
```

### Получение всех сообществ
```
GET /api/v1/groups/
```

### Информация о сообществе
```
GET /api/v1/groups/{id}/
```

### Получение всех подписок пользователя
```
GET /api/v1/follow/
```

### Подписка пользователя на другого
```
POST /api/v1/follow/
Content-Type: application/json
{
    "following": "string"
}