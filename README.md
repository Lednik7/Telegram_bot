# Задача: Умный сервис прогноза погоды
**Уровень сложности: Задача со звездочкой**

Бот: @All_Weather_bot

**Проектирование сервиса:**

1) Для написания данного сервиса потребуются знания языка программирования Python и библиотек: pyowm 2.10.0(для получения информации о погоде), pyTelegramBotAPI 3.6.7(непосредственно для создания бота в Telegram). Чтобы запустить данного бота на удаленном сервере были использованы сервисы Github и Heroku.

2) В качетсве интерфейса взаимодейсвия был выброн чат-бот в Telegram.

3) Формат ответа: Данные о погоде, температуре, влажности, и скорости ветра, полученные с API подставляются в текстовый шаблон и отправляются в виде сообщений в зависимости от запроса пользователя.

Демонстрация работы сервиса доступна по ссылке: https://youtu.be/20j13q8m-d4

**Процесс работы сервиса:**

Сервис - чат-бот, который по заданному запросу пользователя, высылает ему ответ.

Данные приходят от пользователя через интерфейс мессенджера Telegram.

 → Создается запрос к API.

 → Полученный ответ из API обрабатывается программой и подставляется в шаблон.

 → Ответ отправляется.

**Инструкция к запуску:**

P.S. Из-за запрета Telegram в России, бота приходится запускать на удаленном сервере в другой стране.

P.S. Все токены от бота лежат в файле .gitignore

1) Создайте новый репозиторий на своем аккаунте Github.
2) Загрузите в него файлы Procfile, requirements.txt, telegram.py из моего репозитория.
3) Зарегистрируйтесь на Heroku и создайте новый проект.
4) Подключите созданный репозиторий Github к проекту на Heroku. Может попросить пароль от Github.
5) Во вкладке проекта "Deploy" найдите кнопку "Deploy Branch" и нажмите её. Дождитесь окончания процесса.
6) Далее переходим во вкладку проекта "Overview".
7) Находим кнопку синию кнопку "Configure Dynos" и жмем.
8) На новой страничке находим кноку карандаша и подключаем тариф $0.00.
9) На этом всё! Бот запущен на серверах Heroku. В случае ошибки вы можете нажать на кнопку "More"-"View logs" и получить логи ошибки.
