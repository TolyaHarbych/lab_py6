import psycopg2
from psycopg2 import sql
from tabulate import tabulate

def check(cur):
    cur.execute("""
        SELECT * FROM employees
        WHERE position_id IN (
            SELECT position_id FROM positions WHERE salary > 2000
        )
        ORDER BY last_name;
    """)
    result1 = cur.fetchall()
    print("1. Всі робітники з окладом більше 2000 грн:")
    print(tabulate(result1, headers=["employee_id", "last_name", "first_name", "middle_name", "address", "phone_number", "education", "department_id", "position_id"]))

    # Запит 2: Порахувати середню зарплатню в кожному відділі (підсумковий запит)
    cur.execute("""
        SELECT department_id, AVG(salary) AS average_salary
        FROM employees
        JOIN positions ON employees.position_id = positions.position_id
        GROUP BY department_id;
    """)
    result2 = cur.fetchall()
    print("\n2. Середня зарплата в кожному відділі:")
    print(tabulate(result2, headers=["department_id", "average_salary"]))

    # Запит 3: Відобразити всі проекти, які виконуються в обраному відділі (запит з параметром)
    department_id = 1  # Змініть на власний вибір
    cur.execute("""
        SELECT projects.*
        FROM projects
        JOIN project_execution ON projects.project_id = project_execution.project_id
        WHERE project_execution.department_id = %s;
    """, (department_id,))
    result3 = cur.fetchall()
    print("\n3. Проекти, які виконуються в обраному відділі:")
    print(tabulate(result3, headers=["project_id", "project_name", "deadline", "funding_size"]))

    # Запит 4: Порахувати кількість працівників у кожному відділі (підсумковий запит)
    cur.execute("""
        SELECT department_id, COUNT(*) AS employee_count
        FROM employees
        GROUP BY department_id;
    """)
    result4 = cur.fetchall()
    print("\n4. Кількість працівників у кожному відділі:")
    print(tabulate(result4, headers=["department_id", "employee_count"]))

    # Запит 5: Порахувати розмір премії для кожного співробітника (запит з обчислювальним полем)
    # Запит 5: Порахувати розмір премії для кожного співробітника (запит з обчислювальним полем)
    cur.execute("""
        SELECT last_name, first_name, middle_name, CONCAT('₴', salary * bonus_percentage / 100) AS bonus_amount
        FROM employees
        JOIN positions ON employees.position_id = positions.position_id
        ORDER BY last_name;
    """)
    result5 = cur.fetchall()
    print("5. Розмір премії для кожного співробітника:")
    table5 = tabulate(result5, headers=["Прізвище", "Ім'я", "По батькові", "Розмір премії"])
    print(table5)

    # Запит 6: Порахувати кількість робітників, які мають спеціальну, середню, вищу освіту у кожному відділі (перехресний запит)
    cur.execute("""
        SELECT department_id, education, COUNT(*) AS employee_count
        FROM employees
        GROUP BY department_id, education
        ORDER BY department_id, education;
    """)
    result6 = cur.fetchall()
    print("\n6. Кількість робітників за освітою у кожному відділі:")
    print(tabulate(result6, headers=["department_id", "education", "employee_count"]))
