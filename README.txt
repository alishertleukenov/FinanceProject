superuser login: admin
superuser password: alisher
Python 3.12.0
django 3.2.13
--------------------------------------------------------------
1. Откройте CMD
2. Введите в консоль git clone https://github.com/alishertleukenov/FinanceProject.git
3. Перейдите в папку \finance-bank\finance
4. Введите команду docker-compose up --build
5. После того как запустится, в браузере перейдите по адресу 127.0.0.1:8000/
	если выводится ошибка, пропишите в командную строку 
	docker-compose run web python manage.py migrate
	docker exec -i finance-db-1 psql -U postgres < dump.sql

6. Чтобы зайти в админ панель, пропишите адрес 127.0.0.1:8000/admin
7. Login: admin Password: alisher