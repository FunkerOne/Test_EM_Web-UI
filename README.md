# Задание 1: "E2E UI" тестирование 
Для тестирования был выбран сервис [Swag Labs](https://www.saucedemo.com/) 

> Интернет-магазин одежды и аксессуаров.

Тесты: 

[Раздел «Корзина»](tests/test_cart_page.py)
- Проверка успешного оформления заказа

---
### Перед работой с репозиторием требуется установить зависимости 
``` shell
pip3 install -r requirements.txt
```
### Запустить все тесты из директории tests
```shell
pytest tests --alluredir=allure_results
```
### Посмотреть отчет в веб версии пройденного прогона
```shell
allure serve allure_results
```