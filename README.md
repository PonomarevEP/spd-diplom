Документация по API

## Посты

- **GET /api/posts/**: Получение списка всех постов.
- **POST /api/posts/**: Создание нового поста.
- **GET /api/posts/{id}/**: Получение деталей поста.
- **PUT /api/posts/{id}/**: Редактирование поста.
- **DELETE /api/posts/{id}/**: Удаление поста.

## Комментарии

- **GET /api/comments/**: Получение списка всех комментариев.
- **POST /api/comments/**: Создание нового комментария.
- **GET /api/comments/{id}/**: Получение деталей комментария.
- **PUT /api/comments/{id}/**: Редактирование комментария.
- **DELETE /api/comments/{id}/**: Удаление комментария.

## Лайки

- **GET /api/likes/**: Получение списка всех лайков.
- **POST /api/likes/**: Создание нового лайка.
- **GET /api/likes/{id}/**: Получение деталей лайка.
- **DELETE /api/likes/{id}/**: Удаление лайка

###Регистрация пользователя: 
curl -X POST "http://127.0.0.1:8000/register/" -d "username=your_username&password=your_password"

###Получение токена:
curl -X POST "http://127.0.0.1:8000/login/" -d "username=your_username&password=your_password"

curl -X GET "http://127.0.0.1:8000/api/posts/" -H "Authorization: Token your_token_here"
curl -X GET "http://127.0.0.1:8000/api/comments/" -H "Authorization: Token your_token_here"
curl -X GET "http://127.0.0.1:8000/api/posts/" -H "Authorization: Token your_token_here"
