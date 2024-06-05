# vulnerable_web_code

To run app create virtual environment
python3 -m venv .venv

Activate virtual environment
source .venv/bin/activate

Install pip packages
pip install mysqlclient
pip install mysql-connector-python
pip install flask


Create database in mysql:
CREATE USER 'testuser'@'localhost' IDENTIFIED WITH authentication_plugin BY 'testuser';
CREATE DATABASE webServer;
USE webServer;
CREATE TABLE users (username VARCHAR(30) NOT NULL, password VARCHAR(30) NOT NULL);

