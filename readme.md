### DEV1002 - Databases & Servers-  Assessment 3 - Web API Server

# Inventory Management Web Server

## Project Overview
This project is a Flask-based inventory management web server built in Python. It provides structured endpoints for managing products, suppliers, and categories, with a relational database backend to ensure data integrity and flexible querying.

## Entity Relationship Diagram (ERD)
The database schema includes four core entities:
![ERD](images/Inventory_Management_ERD.png)

- **Category**
  - `category_id` (Primary Key)
  - `name`
  - `description`

- **Product**
  - `product_id` (Primary Key)
  - `name`
  - `description`
  - `quantity`
  - `unit_price`
  - `category_id` (Foreign Key → Category)

- **Supplier**
  - `supplier_id` (Primary Key)
  - `name`
  - `contact_email`
  - `phone_number`

- **Product_Supplier** (junction table)
  - `product_id` (Primary Key, Foreign Key → Product)
  - `supplier_id` (Primary Key, Foreign Key → Supplier)
  - `supply_price`
  - `last_supplied_date`

**Relationships:**
- Each product belongs to one category.
- A product can be supplied by multiple suppliers.
- The `Product_Supplier` table tracks supply price and last supplied date for each product-supplier pair.

### Database System: PostgreSQL
PostgreSQL was selected as the database system for this project due to its robustness, flexibility, and alignment with course instruction. Beyond familiarity, PostgreSQL offers:

- **Strong relational integrity** – Ideal for enforcing foreign key constraints and many-to-many relationships.
- **Advanced querying capabilities** – Supports complex joins, subqueries, and indexing strategies.
- **JSON support** – Allows hybrid relational-document storage if needed for future extensions.
- **Open-source and production-ready** – Widely adopted in enterprise environments.

### Comparison with Other Database Systems

| Database      | Type        | Pros                                         | Cons                                       |
|---------------|-------------|----------------------------------------------|--------------------------------------------|
| **PostgreSQL**| Relational  | ACID-compliant, powerful SQL, strong FK support | Slightly heavier setup than SQLite         |
| **MySQL**     | Relational  | Fast reads, easy replication                 | Weaker standards compliance, limited JSON  |
| **MongoDB**   | NoSQL       | Flexible schema, fast for unstructured data  | No joins, poor fit for relational models   |
| **SQLite**    | Relational  | Lightweight, zero config                     | Not ideal for concurrent or large-scale use|

PostgreSQL strikes the right balance between structure and scalability, making it well-suited for this inventory management system.

## Peer's Feedback and Response

As part of the planning stage, I sought feedback from two peers to refine the ERD and database design. Their insights helped improve the accuracy and robustness of the schema.

### Feedback from Amelia
> *"I really like how your ERD is clear and easy to read, and I like how you have included those dot points underneath to explain the relationships. I also think this is a cool idea because it could be used by many different businesses (as in, it's more general and not fixed to a specific theme).  
> My feedback is:  
> The connectors to the junction table (Product_Supplier) need to be flipped, i.e., the 'one' connections should be on the Product and Supplier sides, and the 'many' connections should be on the Product_Supplier side.  
> The connections from Product and Supplier to Product_Supplier shouldn't be optional. A row in the Product_Supplier table can only exist if it has both a Product AND a Supplier, as they're both part of the composite Primary Key."*

**Response:**  
I corrected the connectors to properly reflect the one-to-many relationship between Product/Supplier and Product_Supplier. I also ensured that the connections are mandatory, since each row in the junction table requires both a Product and a Supplier.

---

### Feedback from Courtney
> *"The way you handled the many-to-many relationship between Products and Suppliers works really well, and the junction table keeps everything easy to understand. One small improvement could be adjusting the cardinality between Category and Product so it clearly shows that every product must belong to a category. You might also think about adding unique constraints to fields like category.name or supplier.contact_email to avoid duplicates and keep the data cleaner."*

**Response:**  
I updated the cardinality between Category and Product to show that every product must belong to a category. Additionally, I added unique constraints to `category.name` and `supplier.contact_email` to prevent duplicate entries and maintain data integrity.

---

### Justification
Both sets of feedback were highly valuable in strengthening the ERD and database design:

- Amelia’s feedback ensured the **accuracy of relationships** in the junction table, preventing misinterpretation of the many-to-many structure.  
- Courtney’s feedback improved **data integrity and clarity**, ensuring that products are always tied to a category and that duplicate records are avoided.  

By implementing these changes, the ERD now better reflects real-world inventory management requirements and enforces stricter relational rules, making the system more reliable and scalable.




# Inventory Management ERD
- Each Product belongs to one Category
- Product can be supplied by multiple Suppliers
- Junction table, Product_Supplier, tracks supply price and last supplied date

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
