DROP SCHEMA Bookish;
CREATE SCHEMA Bookish;

DROP TABLE DeletedReasons;
DROP TABLE Borrowed;
DROP TABLE Member;
DROP TABLE Book;
DROP TABLE BookInfo;

CREATE TABLE BookInfo (
                          isbn VARCHAR(17) NOT NULL,
                          title varchar(50) NOT NULL,
                          authorName varchar(50) NOT NULL,
                          authorSurname varchar(50) NOT NULL,
                          PRIMARY KEY (isbn)
);

CREATE TABLE Book (
                      id INT NOT NULL AUTO_INCREMENT,
                      isbn VARCHAR(13) NOT NULL,
                      bookStatus ENUM('available', 'borrowed', 'deleted') NOT NULL,
                      bookCondition ENUM('new', 'used', 'bad') NOT NULL,
                      PRIMARY KEY (id),
                      FOREIGN KEY (isbn) REFERENCES  BookInfo(isbn)
);

CREATE TABLE Member (
                        id INT NOT NULL AUTO_INCREMENT,
                        name varchar(50) NOT NULL,
                        surname varchar(50) NOT NULL,
                        PRIMARY KEY (id)
);

CREATE TABLE Borrowed (
                          bookId INT NOT NULL,
                          memberId INT NOT NULL,
                          dueDate DATE NOT NULL,
                          returned BOOLEAN NOT NULL,
                          PRIMARY KEY (bookId, memberId),
                          FOREIGN KEY (bookId) REFERENCES  Book(id),
                          FOREIGN KEY (memberId) REFERENCES Member(id)
);

CREATE TABLE DeletedReasons (
                                bookId INT NOT NULL,
                                memberId INT NOT NULL,
                                reason VARCHAR(50),
                                PRIMARY KEY (bookId, memberId),
                                FOREIGN KEY (bookId) REFERENCES  Book(id),
                                FOREIGN KEY (memberId) REFERENCES Member(id)
);


