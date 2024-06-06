# vulnerable_web_code
Run it on virtual machine
## Requirements to run code
To run app create virtual environment
python3 -m venv .venv

Activate virtual environment
source .venv/bin/activate

Install pip packages
pip install mysqlclient
pip install mysql-connector-python
pip install flask

and then run code
python3 main.py

##  Creation of flag for challenge 1
Create a new user for virtual machine which username is flag

## To make challenge 2 work:
You have to install mysql and then.
* Create user for mysql
CREATE USER 'testuser'@'localhost' IDENTIFIED WITH authentication_plugin BY 'testuser';
* Give access to that user
  GRANT ALL PRIVILEGES ON *.* TO 'testuser'@'localhost';
* Create database in mysql:
CREATE DATABASE webServer;
* Create table in database:
USE webServer;
CREATE TABLE users (username VARCHAR(30) NOT NULL, password VARCHAR(30) NOT NULL);

