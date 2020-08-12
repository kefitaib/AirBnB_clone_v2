-- deletes database in your MySQL server if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
