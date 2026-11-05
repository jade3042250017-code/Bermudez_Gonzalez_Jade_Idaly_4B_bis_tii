CREATE DATABASE IF NOT EXISTS login_system_db;
USE login_system_db;

CREATE TABLE IF NOT EXISTS users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    passw VARCHAR(50) NOT NULL,
    nombre VARCHAR(100) NOT NULL
);

INSERT INTO users (username, passw, nombre) VALUES ('Bermudez', '6767', 'jade');

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0
);

INSERT INTO products (nombre, descripcion, precio, stock) VALUES
('Laptop HP', 'Laptop 15 pulgadas', 750.00, 10),
('Mouse Inalámbrico', 'Mouse óptico', 15.50, 50);