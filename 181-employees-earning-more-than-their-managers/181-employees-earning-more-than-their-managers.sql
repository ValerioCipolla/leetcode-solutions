# Write your MySQL query statement below
SELECT name as Employee
FROM Employee as x
WHERE salary > (SELECT salary FROM Employee as y WHERE x.managerId = y.id )