# Overview

This is my first rest api written in python using flask


## Database
sqLite is used. The database model consists of two tables:
* bands
* albums


Database model
| bands            | albums                |   
| ---------------- | --------------------- |
| id (primary key) | band_id (foreign key) |
| name             | name                  |
|                  | record_company        | 


## Packages used
* Flask, version: 1.1.2
* Flask-RESTful, version: 0.3.8

