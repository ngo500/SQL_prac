-- create a table
CREATE TABLE Instructor (
  ins_id int PRIMARY KEY NOT NULL,
  lastname varchar(255) NOT NULL,
  firstname varchar(255),
  city varchar(255),
  country char(2)
);

-- add data to table
INSERT INTO Instructor (ins_id, lastname, firstname, city, country)
VALUES (1, 'Ahuja', 'Rav', 'Toronto', 'CA'), 
(2, 'Chong', 'Raul', 'Toronto', 'CA'), 
(3, 'Vasudevan', 'Hima', 'Chicago', 'US');

-- view starting table
SELECT * FROM Instructor;

-- insert Instructor to table
INSERT INTO Instructor (ins_id, lastname, firstname, city, country)
VALUES(4, 'Saha', 'Sandip', 'Edmonton', 'CA');

-- insert 2 Instructor to table
INSERT INTO Instructor(ins_id, lastname, firstname, city, country)
VALUES(5, 'Doe', 'John', 'Sydney', 'AU'),
(6, 'Doe', 'Jane', 'Dhaka', 'BD');

-- insert Instructor to table
INSERT INTO Instructor (ins_id, lastname, firstname, city, country)
VALUES(7, 'Cangiano', 'Antonio', 'Vancouver', 'CA');

-- insert 2 Instructor to table
INSERT INTO Instructor (ins_id, lastname, firstname, city, country)
VALUES(8, 'Ryan', 'Steve', 'Barlby', 'GB'),
(9, 'Sannareddy', 'Ramesh', 'Hyderabad', 'IN');

-- view table after inserts
SELECT * FROM Instructor;

-- update Instructor, with firstname "Sandip", city to "Toronto"
UPDATE Instructor
SET city = 'Toronto'
WHERE firstname = "Sandip";

-- update Instructor, with id 5, city to "Dubai" and country to "AE"
UPDATE Instructor
SET city = 'Dubai', country = 'AE'
WHERE ins_id = 5;

-- update Instructor, with id 1, city to "Markham"
UPDATE Instructor
SET city = 'Markham'
WHERE ins_id = 1;

-- update Instructor, with id 4, city to "Dhaka" and country to "BD"
UPDATE Instructor
SET city = 'Dhaka', country = 'BD'
WHERE ins_id = 4;

-- view table after updates
SELECT * FROM Instructor;

-- delete Instructor, with id 6
DELETE FROM Instructor
WHERE ins_id = 6;

-- delete Instructor, where firstname 'Hima'
DELETE FROM Instructor
WHERE firstname = 'Hima';

-- view table after deletes
SELECT * FROM Instructor;
