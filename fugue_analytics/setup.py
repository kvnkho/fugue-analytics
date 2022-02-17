from fugue_analytics.utilities import connect_to_postgres

def create_metrics_table():
    # Creates a table with date, source, and value columns
    # source can be something like 'Slack' or 'Github'
    conn = connect_to_postgres()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE metrics_over_time ( 
            date DATE, 
            source TEXT NOT NULL, 
            value INTEGER NOT NULL,
            PRIMARY KEY(date, source)
           );
    """)
    print("metric Table created successfully........")
    conn.close()

def recreate_metrics_table():
    # Creates a 
    conn = connect_to_postgres()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE metrics_over_time ( 
            date DATE, 
            source TEXT NOT NULL, 
            value INTEGER NOT NULL,
            PRIMARY KEY(date, source)
           );
    """)
    print("metric Table created successfully........")
    conn.close()


if __name__ == "__main__":
    create_metrics_table()