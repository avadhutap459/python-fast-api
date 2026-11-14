from app.database import engine

try:

    with engine.connect() as connection:

        result = connection.exec_driver_sql(
            "SELECT DB_NAME(), SUSER_SNAME()"
        )

        row = result.fetchone()

        print("Database Connected Successfully!")

        print("Database Name:", row[0])

        print("Windows User:", row[1])

except Exception as e:

    print("Database Connection Failed!")

    print("Error:", str(e))