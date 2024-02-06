--------------------------------------------------
-- Section expenses_table
CREATE TABLE expenses(
    expenses_id SERIAL PRIMARY KEY,
    expenses_name VARCHAR (50) UNIQUE NOT NULL,
    expenses_single_expense SMALLINT NOT NULL,
    expenses_frequency TEXT NOT NULL,
    expenses_first_payment_date date NOT NULL,
    expenses_last_payment_date date NOT NULL,
    expenses_category TEXT NOT NULL
);

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category) 
VALUES('Husleje',4000,'1','2024-01-01','9999-01-01','Bolig/Sommerhus');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('Kviknet',279,'1','2024-01-01','9999-01-01','Bolig/Sommerhus');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('Alka, indboforsikring',315,'1','2024-01-01','9999-01-01','Bolig/Sommerhus');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('Dagligvarer', 4000,'1','2024-01-01','9999-01-01','Bolig/Sommerhus');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('Tryg, forsikring', 382,'1','2024-01-01','9999-01-01','Bil');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('Grøn ejerafgift', 1040,'6','2024-01-01','9999-01-01)','Bil');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('Falck', 68,'1','2024-01-01','2024-02-01','Bil');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('FDM', 73,'12','2024-03-01','9999-02-01','Bil');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('FTF-A, A-kasse', 1104,'3','2024-01-01','9999-01-01','Øvrige omkostninger');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('CBB, Telefon', 100,'1','2024-01-01','9999-01-01', 'Diverse');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('Fitness, Sats', 149,'1','2024-01-01','2024-02-01','Diverse');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('Skatteguiden', 19,'1','2024-01-01','9999-01-01','Diverse');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('Rejsekort', 300,'1','2024-01-01','9999-01-01','Diverse');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('Cykel leasing, Swapfiets', 169,'1','2024-01-01','9999-01-01','Diverse');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('Spotify', 59,'1','2024-01-01','9999-01-01', 'Diverse');

INSERT INTO expenses(expenses_name,expenses_single_expense,expenses_frequency,expenses_first_payment_date, expenses_last_payment_date,expenses_category)  
VALUES('Fitness, Puregym', 249,'1','2024-01-01','2024-02-01','Diverse');

SELECT * FROM expenses WHERE expenses_first_payment_date, expenses_last_payment_date @> '[2024-09-01,2024-09-30)';


UPDATE expenses SET '2024-01-01','9999-01-01' WHERE expenses_name = 'Fitness, Puregym';
