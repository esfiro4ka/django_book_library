## Запуск в режиме разработки

1. Убедитесь, что у вас установлены Docker и Docker Compose.

2. Склонируйте данный репозиторий на свой локальный компьютер:

   ```bash
   git clone https://github.com/esfiro4ka/django_book_library.git
   ```

3. Перейдите в директорию с проектом:

   ```bash
   cd django_book_library
   ```

4. Создайте файл .env внутри директории infra:

   ```bash
   touch infra/.env
   ```
   Внесите в него значения переменных окружения (указанные ниже значения приведены для примера, вам необходимо ввести собственные данные):

   ```bash
        # Параметры Django:
        DJANGO_SECRET_KEY=testsecretkey # секретный ключ Django, используемый для хэширования паролей, создания токенов и других целей безопасности

        # Параметры для подключения к базе данных MySQL:
        MYSQL_DATABASE=book-library # имя БД
        MYSQL_USER=book-library # имя пользователя БД
        MYSQL_PASSWORD=mypassword # пароль пользователя БД
        MYSQL_HOST=db # хост, на котором развернута БД
        MYSQL_PORT=3306 # порт, на котором развернута БД
        MYSQL_ROOT_PASSWORD=myrootpassword # пароль пользователя root БД

        # Параметры для Celery и Redis:
        REDIS_PASSWORD=redispassword #пароль для доступа к серверу Redis
        CELERY_BROKER_URL=redis://redis:6379/0 # URL для брокера сообщений Celery
        CELERY_RESULT_BACKEND=redis://redis:6379/0 # URL для хранения результатов задач Celery

        # Параметры почтового ящика для исходящей почты:
        EMAIL_HOST=smpt.mail.ru # имя хоста
        EMAIL_PORT=2525 # порт хоста электронной почты
        EMAIL_HOST_USER=mymail@mail.ru # имя пользователя
        EMAIL_HOST_PASSWORD=mypassword # пароль электронной почты для внешнего приложения
   ```

5. Соберите Docker-образы и запустите контейнеры:

    ```bash
    docker-compose -f infra/docker-compose.yml build
    ```

    ```bash
    docker-compose -f infra/docker-compose.yml up -d
    ```

6. После успешного запуска вы можете, например, создать книгу, отправив POST-запрос на [http://127.0.0.1:8000/api/v1/books/](http://127.0.0.1:8000/api/v1/books/)

    ```json
    {
        "name": "Новое название книги",
        "author": "Новый автор книги",
        "publishing_year": 2000,
        "isbn": "978-2-266-11156-0"
    }
    ```

    Или зарегистрировать пользователя (предоставьте настоящую электронную почту), отправив POST-запрос на [http://127.0.0.1:8000/api/v1/users/registration/](http://127.0.0.1:8000/api/v1/users/registration/)

    ```json
    {
        "password": "password",
        "username": "username",
        "email": "example@mail.ru"
    }
    ```

7. Вы можете остановить контейнеры с помощью команды:

   ```bash
    docker-compose -f infra/docker-compose.yml down
   ```
