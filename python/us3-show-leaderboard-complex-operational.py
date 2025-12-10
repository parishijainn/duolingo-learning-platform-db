# us3-show-leaderboard-complex-operational.py
# COMPLEX / OPERATIONAL

import psycopg2

def show_table(cur, table_name):
    print(f"\n--- {table_name} ---")
    cur.execute(f"SELECT * FROM {table_name};")
    for row in cur.fetchall():
        print(row)

def show_leaderboard(leaderboard_id):
    print("\n======================================")
    print("USER STORY 3: View Leaderboard Rankings")
    print("As a learner, I want to see my ranking among others so that I can stay motivated through friendly competition.")
    print("======================================\n")

    conn = psycopg2.connect(database="duolingo_project", user="isdb")
    cur = conn.cursor()

    # BEFORE
    show_table(cur, "Users")
    show_table(cur, "Learner")
    show_table(cur, "Leaderboard")
    show_table(cur, "Ranking")

    sql = (
        "SELECT u.userID, u.name, r.rankNumber, r.lessonsCompleted "
        "FROM Ranking r "
        "JOIN Learner l ON r.userID = l.userID "
        "JOIN Users u ON u.userID = r.userID "
        f"WHERE r.leaderboardID = {leaderboard_id} "
        "ORDER BY r.rankNumber ASC;"
    )

    print("\nRunning SQL:\n", sql)
    cur.execute(sql)

    print("\n--- Leaderboard Results ---")
    for row in cur.fetchall():
        print(row)

    # no changes expected because this is read-only
    print("\n--- AFTER EXECUTION (no updates expected) ---")
    show_table(cur, "Ranking")

    cur.close()
    conn.close()


# hard-coded test call 
show_leaderboard(1)
