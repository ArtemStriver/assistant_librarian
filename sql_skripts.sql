CREATE TABLE book (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(50),
  author VARCHAR(50),
  genre VARCHAR(50),
  book_count INT,
);

CREATE TABLE client (
  id INT PRIMARY KEY AUTO_INCREMENT,
  client_name VARCHAR(100),
  address VARCHAR(200),
  phone VARCHAR(50),
  visit_date DATE,
);

CREATE TABLE book_info (
  id INT PRIMARY KEY AUTO_INCREMENT,
  book_id int not null,
  client_id int not null,
  take_date DATE,
  return_date DATE,
  FOREIGN KEY (book_id)  REFERENCES book (id) ON DELETE CASCADE,
  FOREIGN KEY (client_id)  REFERENCES client (id) ON DELETE CASCADE,
);

INSERT INTO book (title, author, genre, book_count)
VALUES
    ('Война и мир', 'Толстой Л.Н.', 'Роман', 10),
    ('Анна Каренина', 'Толстой Л.Н.', 'Роман', 20),
    ('Идиот', 'Достоевский Ф.М.', 'Роман', 8),
    ('Записки из подполья', 'Достоевский Ф.М.', 'Рассказ', 12),
    ('Капитанская дочка', 'Пушкин А.С.', 'Рассказ', 9),
    ('Руслан и Людмила', 'Пушкин А.С.', 'Поэма', 43),
    ('Полное собрание стихотворений', 'Есенин С.А.', 'Стихи', 2);

INSERT INTO client(client_name, address, phone, visit_date) VALUES
	('Иванов Иван Иванович', 'г. Пермь, ул. Ленина, д. 55, кв. 4', '+7(999)888-88-88', '2024-02-29'),
	('Петров Петр Петрович', 'г. Пермь, ул. Луначарского, д. 109, кв. 7', '+7(999)888-88-87', '2024-02-29'),
	('Владов Владислав Владович', 'г. Пермь, ул. Екатерининская, д. 11, кв. 5', '+7(999)888-88-86', '2024-02-29'),
	('Кириллов Кирилл Кириллович', 'г. Пермь, ул. Куйбышева, д. 19, кв. 9', '+7(999)888-88-85', '2024-02-29');
