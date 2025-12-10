# us6-generate-report-complex-analytical.py
# COMPLEX / ANALYTICAL

import psycopg2

def show_table(cur, table_name):
    print(f"\n--- {table_name} ---")
    cur.execute(f"SELECT * FROM {table_name};")
    for row in cur.fetchall():
        print(row)

def generate_progress_report():
    print("\n======================================")
    print("USER STORY 6: Generate Progress Report")
    print("As an instructor, I want to generate reports")
    print("so that I can analyze learner accuracy over time.")
    print("======================================\n")

    conn = psycopg2.connect(database="duolingo_project", user="isdb")
    cur = conn.cursor()

    # BEFORE
    show_table(cur, "Progress")
    show_table(cur, "Report")

    # Analytical query
    sql = (
        "SELECT userID, AVG(lessonScore) AS avgScore "
        "FROM Progress "
        "GROUP BY userID, date "
        "ORDER BY userID;"
    )

    print("\nRunning SQL:\n", sql)
    cur.execute(sql)
    rows = cur.fetchall()

    print("\n--- Progress Analytical Results ---")
    for row in rows:
        print(row)

    # AFTER
    print("\n--- AFTER EXECUTION ---")
    show_table(cur, "Report")

    cur.close()
    conn.close()

# hard-coded test call
generate_progress_report()
