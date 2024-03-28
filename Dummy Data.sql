-- Inserting Locations table data
INSERT INTO Locations (address_no, street_name, city_name, province_name, postal_code, country_name) VALUES
('123', 'Main St', 'City1', 'Province1', '12345', 'Country1'),
('456', 'Second Ave', 'City2', 'Province2', '67890', 'Country2');

-- Inserting Branches table data
INSERT INTO Employee_Position (position_ID, position_name, min_salary, max_salary) VALUES
('POS001', 'Manager', 50000, 80000),
('POS002', 'Bartender', 30000, 50000),
('POS003', 'Waiter', 25000, 40000),
('POS004', 'Chef', 40000, 60000),
('POS005', 'Security Guard', 28000, 35000);

-- Inserting Employees table data
INSERT INTO Employees (employee_ID, position_ID, first_name, last_name, contact_info, email, salary, hire_date) VALUES
('EMP001', 'POS001', 'John', 'Doe', 1234567890, 'john.doe@gmail.com', 60000, '2023-01-15'),
('EMP002', 'POS002', 'Jane', 'Smith', 9876543210, 'jane.smith@gmail.com', 35000, '2023-02-20'),
('EMP003', 'POS003', 'Michael', 'Johnson', 5551234567, 'michael.j@gmail.com', 28000, '2023-03-10'),
('EMP004', 'POS004', 'Sarah', 'Johnson', 5559876543, 'sarah.j@gmail.com', 45000, '2023-04-05'),
('EMP005', 'POS005', 'Robert', 'Williams', 4442223333, 'robert.w@gmail.com', 32000, '2023-05-10'),
('EMP006', 'POS001', 'Jaden', 'Lee', 1122334455, 'jaden.lee@gmail.com', 70000, '2023-01-15'),
('EMP007', 'POS002', 'Emily', 'Brown', 9988776655, 'emily.b@gmail.com', 38000, '2023-02-20'),
('EMP008', 'POS003', 'David', 'Martinez', 5551234567, 'dav.mar@gmail.com', 26000, '2023-03-10'),
('EMP009', 'POS004', 'Sophia', 'Garcia', 5559876543, 'gar.sop@gmail.com', 50000, '2023-04-05'),
('EMP010', 'POS005', 'Ethan', 'Lopez', 4442223333, 'lop123@gmail.com', 30000, '2023-05-10');


-- Inserting Branches table data
INSERT INTO Branches (location_ID, branch_name, employee_ID) VALUES
(1, 'Branch1', 'EMP001'),
(2, 'Branch2', 'EMP006');

UPDATE Employees SET branch_ID = 1 WHERE employee_ID IN ('EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005');
UPDATE Employees SET branch_ID = 2 WHERE employee_ID IN ('EMP006', 'EMP007', 'EMP008', 'EMP009', 'EMP010');

-- Inserting Employee_Schedules table data
INSERT INTO Employee_Schedules (branch_ID, employee_ID, shift_start, shift_end) VALUES 
(1, 'EMP001', '16:30:00', '01:00:00'),
(1, 'EMP002', '17:30:00', '01:00:00'),
(1, 'EMP003', '17:30:00', '01:00:00'),
(1, 'EMP004', '17:30:00', '01:00:00'),
(1, 'EMP005', '17:00:00', '21:00:00'),
(2, 'EMP006', '16:30:00', '01:00:00'),
(2, 'EMP007', '17:30:00', '01:00:00'),
(2, 'EMP008', '17:30:00', '01:00:00'),
(2, 'EMP009', '17:30:00', '01:00:00'),
(2, 'EMP010', '17:00:00', '21:00:00');

-- Inserting Bar_Inventory table data
INSERT INTO Bar_Inventory (branch_ID, product_name, quantity, price) VALUES 
(1, 'Beer', 100, 5),
(1, 'Wine', 50, 10),
(1, 'Whiskey', 20, 15),
(1, 'Vodka', 30, 12),
(1, 'Rum', 40, 8),
(2, 'Beer', 100, 5),
(2, 'Wine', 50, 10),
(2, 'Whiskey', 20, 15),
(2, 'Vodka', 30, 12),
(2, 'Rum', 40, 8);

-- Inserting Security_Logs table data
INSERT INTO Security_Logs (branch_ID, employee_ID, log_time, activity_log) VALUES 
(1, 'EMP001', '16:00:00', TRUE),
(1, 'EMP002', '17:29:00', TRUE),
(1, 'EMP003', '17:29:00', TRUE),
(1, 'EMP004', '17:00:00', TRUE),
(1, 'EMP005', '16:50:00', TRUE),
(2, 'EMP006', '16:00:00', TRUE),
(2, 'EMP007', '17:29:00', TRUE),
(2, 'EMP008', '17:29:00', TRUE),
(2, 'EMP009', '17:00:00', TRUE),
(2, 'EMP010', '16:50:00', TRUE);

-- Inserting BarTables table data
INSERT INTO BarTables (branch_ID, table_ID, start_time, table_status) VALUES
(1, 'B01T0001', '17:00:00', TRUE),
(1, 'B01T0002', '18:00:00', TRUE),
(1, 'B01T0003', '19:00:00', FALSE),
(2, 'B02T0001', '17:30:00', TRUE),
(2, 'B02T0002', '19:00:00', TRUE),
(2, 'B02T0003', '19:00:00', FALSE);

-- Inserting Guesses table data
INSERT INTO Guesses (branch_ID, table_ID, guess_first_name, guess_last_name, guess_band) VALUES 
(1, 'B01T0001', 'John', 'Smith', 'The Band'),
(2, 'B02T0001', 'Jane', 'Doe', 'Solo Artist');


-- Inserting Membership table data
INSERT INTO Membership (membership_id, first_name, second_name, contact_info, membership_status) VALUES
('M00', 'Admin', 'Table', 0000000000, TRUE),
('M01', 'Member1', 'Lastname1', 1234567890, TRUE),
('M02', 'Member2', 'Lastname2', 0987654321, TRUE);

-- Inserting Reservation table data
INSERT INTO Reservations (branch_ID, table_ID, membership_id, reservation_time, number_of_guests) VALUES
(1, 'B01T0001', 'M00', '17:00:00', 5),
(2, 'B02T0001', 'M00', '17:00:00', 5),
(1, 'B01T0002', 'M01', '18:00:00', 8),
(2, 'B02T0002', 'M02', '19:00:00', 13);

UPDATE BarTables SET reservation_ID = 1 WHERE table_ID = 'B01T0001';
UPDATE BarTables SET reservation_ID = 2 WHERE table_ID = 'B02T0001';
UPDATE BarTables SET reservation_ID = 3 WHERE table_ID = 'B01T0002';
UPDATE BarTables SET reservation_ID = 4 WHERE table_ID = 'B02T0002';
