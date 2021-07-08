DELETE SCHEMA 'Bookish';
CREATE SCHEMA 'Bookish';

DELETE TABLE 'BookInfo'
CREATE TABLE 'BookInfo' (
    'isbn' VARCHAR(13) NOT NULL,
    'title' varchar(50) NOT NULL,
    'authorName' varchar(50) NOT NULL,
    'authorSurname' varchar(50) NOT NULL,
     PRIMARY KEY ('isbn')
);

DELETE TABLE 'Book'
CREATE TABLE 'Book' (
    'id' int(11) NOT NULL AUTO_INCREMENT,
    'isbn' VARCHAR(13) NOT NULL,
    'status' ENUM('available', 'borrowed', 'deleted') NOT NULL,
    'condition' ENUM('new', 'used', 'bad') NOT NULL,
    PRIMARY KEY ('id'),
    FOREIGN KEY ('isbn') REFERENCES  BookInfo('isbn')
    );

DELETE TABLE 'Member'
CREATE TABLE 'Member' (
    'id' int(11) NOT NULL AUTO_INCREMENT,
    'name' varchar(50) NOT NULL,
    'surname' varchar(50) NOT NULL,
    PRIMARY KEY ('id')
    );

DELETE TABLE 'Borrowed'
CREATE TABLE 'Borrowed' (
    'bookId' int(11) NOT NULL,
    'memberId' int(11) NOT NULL,
    'dueDate' DATE NOT NULL,
    'returned' BOOLEAN NOT NULL,
    PRIMARY KEY ('bookId', 'memberId'),
    FOREIGN KEY ('bookId') REFERENCES  Book('id'),
    FOREIGN KEY ('isbn') REFERENCES  BookInfo('isbn')
    );

DELETE TABLE 'Borrowed'
CREATE TABLE 'Borrowed' (
    'bookId' int(11) NOT NULL,
    'memberId' int(11) NOT NULL,
    'reason' VARCHAR(50),
    PRIMARY KEY ('bookId', 'memberId'),
    FOREIGN KEY ('bookId') REFERENCES  Book('id'),
    FOREIGN KEY ('isbn') REFERENCES  BookInfo('isbn')
    );


