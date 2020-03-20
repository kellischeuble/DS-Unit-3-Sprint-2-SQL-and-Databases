import sqlite3

# this is just for formatting the print
# statements (makes for easy reading)
def printQuestion(question):
    print()
    print()
    print(f'QUESTION {question}:')
    print("-"*50)

def run(x, db="rpg_db.sqlite3"):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute(x)
    answer = curs.fetchall()
    curs.close()
    conn.commit()
    return answer

# creating a new database

test_database = "test.sqlite3"
new_table = """
            CREATE TABLE IF NOT EXISTS test(
            name TEXT,
            age INT,
            grade FLOAT,
            year DATE
            );
"""

run(new_table, test_database)

data = """
        INSERT INTO test
        VALUES 
        ("Kelli", 23, 1, 1980),
        ("Amin", 29, 2, 1960),
        ("Ping", 45, 4, 2008),
        ("Chris", 25, 6, 1920);
"""
returns = run(data, test_database)
print(returns)

get_avg_age =  """
        SELECT AVG(age)
        FROM test
"""
avg = run(get_avg_age, test_database)
print(avg)



# conn = sqlite.connect("rpg_db.sqlite3")
# curs = conn.cursor()
# curs.execute("SELECT * FROM test").fetchall()

# printQuestion("ONE")