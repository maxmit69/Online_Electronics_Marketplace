# Онлайн-магазин электроники

Этот проект представляет собой систему управления сетью продажи электроники с использованием Django и Django REST
Framework. Система включает в себя модели для управления предприятиями и продуктами, а также API для взаимодействия с
этими данными.

## Предварительные требования

- Python 3.12 или новее
- Poetry 1.4.0 или новее

## Установка

Для установки проекта выполните следующие шаги:

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/maxmit69/Online_Electronics_Marketplace
   ```
2. Перейдите в каталог проекта:
   ```sh
   cd Online_Electronics_Marketplace
   ```
3. Установите Poetry, если он еще не установлен:
   ```sh
    curl -sSL https://install.python-poetry.org | python3 -
   ```
   Затем добавьте Poetry в PATH, добавив следующую строку в ваш профиль (~/.bashrc, ~/.zshrc или аналогичный файл):
   export PATH="$HOME/.local/bin:$PATH"

4. Активируйте виртуальное окружение, созданное Poetry:
   ```sh
   poetry shell
   ```
5. Установите зависимости проекта с помощью Poetry:
   ```sh
   poetry install
   ```
6. Создайте файл .env в корне проекта, чтобы настроить параметры конфигурации.
   Пример содержимого файла env.example:
   ```sh
    DEBUG=True
    SECRET_KEY=your-secret-key
    DATABASE_URL=postgres://user:password@localhost:5432/yourdatabase
   ```
7. Выполните миграции базы данных:
   ```sh
   poetry run python manage.py migrate
   ```
8. Создайте суперпользователя (если необходимо):
   ```sh
   poetry run python manage.py createsuperuser
   ```
9. Загрузите фикстуры данных (если необходимо):
   ```sh
   poetry run python manage.py loaddata network/fixtures/network_data.json
   ``` 
10. Запустите сервер:
   ```sh
   poetry run python manage.py runserver
   ```

## API

### Эндпоинты

- /api/nodes/: Управление узлами сети
    - GET /api/nodes/: Получить список узлов
    - POST /api/nodes/: Создать новый узел
    - GET /api/nodes/{id}/: Получить детали узла
    - PUT /api/nodes/{id}/: Обновить узел
    - DELETE /api/nodes/{id}/: Удалить узел
- /api/products/: Управление продуктами
    - GET /api/products/: Получить список продуктов
    - POST /api/products/: Создать новый продукт
    - GET /api/products/{id}/: Получить детали продукта
    - PUT /api/products/{id}/: Обновить продукт
    - DELETE /api/products/{id}/: Удалить продукт

### Примеры запросов

Получение списка узлов сети (GET /api/nodes/)

  ```sh
   curl -X GET "http://localhost:8000/api/nodes/" -H "Authorization: Bearer <your-token>"
  ```

Пример ответа:
   ```json
   [
  {
    "id": 1,
    "name": "Завод А",
    "email": "factoryA@example.com",
    "country": "Россия",
    "city": "Москва",
    "street": "Ленина",
    "house_number": "10",
    "debt": "0.00",
    "level": "Завод",
    "created_at": "2024-08-21T06:20:16.298753Z",
    "supplier": null,
    "user": 1,
    "products": []
  },
  {
    "id": 2,
    "name": "Розничная сеть Б",
    "email": "retailB@example.com",
    "country": "Россия",
    "city": "Санкт-Петербург",
    "street": "Невский пр.",
    "house_number": "24",
    "debt": "1000.00",
    "level": "Розничная сеть",
    "created_at": "2024-08-21T06:25:16.298753Z",
    "supplier": 1,
    "user": 2,
    "products": []
  }
]
   ```

Создание нового узла сети (POST /api/nodes/)
```sh
curl -X POST "http://localhost:8000/api/nodes/" \
-H "Authorization: Bearer <your-token>" \
-H "Content-Type: application/json" \
-d '{
   "name": "Индивидуальный предприниматель В",
   "email": "ipV@example.com",
   "country": "Россия",
   "city": "Казань",
   "street": "Кремлевская",
   "house_number": "30",
   "supplier": 2,
   "user": 3
}'
```

Пример ответа:

   ```json
   {
  "id": 3,
  "name": "Индивидуальный предприниматель В",
  "email": "ipV@example.com",
  "country": "Россия",
  "city": "Казань",
  "street": "Кремлевская",
  "house_number": "30",
  "debt": "0.00",
  "level": "Индивидуальный предприниматель",
  "created_at": "2024-08-21T06:30:16.298753Z",
  "supplier": 2,
  "user": 3,
  "products": []
}
   ```

## Используемые технологии

- Django
- Django REST Framework
- PostgreSQL
- Poetry для установки и управления зависимостями проекта

## Разработчики

- [Сергей Аристов](https://github.com/maxmit69)

## Контакты

- [GitHub](https://github.com/maxmit69/Online_Electronics_Marketplace)
- [Telegram](https://t.me/sergeiaris)
- [Email](maxmit83@gmail.com)

## Дополнительная информация

Для получения дополнительной информации и настроек, смотрите документацию:

- [Django](https://docs.djangoproject.com/en/4.1/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Poetry](https://python-poetry.org/)
