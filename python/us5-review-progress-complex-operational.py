# us5-review-progress-complex-operational.py
# COMPLEX / OPERATIONAL

import psycopg2

def show_table(cur, table_name):
    print(f"\n--- {table_name} ---")
    cur.execute(f"SELECT * FROM {table_name};")
    for row in cur.fetchall():
        print(row)

def review_learner_progress(user_id):
    print("\n======================================")
    print("USER STORY 5: Review Learner Progress")
    print("As an instructor, I want to review learner progress")
    print("so that I can identify students needing support.")
    print("======================================\n")

    conn = psycopg2.connect(database="duolingo_project", user="isdb")
    cur = conn.cursor()

    # BEFORE
    show_table(cur, "Learner")
    show_table(cur, "Lesson")
    show_table(cur, "Progress")

    # Query for US5
    sql = (
        "SELECT p.userID, p.lessonTitle, p.date, "
        "p.completionRate, p.lessonScore, l.difficulty "
        "FROM Progress p "
        "JOIN Lesson l ON p.lessonTitle = l.lessonTitle "
        f"WHERE p.userID = '{user_id}' "
        "ORDER BY p.date, p.lessonTitle;"
    )

    print("\nRunning SQL:\n", sql)
    cur.execute(sql)
    rows = cur.fetchall()

    # RESULTS
    print("\n--- Learner Progress Results ---")
    for row in rows:
        print(row)

    # AFTER (unchanged — operational, read-only)
    print("\n--- AFTER EXECUTION (no updates expected) ---")
    show_table(cur, "Progress")

    cur.close()
    conn.close()

# hard-coded test call
review_learner_progress("U1")
