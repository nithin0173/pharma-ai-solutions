CREATE TABLE DrugInventory (
    DrugID INT PRIMARY KEY,
    DrugName VARCHAR(100),
    StockLevel INT,
    StorageTemperature VARCHAR(20),
    ExpiryDate DATE
);

INSERT INTO DrugInventory VALUES (101, 'Amlodipine', 50000, '25°C', '2027-12-01');
INSERT INTO DrugInventory VALUES (102, 'Metformin', 85000, '20°C', '2026-06-15');