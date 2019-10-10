# бщение контейнеров по сети

Мы уже умеем создавать bridge-сети, самое время научиться их использовать. 

## Клиент-серверное взаимодействие с Postgres

Для тренировки создадим два контейнера: Postgres-сервер и Postgres-клиент, объединив их с помощью сети `ivi_network`.

### Шаг 1. Запускаем Postgres-сервер

Подходящий мне легковесный контейнер я нашёл на [docker hub](https://hub.docker.com/_/postgres)

<pre>
docker run --name ivi-postgres --network ivi_network -v "${SOURCE_DATA}/pg_data:/var/lib/postgresql/data" -d postgres:10-alpine
</pre>

Обратите внимание на опцию `-v` - мы монтируем директорию с локальной машины `${SOURCE_DATA}/pg_data` во внутреннию директорию контейнера `/var/lib/postgresql/data`.
Эта директория примечательная тем, что в ней Postgres-сервер будет хранить свои мета-данные, в том числе - таблицы в бинарном формате. Мы **не хотим** хранить лишние данные внутри контейнера!

Опуция `-d` отключает ваш сеанс терминала от терминала контейнера. Проверить, что контейнер действительно запустился можно с помощью `docker ps`.

### Шаг 2. Запускаем Postgres-клиент

Для доступа к Postgres-серверу нужен клиент psql. Чтобы получить доступ к контейнеру с Postgres-сервером запустим ещё контейнер с psql. 

Обратите внимание, что мы маунтим директорию с данными 

<pre>
docker run -it --rm  --network ivi_network -v "${SOURCE_DATA}/raw_data:/usr/share/raw_data" postgres:10-alpine psql -h ivi-postgres -U postgres
</pre>

Когда поднимали Postgres-сервер, то ограничились названием образа, который хотим использовать.
Обратите внимание, что сейчас кроме названия образа в `run` добавился вызов бинарника постгрес-клиента `psql -h ivi-postgres -U postgres`.
Кроме того, пропала опция `-d` - мы не хотим отключаться от терминала контейнера, мы хотим интерактивный сеанс.

### Шаг 3. Пишем SQL через клиента

Вы подключилились в сеанс терминала докер-контейнера, в котором запущен `psql` самое время залить в постгрю данные - не зря же мы смонтировали в контейнер с клиентом директорию `${SOURCE_DATA}/raw_data`/

Начнём с того, что создадим таблицу, куда будем заливать csv файл

<pre>
CREATE TABLE ratings (userId bigint, movieId bigint, rating float(25), timestamp bigint);
</pre>

Далее волшебство докера - вызываем команду `\copy` из `psql`:

<pre>
\copy ratings FROM '/usr/share/raw_data/ratings.csv' DELIMITER ',' CSV HEADER;
</pre>

Обратите внимание на путь до файла - эта директория **внутри** контейнера с постгрес-клиентом.
Но сам файл `ratings.csv` лежит на вашей локальной хост-машине в директории `${SOURCE_DATA}/raw_data`!

Осталось проверить, что обмана нет и файл действительно загрузился. Для чистоты эксперимента закройте терминал с докер-клиентом и выполните на хост-машине команду

<pre>
docker run -it --rm  --network ivi_network postgres:10-alpine psql -h ivi-postgres -U postgres -с "SELECT COUNT(*) FROM ratings;"
</pre>

Вы должны увидеть в консоли результат запроса - количество строк в свежесозданной таблице.

Если все получилось - поздравляю, вы великолепны. Вы умеете поднимать контейнеры, подключать к ним внешние файлы, а так же соединять контейнеры bridge-сетью

До сих пор мы использовали уже готовые образы - самое время научиться делать кастомные образы [с помощью Dockerfile](./docker_build.md)