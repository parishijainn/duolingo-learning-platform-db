# us1-track-progress-simple-operational.py
# SIMPLE / OPERATIONAL

import psycopg2

def show_table(cur, table_name):
    print(f"\n--- {table_name} ---")
    cur.execute(f"SELECT * FROM {table_name};")
    for row in cur.fetchall():
        print(row)

def show_daily_progress(user_id, date_value):
    print("\n======================================")
    print("USER STORY 1: Track Daily Progress")
    print("As a learner, I want to view my daily lesson completion")
    print("and streak status so that I can stay motivated.")
    print("======================================\n")

    conn = psycopg2.connect(database="duolingo_project", user="isdb")
    cur = conn.cursor()

    # BEFORE
    show_table(cur, "Learner")
    show_table(cur, "Lesson")
    show_table(cur, "Progress")

    # Query for US1
    # sql = (
    #     "SELECT p.userID, p.date, p.lessonTitle, "
    #     "l.difficulty, p.completionRate, p.lessonScore, "
    #     "lr.currentStreak, lr.longestStreak "
    #     "FROM Progress p "
    #     "JOIN Lesson l ON p.lessonTitle = l.lessonTitle "
    #     "JOIN Learner lr ON p.userID = lr.userID "
    #     f"WHERE p.userID = '{user_id}' "
    #     f"AND p.date = {date_value} "
    #     "ORDER BY p.lessonTitle;"
    # )
    sql = (
        "SELECT p.userID, p.date, p.lessonTitle, "
        "l.difficulty, p.completionRate, p.lessonScore, "
        "lr.currentStreak, lr.longestStreak "
        "FROM Progress p "
        "JOIN Lesson l ON p.lessonTitle = l.lessonTitle "
        "JOIN Learner lr ON p.userID = lr.userID "
        f"WHERE p.userID = '{user_id}' "
        f"AND p.date = TO_DATE('{date_value}', 'YYYYMMDD') "
        "ORDER BY p.lessonTitle;"
    )


    print("\nRunning SQL:\n", sql)
    cur.execute(sql)
    rows = cur.fetchall()

    # RESULTS
    print("\n--- Daily Progress Results ---")
    for row in rows:
        print(row)

    # AFTER (unchanged — simple operational user story)
    print("\n--- AFTER EXECUTION (no updates expected) ---")
    show_table(cur, "Progress")

    cur.close()
    conn.close()

# hard-coded test call 
show_daily_progress("afels", 20251204)
