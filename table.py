
# Створення таблиці "Співробітники"
create_employees_table = ("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id SERIAL PRIMARY KEY,
        last_name VARCHAR(255),
        first_name VARCHAR(255),
        middle_name VARCHAR(255),
        address VARCHAR(255),
        phone_number VARCHAR(255),
        education VARCHAR(255),
        department_id INTEGER,
        position_id INTEGER
    )
""")
# Відділи
create_departments_table = ("""
    CREATE TABLE IF NOT EXISTS departments (
        department_id SERIAL PRIMARY KEY,
        department_name VARCHAR(255),
        phone_number VARCHAR(255) CHECK (phone_number ~ '^[+]?[0-9 ()-]*$' OR phone_number IS NULL),
        room_number INTEGER CHECK (room_number BETWEEN 701 AND 710)
    )
""")

# Створення таблиці "Посади"
create_positions_table = ("""
    CREATE TABLE IF NOT EXISTS positions (
        position_id SERIAL PRIMARY KEY,
        position_name VARCHAR(255),
        salary INTEGER,
        bonus_percentage INTEGER
    )
""")

# Створення таблиці "Проекти"
create_projects_table = ("""
    CREATE TABLE IF NOT EXISTS projects (
        project_id SERIAL PRIMARY KEY,
        project_name VARCHAR(255),
        deadline DATE,
        funding_size INTEGER
    )
""")

# Створення таблиці "Виконання проектів"
create_project_execution_table = ("""
    CREATE TABLE IF NOT EXISTS project_execution (
        execution_id SERIAL PRIMARY KEY,
        project_id INTEGER REFERENCES projects(project_id),
        department_id INTEGER,
        start_date DATE
    )
""")