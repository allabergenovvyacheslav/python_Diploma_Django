## Дипломная работа по теме: Анализ и сравнение написания web-приложений с использованием разных фреймворков.
### Дипломную работу выполнил Аллабергенов Вячеслав

Выбор данной темы обусловлен её актуальностью, высокому спросу на рынке ит-услуг, моей личной заинтересованности и желании углубленно изучить данную тему.
В процессе принятия решения какими фреймворками воспользоваться для работы, мой выбор пал на aiogram, FastAPI, и конечно Django.
Целью работы было создание приложения для работы с товарами, в частности демонстрация товара, описание, цена и краткий экскурс в деятельность компании.
При выполнении работы приобретен навык подключения к встраиваемой СУБД  - SQLite, отработана практика по созданию и поддержке таблиц и содержащихся в них данных.
В процессе работы приобретены навыки по работе с сторонними библиотеками, такими как sqlalchemy, pydantic, os, pillow, numpy и др.
Применена на практике работа с шаблонизатором Jinja2, Django HTML, опробован в работе язык программирования для работы с реляционными базами данных - SQL.
В целом пройден значительный путь к дальнейшей самостоятельной деятельности с намечен ряд задач для дальнейшего обучения и развития в качестве Python разработчика.

## Обзор фреймворков для разработки ВЭБ-приложений

## Фреймворк 
Фреймворк — это надстройка над языком программирования, которая упрощает разработку. Внутри фреймворка собрано много готовых конструкций, которые программисту не нужно делать самому — вместо этого он использует команды фреймворка и сразу получает результат. Можно представить, что фреймворк — это набор полуфабрикатов, из которых можно приготовить блюдо.

### Aiogram

Aiogram — это высокоуровневая асинхронная библиотека для Telegram Bot API. Она позволяет реализовывать ботов, которые могут работать параллельно с несколькими пользователями, не ожидая ответа от каждого из них.
Некоторые преимущества библиотеки:
<li>интуитивно понятный интерфейс</li>
<li>минимизация необходимости глубокого погружения в детали реализации Telegram API</li>
<li>сосредоточенность на логике взаимодействия бота с пользователем.</li>
Aiogram предлагает множество инструментов и полный доступ к Telegram API для работы с сообщениями, клавиатурой, медиафайлами и другими функциями.
Библиотека написана на Python с использованием asyncio и aiohttp. Последняя версия, выпущенная 18 сентября 2024 года, — 3.13.1.
В своей работе я пользовался версией 2.25

### FastAPI

FastAPI — это современный и высокопроизводительный веб-фреймворк для создания API на языке программирования Python. Он был запущен в 2018 году и разрабатывался как простой и удобный инструмент для ускорения разработки и уменьшения количества шаблонного кода. Еще стоит упомянуть, что FastAPI — это микрофреймворк, в котором акцентирование идет на простоту использования и производительность.
Некоторые особенности FastAPI:
<li>высокая производительность. Достигается путём использования асинхронных функций — обрабатывается сразу несколько запросов.</li>
<li>атоматическая документация для API. Упрощает разработку, тестирование, взаимодействие с клиентами и другими разработчиками.</li>
<li>встроенная валидация. Позволяет избежать ошибок и писать код более компактно.</li>
<li>поддержка популярных библиотек. Например, SQLAlchemy, JWT, pytest и многие другие.</li>

### Django

Django — это фреймворк для быстрой разработки сайтов и приложений на Python. Это набор готовых инструментов и функций, который позволяет реализовывать на Python сайты и приложения, работающие в браузере, быстрее и проще, чем писать весь код с нуля. Ну и конечно тут стоит отметить, Django — это мега-фреймворк, у которого большое количество возможностей.
Основные возможности Django:
<li>Встроенный веб-сервер для обработки запросов от пользователей к веб-сервису.</li>
<li>Механизмы авторизации пользователей.</li> 
<li>Подключение и работа с базами данных. </li>
<li>Шаблоны страниц и простых веб-интерфейсов. </li>
<li>Система кэширования для увеличения скорости загрузки и открытия страниц через браузеры, внешние клиенты или приложения.</li> 
<li>Административный интерфейс для управления контентом сервиса — наполнения, изменения, обновления используемых данных. </li>
Django работает по модели MVT — Model-View-Template, она разделяет логику работы сайта, внешний вид страниц и реакции на действия пользователей.
Сейчас на Django работает много популярных проектов, например:
YouTube;
Google (для вывода результатов по шаблону);
Dropbox;
Quora;
Mozilla;
Spotify;
Reddit.
Django можно использовать везде, где есть большая база данных и много пользователей.




















