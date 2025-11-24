# DEV1002 - Databases & Servers
## Assessment 3 - Web API Server

# Inventory Management ERD
- Each Product belongs to one Category
- Product can be supplied by multiple Suppliers
- Junction table, Product_Supplier, tracks supply price and last supplied date

![ERD](images/Inventory_Management_ERD.png)

## Database
DATABASE_URL="postgresql+psycopg2://username:password@host:port/database_name
1. create a database
- Connect to postgres
```bash
sudo -u postgres psql
```
- create a database
```
CREATE DATABASE inventory_db;
```
- see all database in the system -> \l
- see all users int he system -> \du
- connect to database \c inventory_db
- see all tables -> \dt

- create user
```
CREATE USER inventory_dev PASSWORD '123456';
```
- grant privileges to database
```
GRANT ALL PRIVILEGES ON DATABASE inventory_db TO inventory_dev;
```
- grant privileges to schema, (to find schemas name \dn)
```
GRANT ALL PRIVILEGES ON SCHEMA public TO inventory_dev;
```
- 
