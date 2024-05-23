-- Crea una tabla de ejemplo
DROP TABLE sample_table;
CREATE TABLE sample_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO sample_table (name) VALUES ('Alice');
INSERT INTO sample_table (name) VALUES ('Bob');
INSERT INTO sample_table (name) VALUES ('Charlie');
INSERT INTO sample_table (name) VALUES ('David');
INSERT INTO sample_table (name) VALUES ('Eve');
