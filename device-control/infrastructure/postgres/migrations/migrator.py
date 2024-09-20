import argparse
from sqlalchemy import create_engine, text

DATABASE_URL =  "postgresql://chuikin.p:chuikin.p@localhost:5432/yandex-test?sslmode=disable"

def execute_sql_file(file_path):
    """Reads and executes the SQL commands from the provided file."""
    with open(file_path, 'r') as file:
        sql_commands = file.read()

    # Create an engine and execute the SQL commands
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        connection.execute(text(sql_commands))
        connection.execute(text("COMMIT"))  # Ensure that changes are committed if necessary

def main():
    # Setup argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='Run database migrations.')

    # Define the arguments --up and --down
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--up', action='store_true', help='Run the up migration (apply the migration).')
    group.add_argument('--down', action='store_true', help='Run the down migration (rollback the migration).')

    # Parse the arguments
    args = parser.parse_args()

    # Run the appropriate migration
    if args.up:
        print("Running the up migration...")
        execute_sql_file('up.sql')
    elif args.down:
        print("Running the down migration...")
        execute_sql_file('down.sql')
    else:
        print("Running default migrations...")
        execute_sql_file('up.sql')

if __name__ == "__main__":
    main()
