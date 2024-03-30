-- Get all FeedbackReviews
SELECT * FROM Feedback_Reviews;

-- Get a specific Branch by branch_id
SELECT * FROM Branches WHERE branch_id = :branch_id;

-- Get BarInventory for a specific branch
SELECT * FROM Bar_Inventory WHERE branch_id = :branch_id;

-- Get Bartables for a specific branch ordered by table_id
SELECT * FROM Bartables WHERE branch_id = :branch_id ORDER BY table_id;

-- Create a new Order
INSERT INTO Orders (table_id, branch_id, product_name) VALUES (:table_id, :branch_id, :product_name);

-- Create a new OrderProduct
INSERT INTO OrderProduct (order_id, product_name, quantity, branch_id) VALUES (:order, :product_name, :quantity, :branch_id);

-- Get Orders for a specific branch and table
SELECT * FROM Orders WHERE branch_id = :branch_id AND table_id = :table_id;

-- Delete Orders for a specific table
DELETE FROM Orders WHERE table_id = :table_id;

-- Get Branches, Employees, Guesses, SecurityLogs, Reservations for a specific branch
SELECT * FROM Branches WHERE branch_id = :branch_id;
SELECT * FROM Employees WHERE branch_id = :branch_id;
SELECT * FROM Guesses WHERE branch_id = :branch_id;
SELECT * FROM SecurityLogs WHERE branch_id = :branch_id;
SELECT * FROM Reservations WHERE branch_id = :branch_id;

-- Get all Memberships
SELECT * FROM Membership;

-- Update an Order to mark it as completed
UPDATE Orders SET completed = True WHERE order_id = :order_id;

-- Create a new Reservation
INSERT INTO Reservations (branch, table, membership_id, reservation_time, number_of_guests) VALUES (:branch, :table, :membership_id, :reservation_time, :number_of_guests);

-- Update a Bartable to mark it as reserved
UPDATE Bartables SET table_status = True, start_time = :reservation_time WHERE table_id = :table_id;

-- Get Bartables for a specific branch that are not reserved ordered by table_id
SELECT * FROM Bartables WHERE branch_id = :branch_id AND table_status = False ORDER BY table_id;
