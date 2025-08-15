# Café Fausse

## Overview

Café Fausse website is a responsive, full-stack web applicaion that provides information about the restaurant, displays the menu, allows customers to make table reservations, and showcases awards and customer testimonials. The project will consist of three main parts:

- **Database** hosted using PostgreSQL
- **Back-end** created using Python's Flask
- **Front-end** created in React (JavaScript)

## Database

For this app we are using SQL database in PostgreSQL. For it's creation we use 'pgAdmin 4' that provides GUI to manage our databases.
Steps to create a database:

- Create a Server Group
- Create a Server in the Server Group
- Create a Database in the server

After this we will create tables. SQL queries for that are in _cafe_fausse.sql_.
From the file we run queries from sections for creating tables and and setting restrictions.

Alternatively Flask app will create tables as it is started as there are table schemas defined in **modules.py**.

When tables are created we run INSERT statements for tables **categories** and **menu** that can be found in _cafe_fausse.sql_.

Database has been set up!

## Back-end

Back-end for our web application is built using Flask.

To start we create a virtual envrionment with command: `python -m venv .venv`
After creating environment we activate it with command: `.\.venv\Scripsts\activate`
Next step is to upgrade pip to the newest version: `python -m pip install --upgrade pip`

After the basics we can working with Flask.