# us4-evaluate-study-plan-complex-analytical.py
# COMPLEX / ANALYTICAL

import psycopg2

def show_table(cur, table_name):
    print(f"\n--- {table_name} ---")
    cur.execute(f"SELECT * FROM {table_name};")
    for row in cur.fetchall():
        print(row)

def evaluate_adherence(user_id):
    print("\n======================================")
    print("USER STORY 4: Evaluate Study Plan Adherence")
    print("As a learner, I want to compare planned study sessions")
    print("with the lessons I actually completed, so I can monitor")
    print("how well I follow my study plan.")
    print("======================================\n")

    conn = psycopg2.connect(database="duolingo_project", user="isdb")
    cur = conn.cursor()

    # BEFORE
    show_table(cur, "plannedstudysession")
    show_table(cur, "Progress")

    sql = (
        "WITH joined AS ( "
        "   SELECT "
        "       pss.userID, "
        "       pss.plannedDate, "
        "       pss.lessonTitle AS plannedLesson, "
        "       pss.plannedMinutes, "
        "       pss.completionStatus, "
        "       pr.lessonTitle AS actualLesson, "
        "       pr.date AS actualDate, "
        "       CASE WHEN pr.date IS NOT NULL THEN 'yes' ELSE 'no' END AS completedFlag, "
        "       CASE "
        "           WHEN pss.completionStatus = 'planned' AND pr.date IS NOT NULL THEN 'on track' "
        "           WHEN pss.completionStatus = 'planned' AND pr.date IS NULL THEN 'not completed' "
        "           WHEN pss.completionStatus = 'completed' AND pr.date IS NOT NULL THEN 'completed as planned' "
        "           WHEN pss.completionStatus = 'missed' AND pr.date IS NOT NULL THEN 'completed despite marking missed' "
        "           WHEN pss.completionStatus = 'missed' AND pr.date IS NULL THEN 'missed' "
        "           ELSE 'unknown' "
        "       END AS adherenceStatus "
        "   FROM plannedstudysession pss "
        "   LEFT JOIN Progress pr "
        "       ON pss.userID = pr.userID "
        "       AND pss.lessonTitle = pr.lessonTitle "
        "       AND pss.plannedDate = pr.date "
        "   WHERE pss.userID = '%s' "
        ") "
        "SELECT * FROM joined ORDER BY plannedDate;"
    ) % user_id

    print("\nRunning SQL:\n", sql)
    cur.execute(sql)
    rows = cur.fetchall()

    print("\n--- Study Plan Adherence ---")
    print("Date        Lesson           Planned?    Completed?   Adherence")
    print("--------------------------------------------------------------------")

    for r in rows:
        date = r[1]
        lesson = r[2]
        planned_status = r[4]      
        completed_flag = r[7]
        adherence = r[8]

        print(f"{date}   {lesson:15} {planned_status:10} {completed_flag:10} {adherence}")


    # AFTER EXECUTION — correctly placed OUTSIDE the loop
    print("\n--- AFTER EXECUTION (analytical; no changes expected) ---")
    show_table(cur, "plannedstudysession")

    cur.close()
    conn.close()

# Demonstration call
evaluate_adherence("afels")
