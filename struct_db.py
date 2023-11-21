from tabulate import tabulate

def data_table(cur):
    # Виведення структури та даних таблиць
    table_names = ["employees", "departments", "positions", "projects", "project_execution"]

    for table_name in table_names:
        # Виведення структури таблиці
        cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}';")
        structure_result = cur.fetchall()
        print(f"\nСтруктура таблиці '{table_name}':")
        table_structure = tabulate(structure_result, headers=["Назва стовпця", "Тип даних"], tablefmt="grid")
        print(table_structure)

        # Виведення даних таблиці
        cur.execute(f"SELECT * FROM {table_name};")
        data_result = cur.fetchall()
        print(f"\nДані таблиці '{table_name}':")
        table_data = tabulate(data_result, headers=[desc[0] for desc in cur.description], tablefmt="grid")
        print(table_data)

    # Виконання запитів та виведення результатів
    queries = [
        "SELECT * FROM employees WHERE position_id IN (SELECT position_id FROM positions WHERE salary > 2000) ORDER BY last_name;",
        "SELECT department_id, AVG(salary) AS average_salary FROM employees JOIN positions ON employees.position_id = positions.position_id GROUP BY department_id;",
        "SELECT projects.* FROM projects JOIN project_execution ON projects.project_id = project_execution.project_id WHERE project_execution.department_id = 1;",
        "SELECT department_id, COUNT(*) AS employee_count FROM employees GROUP BY department_id;",
        "SELECT last_name, first_name, middle_name, CONCAT('₴', salary * bonus_percentage / 100) AS bonus_amount FROM employees JOIN positions ON employees.position_id = positions.position_id ORDER BY last_name;",
        "SELECT department_id, education, COUNT(*) AS employee_count FROM employees GROUP BY department_id, education ORDER BY department_id, education;"
    ]

    for query in queries:
        cur.execute(query)
        result = cur.fetchall()
        print(f"\nРезультат запиту:\n{query}")
        table_result = tabulate(result, headers=[desc[0] for desc in cur.description], tablefmt="grid")
        print(table_result)
