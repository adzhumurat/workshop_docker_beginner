# Подготовка машины к работе

## Установка docker

Если у вас Мак или Линукс, то проблем с установкой докера не будет - на офсайте есть хорошие инструкции
* [тут Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [тут MacOS](https://docs.docker.com/docker-for-mac/install/)
* Если у Windows, то для установки `docker toolbox` нужно использовать вот [эту инструкцию](https://docs.docker.com/toolbox/toolbox_install_windows/) и затем [установить сам docker](https://docs.docker.com/docker-for-windows/install/)

Когда docker будет установлен, проверьте его работу командой
<pre>
docker run hello-world
</pre>

Если не работает, или работает только с `sudo` - продолжайте настраивать. Когда заработает - можно переходить к загрузке исходных данных.

Так же понадобится утилита `docker-compose`, устанавливать [строго по инструкции с официального сайта](https://docs.docker.com/compose/install/)

## Загрузка файлов csv

Для начала создайте пустую директорию, в которой ваши докер-приложения будут хранить данные, например у меня это `/usr/local/share/source_data`.
Дайте на директорию самые широкие права, чтобы наверняка ничего не завалилось при записи или чтении (в продакшн-среде, конечно, так делать нельзя).
<pre>
sudo mkdir /usr/local/share/source_data; sudo chmod 777 /usr/local/share/source_data;
</pre>

Добавьте в `~/.bash_profile` (для MacOS) или в `~/bashrc` (для Ubuntu) переменную окружения `SOURCE_DATA`, чтобы упростить работу с данными

<pre>
export SOURCE_DATA="/usr/local/share/source_data"
</pre>

Дальше инструкции только для Ubuntu, для MacOS аналогично. Активируем нашу переменную с помощью утилиты `source` и проверяем, что она доступна в текущем терминале с помощью команды `echo`.
<pre>
source ~/.bashrc; echo $SOURCE_DATA;
</pre>

Эти действия мы совершили для того, чтобы более удобно настроить рабочую среду: скачать данные, залить их в Postgres и т.д.
Мы установили переменную среды **SOURCE_DATA** - туда, в эту директорию, будет распакован архив с данными, которые будем загружать в Postgres - это набор `csv` файлов.

Если видите название директории - всё ок, переходим к созданию поддиректорий.
<pre>
mkdir $SOURCE_DATA/raw_data; mkdir $SOURCE_DATA/pg_data;
</pre>

Проверим, что все директории созданы успешно

<pre>
ls $SOURCE_DATA
</pre>

Результат работы команды
<pre>
raw_data, pg_data
</pre>

Скачайте архив `raw_data.zip` [по этой ссылке](https://drive.google.com/file/d/1ZmRvyaUJ1vnqCn_v_kyqC4YoLEHJWWTW/view?usp=sharing) и распакуйте его содержимое в `${SOURCE_DATA/raw_data`.
Проверьте корректность распаковки с помощью команды

<pre>
ls ${SOURCE_DATA}/raw_data
</pre> 

Результат работы команды
<pre>
links.csv ratings.csv tags.json test.json
</pre>

Если данные в директории есть - поздравляю, вы полностью готовы к участию в воркшопе! Перед началом практики познакомимся с [основными концепциями Docker](./docker_intro.md).
