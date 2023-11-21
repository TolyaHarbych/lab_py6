from faker import Faker
import random
from middle_name import ukrainian_middle_names


fake = Faker('uk_UA')
def create(cur):
    for _ in range(17):
        last_name = random.choice(ukrainian_middle_names)
        cur.execute("""
            INSERT INTO employees (last_name, first_name, middle_name, address, phone_number, education, department_id, position_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            fake.last_name(),
            fake.first_name(),
            last_name,
            fake.address(),
            fake.phone_number(),
            random.choice(['special', 'secondary', 'higher']),
            random.randint(1, 5),
            random.randint(1, 3)
        ))


    # Заповнення таблиці "Відділи"
    for i in range(5):
        cur.execute("""
            INSERT INTO departments (department_name, phone_number, room_number)
            VALUES (%s, %s, %s)
        """, (
            f"Department {i+1}",
            fake.phone_number(),
            random.randint(701, 710)
        ))

    # Заповнення таблиці "Посади"
    positions_data = [
        ("Engineer", 50000, 10),
        ("Editor", 45000, 8),
        ("Programmer", 60000, 15)
    ]

    for position_data in positions_data:
        cur.execute("""
            INSERT INTO positions (position_name, salary, bonus_percentage)
            VALUES (%s, %s, %s)
        """, position_data)

    # Заповнення таблиці "Проекти"
    for i in range(8):
        cur.execute("""
            INSERT INTO projects (project_name, deadline, funding_size)
            VALUES (%s, %s, %s)
        """, (
            f"Project {i+1}",
            fake.future_date(),
            random.randint(100000, 500000)
        ))

    # Заповнення таблиці "Виконання проектів"
    for i in range(8):
        cur.execute("""
            INSERT INTO project_execution (project_id, department_id, start_date)
            VALUES (%s, %s, %s)
        """, (
            i + 1,
            random.randint(1, 5),  # assuming there are 5 departments
            fake.past_date()
        ))



