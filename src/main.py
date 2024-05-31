import psycopg2 as pg
import api.stock_api as api
import database.database as format
tickers= api.get_sp500_tickers()

try:
    connection = pg.connect(
        dbname="Market Monitor",
        user="postgres",
        password="sb1112",
        host="localhost",
        port="5433"
    )
    print("Connection to PostgreSQL database successful!")
except pg.Error as e:
    print("Error connecting to PostgreSQL database:", e)

data = api.get_company_profile(tickers[3])
format = format.company_profile_insert_statement(data)

cursor = connection.cursor()

# Example: Delete a row from a table
try:
    # Assume we have a table named "users" with columns "id", "name", and "email"
    # We want to delete the row where id=1
    cursor.execute(format)
    print("Row inserted successfully")
except pg.Error as e:
    print("Error deleting row:", e)
    connection.rollback()  # Rollback the transaction in case of an error
finally:
    # Commit the transaction and close cursor and connection
    connection.commit()
    cursor.close()
    connection.close()
    print("Connection closed.")