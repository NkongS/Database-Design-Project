-- Active: 1711567510462@@34.126.125.221@5432@postgres@public
DROP TABLE IF EXISTS Locations, Branches, Employees, Employee_Schedules, Bar_Inventory, Security_Logs, BarTables, Guesses, Membership, Feedback_Reviews, Reservations, Employee_Position, Orders, OrderProduct; 

CREATE TABLE Locations (
    location_ID    SERIAL PRIMARY KEY,
    address_no     VARCHAR(40),
    street_name    VARCHAR(30),
    city_name      VARCHAR(30) NOT NULL,
    province_name  VARCHAR(25),
    postal_code    VARCHAR(12),
    country_name   VARCHAR(25)
);

CREATE TABLE Employee_Position (
    position_ID    VARCHAR(10) PRIMARY KEY,
    position_name  VARCHAR(30),
    min_salary     INTEGER,
    max_salary     INTEGER
);

CREATE TABLE Employees (
    employee_ID    VARCHAR(10) PRIMARY KEY,
    position_ID    VARCHAR(10) REFERENCES Employee_Position(position_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    first_name     VARCHAR(30),
    last_name      VARCHAR(30),
    contact_info   NUMERIC(12),
    email          VARCHAR(45),
    salary         INTEGER,
    hire_date      DATE
);

CREATE TABLE Branches (
    branch_ID      SERIAL PRIMARY KEY,
    location_ID    INTEGER REFERENCES Locations(location_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    branch_name    VARCHAR(40),
    employee_ID    VARCHAR(10) REFERENCES Employees(employee_ID) ON UPDATE CASCADE ON DELETE CASCADE
);

--
ALTER TABLE Employees ADD COLUMN branch_ID INTEGER REFERENCES Branches(branch_ID) ON UPDATE CASCADE ON DELETE CASCADE; --add branch_ID as fk to Employees table
--

CREATE TABLE Employee_Schedules (
    schedule_ID    SERIAL PRIMARY KEY,
    branch_ID      INTEGER REFERENCES Branches(branch_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    employee_ID    VARCHAR(10) REFERENCES Employees(employee_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    shift_start    TIME,
    shift_end      TIME
);

CREATE TABLE Bar_Inventory (
    product_ID     SERIAL PRIMARY KEY,
    branch_ID      INTEGER REFERENCES Branches(branch_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    product_name   VARCHAR(30),
    quantity       INTEGER,
    price          INTEGER
);

CREATE TABLE Security_Logs (
    log_ID         SERIAL PRIMARY KEY,
    branch_ID      INTEGER REFERENCES Branches(branch_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    employee_ID    VARCHAR(10) REFERENCES Employees(employee_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    log_time       TIME,
    activity_log   BOOLEAN
);

CREATE TABLE BarTables (
    branch_ID      INTEGER REFERENCES Branches(branch_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    table_ID       VARCHAR(8) PRIMARY KEY,
    start_time     TIME,
    check_out_time TIME,
    table_status   BOOLEAN
);

CREATE TABLE Guesses (
    branch_ID          INTEGER,
    table_ID           VARCHAR(8),
    guess_first_name   VARCHAR(30),
    guess_last_name    VARCHAR(30),
    guess_band         VARCHAR(30),
    PRIMARY KEY (branch_ID, table_ID),
    FOREIGN KEY(branch_ID) REFERENCES Branches(branch_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(table_ID) REFERENCES BarTables(table_ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Membership (
    membership_id     VARCHAR(10) PRIMARY KEY,
    first_name        VARCHAR(30),
    second_name       VARCHAR(30),
    contact_info      NUMERIC(12),
    membership_status BOOLEAN
);

CREATE TABLE Feedback_Reviews (
    review_ID        SERIAL PRIMARY KEY,
    membership_id    VARCHAR(10) REFERENCES Membership(membership_id) ON UPDATE CASCADE ON DELETE CASCADE,
    rating           INTEGER,
    feedbacks        TEXT
);

CREATE TABLE Reservations (
    reservation_ID     SERIAL PRIMARY KEY,
    branch_ID          INTEGER REFERENCES Branches(branch_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    table_ID           VARCHAR(8) REFERENCES BarTables(table_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    membership_id      VARCHAR(10) REFERENCES Membership(membership_id) ON UPDATE CASCADE ON DELETE CASCADE,
    reservation_time   TIME,
    number_of_guests   INTEGER
);
--
ALTER TABLE BarTables ADD COLUMN reservation_ID INTEGER REFERENCES Reservations(reservation_ID) ON UPDATE CASCADE ON DELETE CASCADE; --add reservation_ID as fk to BarTables table
--

CREATE TABLE Orders (
    order_id        SERIAL PRIMARY KEY,
    branch_ID       INTEGER REFERENCES Branches(branch_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    item_id         INTEGER REFERENCES Bar_Inventory(product_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    table_id        VARCHAR(8) REFERENCES BarTables(table_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    completed       BOOLEAN DEFAULT FALSE,
);

CREATE TABLE OrderProduct (
    id SERIAL PRIMARY KEY,
    branch_ID       INTEGER REFERENCES Branches(branch_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    item_id         INTEGER REFERENCES Bar_Inventory(product_ID) ON UPDATE CASCADE ON DELETE CASCADE,
    order_id        INTEGER REFERENCES Orders(order_id) ON UPDATE CASCADE ON DELETE CASCADE,
    quantity        INTEGER
);

ALTER TABLE employees ADD COLUMN schedule_id INTEGER, ADD CONSTRAINT employees_schedule_id_fkey FOREIGN KEY (schedule_id) REFERENCES employee_schedules (schedule_id);
