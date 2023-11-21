from conection import *
from table import *
from create_data import create
from zapros import *
from struct_db import data_table


connection = create_connection(
    "postgres", "Harbych", "1111", "127.0.0.1", "5432"
)


execute_query(connection, create_employees_table)
execute_query(connection, create_departments_table)
execute_query(connection, create_positions_table)
execute_query(connection, create_projects_table)
execute_query(connection, create_project_execution_table)

cur = connection.cursor()

create(cur)
# check(cur)
# data_table(cur)