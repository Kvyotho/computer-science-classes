#1)
SELECT CONCAT(fname,' ',lname)'admin', name 'business', city
FROM officer o
INNER JOIN business b on o.cust_id = b.cust_id
INNER JOIN customer c on b.cust_id = c.cust_id;
#---------------------//--------------------------------------
#2)
SELECT CONCAT(i.fname,' ',i.lname) names
FROM customer c
JOIN individual i on c.cust_id = i.cust_id
JOIN account a on c.cust_id = a.cust_id
JOIN branch b on a.open_branch_id = b.branch_id
WHERE c.city != b.city
AND c.cust_type_cd = 'I'

UNION

SELECT bu.name names
FROM customer c
JOIN business bu on c.cust_id = bu.cust_id
JOIN account a on c.cust_id = a.cust_id
JOIN branch br on a.open_branch_id = br.branch_id
WHERE c.city != br.city
AND c.cust_type_cd = 'B';

#---------------------//--------------------------------------
#3)
SELECT CONCAT(e.fname,' ',e.lname)emp_name, YEAR(t.txn_date) tr_year, COUNT(t.txn_id) yr
FROM employee e
LEFT JOIN account a on e.emp_id = a.open_emp_id
LEFT JOIN transaction t on a.account_id = t.account_id
GROUP BY e.emp_id, e.fname, e.lname, YEAR(t.txn_date)
ORDER BY emp_name ASC, year(t.txn_date) ASC;	

#---------------------//--------------------------------------
#4)
SELECT a.account_id, CONCAT(i.fname,' ', i.lname)owner_name, a.avail_balance, b.name branch_name
FROM account a
JOIN customer c on a.cust_id = c.cust_id
JOIN individual i on c.cust_id = i.cust_id
JOIN branch b on a.open_branch_id = b.branch_id
WHERE a.avail_balance = (
SELECT MAX(a2.avail_balance)
FROM account a2
WHERE a2.open_branch_id = a.open_branch_id)

UNION

SELECT a.account_id, bu.name owner_name, a.avail_balance, br.name branch_name
FROM account a
JOIN customer c on a.cust_id = c.cust_id
JOIN business bu on c.cust_id = bu.cust_id
JOIN branch br on a.open_branch_id = br.branch_id
WHERE a.avail_balance = (
SELECT MAX(a2.avail_balance)
FROM account a2
WHERE a2.open_branch_id = a.open_branch_id)

ORDER BY avail_balance DESC;

#---------------------//--------------------------------------
#5) A)
CREATE VIEW cityview as
SELECT c.cust_id, c.cust_type_cd, a.open_branch_id, c.city 
FROM customer c
JOIN account a on c.cust_id = a.cust_id
JOIN branch b on a.open_branch_id = b.branch_id
WHERE c.city != b.city;


SELECT CONCAT(i.fname,' ',i.lname) names
FROM cityview cv
JOIN individual i on cv.cust_id = i.cust_id
WHERE cv.cust_type_cd = 'I'

UNION

SELECT bu.name names
FROM cityview cv
JOIN business bu on cv.cust_id = bu.cust_id
WHERE cv.cust_type_cd = 'B';

#---------------------//--------------------------------------
#5) B) 
CREATE VIEW balanceview as
SELECT open_branch_id, MAX(avail_balance) max_bal
FROM account 
GROUP BY open_branch_id;

SELECT a.account_id, CONCAT(i.fname,' ', i.lname)owner_name, a.avail_balance, b.name branch_name
FROM account a
JOIN customer c on a.cust_id = c.cust_id	
JOIN individual i on c.cust_id = i.cust_id
JOIN branch b on a.open_branch_id = b.branch_id
JOIN balanceview bv on a.open_branch_id = bv.open_branch_id and a.avail_balance = bv.max_bal 

UNION

SELECT a.account_id, bu.name owner_name, a.avail_balance, br.name branch_name
FROM account a
JOIN customer c on a.cust_id = c.cust_id
JOIN business bu on c.cust_id = bu.cust_id
JOIN branch br on a.open_branch_id = br.branch_id
JOIN balanceview bv on a.open_branch_id = bv.open_branch_id and a.avail_balance = bv.max_bal 

ORDER BY avail_balance DESC;
