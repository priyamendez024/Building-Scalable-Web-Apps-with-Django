
# Chapter 4: PostgreSQL Deep Dive

# Example for creating a database and a table in PostgreSQL
CREATE DATABASE mydatabase;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
    