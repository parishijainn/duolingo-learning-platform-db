# us5-analyze-regional-engagement-complex-analytical.py
# COMPLEX / ANALYTICAL

import psycopg2

def show_table(cur, table_name):
    print(f"\n--- {table_name} ---")
    cur.execute(f"SELECT * FROM {table_name};")
    for row in cur.fetchall():
        print(row)

def analyze_regional_engagement(min_lessons=1):
    """
    Assumptions:
      - Learner(userID, region, ...)
      - Progress(userID, lessonTitle, date, completionRate, lessonScore, ...)
      - 'region' is a text field that can be grouped on
    """

    print("\n======================================")
    print("USER STORY 5: Analyze Regional Learner Engagement")
    print("As a program manager, I want to see how engagement")
    print("varies by region so I can prioritize support and")
    print("marketing efforts.")
    print("======================================\n")

    # Connect to the same database used in earlier user stories
    conn = psycopg2.connect(database="duolingo_project", user="isdb")
    cur = conn.cursor()

    # BEFORE — inspect relevant tables
    show_table(cur, "Learner")
    show_table(cur, "Progress")

    # ANALYTICAL QUERY
    sql = """
        WITH region_stats AS (
        SELECT
            u.region,
            COUNT(DISTINCT lr.userID) AS total_learners,
            COUNT(DISTINCT CASE WHEN p.date IS NOT NULL THEN lr.userID END)
                AS active_learners,
            COUNT(p.*) AS lessons_done,
            AVG(p.completionRate) AS avg_completion_rate,
            AVG(p.lessonScore) AS avg_lesson_score
        FROM Learner lr
        JOIN Users u
            ON lr.userID = u.userID
        LEFT JOIN Progress p
            ON lr.userID = p.userID
        GROUP BY u.region
    ),
    ranked AS (
        SELECT
            region,
            total_learners,
            active_learners,
            lessons_done,
            avg_completion_rate,
            avg_lesson_score,
            (CASE
                WHEN total_learners > 0 THEN lessons_done::numeric / total_learners
                ELSE NULL
            END) AS avg_lessons_per_learner,
            RANK() OVER (ORDER BY lessons_done DESC) AS engagement_rank
        FROM region_stats
    )
    SELECT
        region,
        total_learners,
        active_learners,
        lessons_done,
        avg_lessons_per_learner,
        avg_completion_rate,
        avg_lesson_score,
        engagement_rank
    FROM ranked
    WHERE lessons_done >= %s
    ORDER BY engagement_rank;
    """

    print("\nRunning SQL (regional engagement):\n", sql % (min_lessons,))

    cur.execute(sql, (min_lessons,))
    rows = cur.fetchall()

    print("\n--- Regional Engagement Summary ---")
    header = (
        f"{'Region':15}"
        f"{'Learners':>10}"
        f"{'Active':>10}"
        f"{'Lessons':>10}"
        f"{'Avg/Learner':>13}"
        f"{'Avg Comp%':>12}"
        f"{'Avg Score':>12}"
        f"{'Rank':>7}"
    )
    print(header)
    print("-" * len(header))

    for r in rows:
        region                = r[0]
        total_learners        = r[1] or 0
        active_learners       = r[2] or 0
        lessons_done          = r[3] or 0
        avg_lessons_per_user  = r[4]
        avg_completion_rate   = r[5]
        avg_lesson_score      = r[6]
        engagement_rank       = r[7]

        print(
            f"{(region or 'Unknown'):15}"
            f"{total_learners:10d}"
            f"{active_learners:10d}"
            f"{lessons_done:10d}"
            f"{(avg_lessons_per_user or 0):13.2f}"
            f"{(avg_completion_rate or 0):12.2f}"
            f"{(avg_lesson_score or 0):12.2f}"
            f"{engagement_rank:7d}"
        )

    # AFTER — purely analytical, no changes expected
    print("\n--- AFTER EXECUTION (analytical; data unchanged) ---")
    show_table(cur, "Learner")
    show_table(cur, "Progress")

    cur.close()
    conn.close()

# Hard-coded demonstration call
# Require at least 5 lessons in a region to be included
analyze_regional_engagement(min_lessons=5)
