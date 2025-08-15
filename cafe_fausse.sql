/* 
  --------------------------------------------------
  Queries for table creation
  --------------------------------------------------
*/

CREATE TABLE customers (
	customer_id INT NOT NULL,
	customer_name VARCHAR(50),
	email VARCHAR(75) UNIQUE NOT NULL,
	phone_number VARCHAR(15) NULL,
	newsletter_signup BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE reservations (
	reservation_id INT NOT NULL,
	customer_id INT NULL, 
	timeslot TIMESTAMP NOT NULL, -- format: 'YYYY-MM-DD HH:MM:SS'
	table_nr INT NOT NULL CHECK (table_nr BETWEEN 1 AND 30) -- from 1 to 30 (included)
);


-- Optional tables
CREATE TABLE categories (
	category_id INT NOT NULL,
	category_name VARCHAR(30) NOT NULL
);

CREATE TABLE menu (
	item_id INT NOT NULL,
	item_name VARCHAR(50) NOT NULL,
	item_description VARCHAR(250) NOT NULL,
	item_price decimal(5, 2) NOT NULL,
	item_category INT NULL
);



/* 
  --------------------------------------------------
  Queries for setting restrictions
  - primary keys
  - foreign keys
  --------------------------------------------------
*/

-- Set primary key for customers table
ALTER TABLE customers
ADD PRIMARY KEY (customer_id);

-- Set primary key for reservations table
ALTER TABLE reservations
ADD PRIMARY KEY (reservation_id);

-- Add foreign key in reservations to link with customer_id
ALTER TABLE reservations
ADD CONSTRAINT "foreign_key_reservation_customer_id"
FOREIGN KEY (customer_id)
REFERENCES customers (customer_id)
ON DELETE SET NULL
ON UPDATE CASCADE;


-- Add primary key in categories table
ALTER TABLE categories
ADD PRIMARY KEY (category_id);

-- Add primary key in menu table
ALTER TABLE menu
ADD PRIMARY KEY (item_id);

-- SET foreign key item_category to link to category_id
ALTER TABLE menu
ADD CONSTRAINT "foreign_key_item_category_id"
FOREIGN KEY (item_category)
REFERENCES categories (category_id)
ON DELETE SET NULL
ON UPDATE CASCADE;

/* 
  --------------------------------------------------
  Queries for deleting tables
  --------------------------------------------------
*/

DROP TABLE customers;

DROP TABLE reservations;

DROP TABLE categories;

DROP TABLE menu;

/* 
  --------------------------------------------------
  Queries for data insertion in tables
  --------------------------------------------------
*/

INSERT INTO customers (customer_id, customer_name, email, newsletter_signup)
VALUES (1, 'Reinis Janovskis', 'reinis.janovskis@hotmail.com', TRUE);

INSERT INTO customers (customer_id, customer_name, email)
VALUES (2, 'Johnny Bravo', 'jb23@google.com');

INSERT INTO reservations(reservation_id, customer_id, timeslot, table_nr)
VALUES (1, 1, '2025-08-16 17:30:00', 30);

INSERT INTO categories (category_id, category_name)
VALUES (1, 'starter');
INSERT INTO categories (category_id, category_name)
VALUES (2, 'main');
INSERT INTO categories (category_id, category_name)
VALUES (3, 'desert');
INSERT INTO categories (category_id, category_name)
VALUES (4, 'beverage');



INSERT INTO menu (item_id, item_name, item_description, item_price, item_category) VALUES
(1, 'Bruschetta', 'Fresh tomatoes, basil, olive oil, and toasted baguette slices', 8.50, 1),
(2, 'Caesar Salad', 'Crisp romaine with homemade Caesar dressing', 9.00, 1),
(3, 'Grilled Salmon', 'Served with lemon butter sauce and seasonal vegetables', 22.00, 2),
(4, 'Ribeye Steak', '12 oz prime cut with garlic mashed potatoes', 28.00, 2),
(5, 'Vegetable Risotto', 'Creamy Arborio rice with wild mushrooms', 18.00, 2),
(6, 'Tiramisu', 'Classic Italian dessert with mascarpone', 7.50, 3),
(7, 'Cheesecake', 'Creamy cheesecake with berry compote', 7.00, 3),
(8, 'Red Wine (Glass)', 'A selection of Italian reds', 10.00, 4),
(9, 'White Wine (Glass)', 'Crisp and refreshing', 9.00, 4),
(10, 'Craft Beer', 'Local artisan brews', 6.00, 4),
(11, 'Espresso', 'Strong and aromatic', 3.00, 4);





/* 
  --------------------------------------------------
  Queries for selecting data from tables
  --------------------------------------------------
*/

SELECT * FROM customers;

SELECT * FROM reservations;

SELECT * FROM categories;

SELECT * FROM menu;

SELECT menu.item_name, menu.item_description, menu.item_price, categories.category_name FROM menu
LEFT JOIN categories
ON menu.item_category = categories.category_id;