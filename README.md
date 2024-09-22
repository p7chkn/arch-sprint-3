## Задание №1

- 1.1 [задание](tasks/1_1.md)
- 1.2 [задание](tasks/1_2.md)
- 1.3 [задание](tasks/1_3.md)
- 1.4 [задание](tasks/1_4.md)

## Задание №2

Задание выполнено с использованием docker-compose (наставник сказал, что можно так) и nginx в качестве API Gateway. 

В качестве языка программирования используется Python.
2 новых сервиса для MVP называются device-control и telemetry. Расположены в соответствующих папках. 

### Инструкции
Чтобы поднять проект через docker-compose: нужно убедиться, что он установлен:

```shell
docker-compose version
```
или 

```shell
docker compose version
```

[Инструкция по установке docker compose](https://docs.docker.com/compose/install/)

Далее создать файл с переменными окружения, это можно сделать при помощи шаблона:
```shell
cp .env_example .env
```
При желании можно установить собственные значения.

Далее нужно поднять весь docker compose:

```shell
docker compose up -d
```
или
```shell
docker-compose up -d
```

После этого нужно запустить миграции в базе данных, сделать это можно так:
```shell
docker compose exec device-control-api sh -c './migrate_up.sh'

docker compose exec telemetry-api sh -c './migrate_up.sh'
```

После этого можно обращаться к системе через http://localhost:8000

Если нужно обновить образы в репозитории, в папке сервисов есть для этого скрипт [вот](device-control/build_and_push.sh) и [вот](telemetry/build_and_push.sh).
Нужно учесть, что для того, что бы запушить изменения в образах нужно иметь доступ, для этого нужно задать переменные окружения перед выполнением скрипта:
```shell
export GITHUB_USERNAME="<YOUR_GIHUB_USERNAME>"
export GITHUB_PAT="<YOUR_GITHUB_TOKEN>"
```
[Инструкция как получить токен.](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

Так же стоит обратить внимание, если залить образы в личный профиль гитхаба, то в [docker-compose](docker-compose.yaml) нужно поменять будет пути образов. 