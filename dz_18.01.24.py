import requests, lxml
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import mysql.connector
from Auth import db_host, db_user, db_password, db_name
import datetime


class JobParser:
    list_of_ocupation = []
    list_of_company = []
    list_of_place_work = []
    list_of_time = []

    def save_ocupation(self):
        try:
            url = 'https://realpython.github.io/fake-jobs/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            ocupation  = soup.find_all('h2')
            for i in ocupation:
                self.list_of_ocupation.append(i.text)
            print(self.list_of_ocupation)
        except HTTPError as er:
            print(f'Error is {er}')
        except Exception as r:
            print(f'Error {r}')


    def save_company(self):
        try:
            url = 'https://realpython.github.io/fake-jobs/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            company = soup.find_all('h3')
            for i in company:
                self.list_of_company.append(i.text)
            print(self.list_of_company)
        except HTTPError as er:
            print(f'Error is {er}')
        except Exception as r:
            print(f'Error {r}')


    def save_place_work(self):
        try:
            url = 'https://realpython.github.io/fake-jobs/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            place_work = soup.find_all('p', class_='location')
            for i in place_work:
                self.list_of_place_work.append(i.text.strip())
            print(self.list_of_place_work)
        except HTTPError as er:
            print(f'Error is {er}')
        except Exception as r:
            print(f'Error {r}')


    def save_time(self):
        try:
            url = 'https://realpython.github.io/fake-jobs/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            place_work = soup.find_all('p', class_='is-small has-text-grey')
            for i in place_work:
                self.list_of_time.append(i.text.strip())
            print(self.list_of_time)
        except HTTPError as er:
            print(f'Error is {er}')
        except Exception as r:
            print(f'Error {r}')


class MySQLHandler:
    def create_connection(db_host, db_user, db_password, db_name):
        mysql_connection = None
        try:
            mysql_connection = mysql.connector.connect(
                host=db_host,
                user=db_user,
                password=db_password,
                database=db_name
            )
            print('Connection successful')
        except mysql.connector.Error as error:
            print(f'Error is {error}')
        return mysql_connection

    def create_database(mysql_connection, db_name):
        try:
            cursor = mysql_connection.cursor()
            cursor.execute(f"""
                CREATE DATABASE IF NOT EXISTS {db_name}
                DEFAULT CHARACTER SET cp1251
                COLLATE cp1251_ukrainian_ci
            """)
            print(f'Database {db_name} created or already exists')
        except mysql.connector.Error as error:
            print(f'Error is {error}')

    def create_table(mysql_connection):
        try:
            cursor = mysql_connection.cursor()
            sql_script = """
                CREATE TABLE IF NOT EXISTS parsing (
                    users_id                INT AUTO_INCREMENT PRIMARY KEY,
                    посада                  VARCHAR(512) NOT NULL,
                    компанія                VARCHAR(32) NOT NULL,
                    місце_роботи            VARCHAR(32) NOT NULL,
                    дата_і_час              VARCHAR(32) NOT NULL,
                    час_створення           DATETIME NOT NULL
                );
            """
            cursor.execute(sql_script)
            print("Table created")
        except mysql.connector.Error as error:
            print(f'Error is {error}')

class JobToDatabase(MySQLHandler):
    def insert_data(self, mysql_connection, occupations, companies, places, times):
        try:
            cursor = mysql_connection.cursor()
            sql_script = """
            INSERT INTO parsing (посада, компанія, місце_роботи, дата_і_час, час_створення)
            VALUES (%s, %s, %s, %s, %s)
            """
            for i in range(len(occupations)):
                occupation = occupations[i].strip()
                company = companies[i].strip()
                place = places[i].strip()
                time = times[i].strip()
                cursor.execute(sql_script, (
                    occupation,
                    company,
                    place,
                    time,
                    datetime.datetime.now()
                ))
            mysql_connection.commit()
            print("Records inserted successfully")
        except mysql.connector.Error as error:
            print(f'Error is {error}')

if __name__ == '__main__':
    parsing = JobParser()
    parsing.save_ocupation()
    parsing.save_company()
    parsing.save_place_work()
    parsing.save_time()

    mysql_connection = MySQLHandler.create_connection(db_host, db_user, db_password, db_name)

    if mysql_connection:
        MySQLHandler.create_database(mysql_connection, db_name)
        mysql_connection = MySQLHandler.create_connection(db_host, db_user, db_password, db_name)
        MySQLHandler.create_table(mysql_connection)
        job_to_db = JobToDatabase()
        job_to_db.insert_data(
            mysql_connection,
            parsing.list_of_ocupation,
            parsing.list_of_company,
            parsing.list_of_place_work,
            parsing.list_of_time
        )

        mysql_connection.close()