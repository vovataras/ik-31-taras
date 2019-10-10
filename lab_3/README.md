# Lab_3: Вступ до моніторингу.

1. Ініціалізовую середовище pipenv та встановлюю необхідні пакети:
    ```
    pipenv --python 3.7
    pipenv install django
    ```
2. За допомогою Django Framework створюю заготовку проекту. Для зручності винношу всі створені файли на один рівень вище:
    ```
    pipenv run django-admin startproject web_site
   
    mv web_site/web_site/* web_site/
    mv web_site/manage.py ./
    ```
3. Переконуюсь що все встановилось правильно і можна запустити Django сервер. Виконую команду вказану нижче та переходжу за посиланням яке вивелось у консолі:
    ```
    pipenv run python manage.py runserver
    ```
    ![django server](images/lab_3_1.png)
4. Зупиняю сервер виконавши переривання Ctrl+C. Створюю коміт із базовим темплейтом сайту.