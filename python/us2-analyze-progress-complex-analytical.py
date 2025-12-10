# us2-analyze-progress-complex-analytical.py
# COMPLEX / ANALYTICAL (uses window functions)

import psycopg2

def show_table(cur, table):
    print(f"\n--- {table} ---")
    cur.execute(f"SELECT * FROM {table};")
    for row in cur.fetchall():
        print(row)

def format_date(d):
    s = str(d)
    if len(s) == 8:
        return f"{s[0:4]}-{s[4:6]}-{s[6:8]}"
    return s

# ---------------------------------------------------------
# NEW: Analyze progress for MULTIPLE users
# ---------------------------------------------------------
def analyze_progress(user_list):

    print("\n======================================")
    print("USER STORY 2: Analyze Progress Over Time")
    print("As a learner, I want to see how my lesson completion")
    print("rates and lesson scores change over time across lessons,")
    print("so that I can identify improvement patterns.")
    print("======================================\n")

    conn = psycopg2.connect(database="duolingo_project", user="isdb")
    cur = conn.cursor()

    # BEFORE
    show_table(cur, "Lesson")
    show_table(cur, "Progress")

    for user_id in user_list:

        print("\n======================================")
        print(f"PROGRESS TRENDS FOR USER: {user_id}")
        print("======================================\n")

        sql = (
            "SELECT "
            "   p.userID, "
            "   p.lessonTitle, "
            "   p.date, "
            "   p.completionRate, "
            "   p.lessonScore, "
            "   AVG(p.completionRate) OVER ("
            "       PARTITION BY p.userID, p.lessonTitle "
            "       ORDER BY p.date "
            "       ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW"
            "   ) AS running_avg_completion, "
            "   AVG(p.lessonScore) OVER ("
            "       PARTITION BY p.userID, p.lessonTitle "
            "       ORDER BY p.date "
            "       ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW"
            "   ) AS running_avg_score "
            "FROM Progress p "
            f"WHERE p.userID = '{user_id}' "
            "ORDER BY p.lessonTitle, p.date;"
        )

        print("\nRunning SQL:\n", sql, "\n")
        cur.execute(sql)
        rows = cur.fetchall()

        print("\n--- Progress Trend Results (with Window Functions) ---")

        if not rows:
            print(f"(no progress rows found for user '{user_id}')")
        else:
            header = (
                f"{'Date':<12}"
                f"{'Lesson':<15}"
                f"{'Comp%':>7}"
                f"{'Score':>7}"
                f"{'RunAvg%':>10}"
                f"{'RunAvgScore':>13}"
            )
            print(header)
            print("-" * len(header))

            for (uid, lesson, date_val, comp, score, avg_comp, avg_score) in rows:
                date_str = format_date(date_val)
                avg_comp_f = float(avg_comp)
                avg_score_f = float(avg_score)
                print(
                    f"{date_str:<12}"
                    f"{lesson:<15}"
                    f"{comp:>7}"
                    f"{score:>7}"
                    f"{avg_comp_f:>10.1f}"
                    f"{avg_score_f:>13.1f}"
                )

    # AFTER
    print("\n--- AFTER EXECUTION (analytical; data unchanged) ---")
    show_table(cur, "Progress")

    cur.close()
    conn.close()

# hard-coded demonstration call 
analyze_progress(["afels", "lhariharan"])
