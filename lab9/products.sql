CREATE DATABASE IF NOT EXISTS products;
USE products;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO products (name, price) VALUES
('Laptop HP Pavilion', 14500.00),
('Mouse Inalámbrico Logitech', 450.50),
('Teclado Mecánico RGB', 1200.00),
('Monitor 24 pulgadas', 3200.00);