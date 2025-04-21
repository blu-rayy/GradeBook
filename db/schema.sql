-- USERS
CREATE TABLE IF NOT EXISTS users (
    userID INTEGER PRIMARY KEY, AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    password VARCHAR(250) NOT NULL,
    school VARCHAR(250)
);

-- COURSE
CREATE TABLE IF NOT EXISTS course (
    courseID INTEGER PRIMARY KEY, AUTO_INCREMENT,
    course_title VARCHAR(500) NOT NULL,
    course_nickname VARCHAR(15) NOT NULL,
    course_code VARCHAR(15) NOT NULL,
    units VARCHAR(1) NOT NULL,
    section VARCHAR(15),
    linked_courseID INTEGER,
    FOREIGN KEY (linked_courseID) REFERENCES course(courseID)
);

-- SEMESTER
CREATE TABLE IF NOT EXISTS semester (
    semesterID INTEGER PRIMARY KEY, AUTO_INCREMENT,
    year NUMERIC(1) NOT NULL,
    term NUMERIC(1) NOT NULL,
    courseID INTEGER NOT NULL,
    FOREIGN KEY (courseID) REFERENCES course(courseID)
);

-- GRADES
CREATE TABLE IF NOT EXISTS grades (
    gradeID INTEGER PRIMARY KEY, AUTO_INCREMENT,
    category VARCHAR(8) NOT NULL,
    subcategory VARCHAR(50) NOT NULL,
    weight NUMERIC(5,2) NOT NULL,
    userID INTEGER NOT NULL,
    grade REAL,
    courseID INTEGER NOT NULL,
    component VARCHAR(3) NOT NULL CHECK (component IN ('LEC', 'LAB')),
    FOREIGN KEY (userID) REFERENCES users(userID),
    FOREIGN KEY (courseID) REFERENCES course(courseID)
);

-- Initialize sqlite_sequence only if it doesn’t exist
CREATE TABLE IF NOT EXISTS sqlite_sequence(name, seq);

-- Insert or update starting values if not already set
INSERT INTO sqlite_sequence (name, seq) 
    SELECT 'users', 99
    WHERE NOT EXISTS (SELECT 1 FROM sqlite_sequence WHERE name = 'users');

INSERT INTO sqlite_sequence (name, seq) 
    SELECT 'grades', 199
    WHERE NOT EXISTS (SELECT 1 FROM sqlite_sequence WHERE name = 'grades');

INSERT INTO sqlite_sequence (name, seq) 
    SELECT 'course', 399
    WHERE NOT EXISTS (SELECT 1 FROM sqlite_sequence WHERE name = 'course');

INSERT INTO sqlite_sequence (name, seq) 
    SELECT 'semester', 499
    WHERE NOT EXISTS (SELECT 1 FROM sqlite_sequence WHERE name = 'semester');
