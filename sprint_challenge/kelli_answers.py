import sqlite3

# this is just for formatting the print
# statements (makes for easy reading)
def printQuestion(question):
    print()
    print()
    print(question)

def run(x, db):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute(x)
    answer = curs.fetchall()
    curs.close()
    conn.commit()
    return answer

printQuestion("PART ONE")

# creating a new database
db1 = "demo_data.sqlite3"

new_table = """
    CREATE TABLE IF NOT EXISTS demo (
    s VARCHAR,
    x INT,
    y INT
);
"""
run(new_table, db1)

# INSERT DATA
insert_data = """
        INSERT INTO demo
        (s, x, y)
        VALUES 
        ('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7);
"""
run(insert_data, db1)

printQuestion('Number of rows:')
query = 'SELECT COUNT(*) FROM demo'
rows = run(query, db1)
print(rows[0][0])

printQuestion('Number of rows where x AND y are at least 5:')
query = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5
AND y >= 5
"""
rows_5 = run(query, db1)
print(rows_5[0][0])

printQuestion('Unique values of y:')
query = """
SELECT COUNT(DISTINCT y)
FROM demo
"""
distinct_y = run(query, db1)
print(distinct_y[0][0])

printQuestion("PART TWO")
db2 = "northwind_small.sqlite3"

# THIS IS WRONG!!!!
printQuestion('Ten most expensive items:')

query = """
SELECT ProductName
FROM Product
ORDER BY Product.UnitPrice DESC
LIMIT 10;
"""
top_products = run(query, db2)
print(list(top_products))

printQuestion('Average age of an employee at time of hiring:')

query = """
SELECT AVG(HireDate - BirthDate)
FROM Employee;
"""
avg_age = run(query, db2)
print(avg_age[0][0])

printQuestion('Average age of an employee at time of hiring by city:')

query = """
SELECT AVG(HireDate - BirthDate), City
FROM Employee
GROUP BY City;
"""
avg_age_by_city = run(query, db2)
print(list(avg_age_by_city))

printQuestion("PART THREE")

printQuestion("Ten most expensive items and suppliers:")

query = """
SELECT ProductName, CompanyName
FROM Product p
JOIN Supplier s
ON p.Id = s.Id
ORDER BY UnitPrice DESC
LIMIT 10;
"""

products_suppliers = run(query, db2)
print(list(products_suppliers))

printQuestion("Largest category:")
query = """
SELECT CategoryName, COUNT(CategoryId) FROM Product
JOIN Category ON Product.CategoryId = Category.id
GROUP BY CategoryId
ORDER BY COUNT(CategoryId) DESC
LIMIT 1;
"""

category = run(query, db2)
print(category[0][0])

printQuestion("Employee with most territories:")
query = """
SELECT FirstName, LastName
FROM Employee e
JOIN EmployeeTerritory et
ON e.Id = et.EmployeeId
JOIN Territory t
ON et.TerritoryId = t.Id
GROUP BY e.Id
ORDER BY COUNT(et.TerritoryId) DESC
LIMIT 1;
"""

employee = run(query, db2)
print(employee)


# The Employee and Territory tables have a many to many relationship. This is
# because many different employees can belong to many different territories,
# and vise versa. Because of this, there needs to be an intermediate table in 
# between to allow joins.

# A document store might be appropriate in the beginning stages when the relationship
# between all of the data isn't really all that fleshed out yet, and the data
# is all kind of realted, but not really. It also might be appropriate when 
# gettin into the "BIG DATA" realm, where there is so much data it needs to be
# stored among all different systems. 

# NewSQL is trying to bridge the gap between noSQL and document stores. This is
# useful when the data is way too large
# for a relational database, so that we can still have the transactional
# and consistency requirements that are usually hard to get with document stores.
# These newSQL systems allow for both consistency and scalability. The term
# isn't as broad as NoSQL. However, newSQL still has the relational data model but 
# with more scalability.