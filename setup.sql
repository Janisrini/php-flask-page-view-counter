CREATE DATABASE IF NOT EXISTS page_counter;
USE page_counter;

CREATE TABLE IF NOT EXISTS counter (
    id INT AUTO_INCREMENT PRIMARY KEY,
    page_name VARCHAR(255) UNIQUE,
    view_count INT DEFAULT 0
);

INSERT INTO counter (page_name, view_count)
VALUES ('home', 0)
ON DUPLICATE KEY UPDATE view_count = view_count;
