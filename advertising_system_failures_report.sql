-- Sirve para borrar las tablas si existen
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS campaigns;
DROP TABLE IF EXISTS events;

-- Sirve para crear las tablas
CREATE TABLE customers (
    id INTEGER,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE campaigns (
    id INTEGER,
    customer_id INTEGER,
    name TEXT
);

CREATE TABLE events (
    dt TEXT,
    campaign_id INTEGER,
    status TEXT
);

-- Sirve para agregar los datos de ejemplo
INSERT INTO customers VALUES
(1, 'Whitney', 'Ferrero'),
(2, 'Dickie', 'Romera');

INSERT INTO campaigns VALUES
(1, 1, 'Upton Group'),
(2, 1, 'Roob, Hudson and Rippin'),
(3, 1, 'McCullough, Rempel and Larson'),
(4, 1, 'Lang and Sons'),
(5, 2, 'Ruecker, Hand and Haley');

INSERT INTO events VALUES
('2021-12-02 13:52:00', 1, 'failure'),
('2021-12-02 08:17:48', 2, 'failure'),
('2021-12-02 08:18:17', 2, 'failure'),
('2021-12-01 11:55:32', 3, 'failure'),
('2021-12-01 06:53:16', 4, 'failure'),
('2021-12-02 04:51:09', 4, 'failure'),
('2021-12-01 06:34:04', 5, 'failure'),
('2021-12-02 03:21:18', 5, 'failure'),
('2021-12-01 03:18:24', 5, 'failure'),
('2021-12-02 15:32:37', 1, 'success'),
('2021-12-01 04:23:20', 1, 'success'),
('2021-12-02 06:53:24', 1, 'success'),
('2021-12-02 08:01:02', 2, 'success'),
('2021-12-01 15:57:19', 2, 'success'),
('2021-12-02 16:14:34', 3, 'success'),
('2021-12-02 21:56:38', 3, 'success'),
('2021-12-01 05:54:43', 4, 'success'),
('2021-12-02 17:56:45', 4, 'success'),
('2021-12-02 11:56:50', 4, 'success'),
('2021-12-02 06:08:20', 5, 'success');

-- Consulta que muestra los clientes con más de 3 fallas
-- Select sirve para seleccionar columnas de una tabla
SELECT
-- Concatena el nombre y apellido del cliente
  cu.first_name || ' ' || cu.last_name AS customer,
-- Cuenta el número de fallas
  COUNT(*) AS failures
FROM customers AS cu
-- Une las tablas customers y campaigns
JOIN campaigns ca ON ca.customer_id = cu.id
-- Une las tablas campaigns y events
JOIN events e ON e.campaign_id = ca.id
-- Filtra los eventos con status 'failure'  
WHERE e.status = 'failure'
-- Agrupa los resultados por cliente
GROUP BY cu.id, cu.first_name, cu.last_name
-- Filtra los clientes con más de 3 fallas
HAVING COUNT(*) > 3
-- Ordena los resultados por número de fallas
ORDER BY failures DESC;
