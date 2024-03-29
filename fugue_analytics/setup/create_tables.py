from fugue_analytics.utilities.postgres import connect_to_postgres, execute_query
from fugue_analytics.setup.github import initialize_github_stats
from fugue_analytics.setup.slack import initialize_slack_stats

def create_metrics_table():
    """
    Creates a table with date, source, and value columns.
    Source can be something like 'Slack Joins' or 'Github Stars'
    """
    conn = connect_to_postgres()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE metrics_over_time ( 
            datetime TIMESTAMP, 
            source TEXT NOT NULL, 
            value INTEGER NOT NULL,
            PRIMARY KEY(datetime, source)
           );
    """)
    print("metric Table created successfully........")
    conn.commit()
    conn.close()
    cur.close()
    return

def drop_table(table_name="metrics_over_time"):
    # Drops a table
    conn = connect_to_postgres()
    cur = conn.cursor()
    cur.execute("""
        DROP TABLE IF EXISTS {};
    """.format(table_name))
    print(f"{table_name} dropped successfully........")
    conn.commit()
    conn.close()
    cur.close()
    return


if __name__ == "__main__":
    drop_table()
    create_metrics_table()
    initialize_github_stats()
    initialize_slack_stats()
    execute_query()