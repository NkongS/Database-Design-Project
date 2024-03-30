--These query were translated from the django code to postgreSQL code so there might be some errors

-- Get all FeedbackReviews
SELECT * FROM Feedback_Reviews;

-- Create a new FeedbackReview
INSERT INTO Feedback_Reviews(membership_id, rating, feedbacks) VALUES (:membership_id, :rating, :feedbacks);

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

-- Update an Order to mark it as completed
UPDATE Orders SET completed = TRUE WHERE order_id = :order_id;

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

-- Create a new Reservation
INSERT INTO Reservations (branch_id, table_id, membership_id, reservation_time, number_of_guests) VALUES (:branch, :table, :membership_id, :reservation_time, :number_of_guests);

-- Update a Bartable to mark it as reserved
UPDATE Bartables SET table_status = True, start_time = :reservation_time WHERE table_id = :table_id;

-- Get Bartables for a specific branch that are not reserved ordered by table_id
SELECT * FROM Bartables WHERE branch_id = :branch_id AND table_status = False ORDER BY table_id;

INSERT INTO Membership (membership_id, first_name, second_name, contact_info, membership_status) VALUES (:membership_id, :first_name, :second_name, :contact_info, :membership_status);

-- Trigger to update inventory's item quantity when an order is completed
CREATE OR REPLACE FUNCTION update_inventory_after_order_completed() RETURNS TRIGGER AS $$
DECLARE
    order_items CURSOR FOR SELECT * FROM OrderProduct WHERE order_id = NEW.order_id;
    item RECORD;
    product_in_inventory RECORD;
BEGIN
    IF NEW.completed THEN
        FOR item IN order_items LOOP
            SELECT * INTO product_in_inventory FROM Bar_Inventory WHERE product_id = item.product_id;
            UPDATE Bar_Inventory SET quantity = product_in_inventory.quantity - item.quantity WHERE product_id = item.product_id;
        END LOOP;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_inventory_after_order_completed_trigger
AFTER INSERT OR UPDATE ON Orders
FOR EACH ROW EXECUTE PROCEDURE update_inventory_after_order_completed();
