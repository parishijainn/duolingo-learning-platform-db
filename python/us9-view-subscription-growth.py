# us6-view-subscription-growth-complex-analytical.py
# COMPLEX / ANALYTICAL

import psycopg2

def show_table(cur, table_name):
    print(f"\n--- {table_name} ---")
    cur.execute(f"SELECT * FROM {table_name};")
    for row in cur.fetchall():
        print(row)

def view_subscription_growth():
    """
    Assumptions:
      - Subscription(
            subscriptionID SERIAL PRIMARY KEY,
            userID         TEXT,
            startDate      DATE,
            endDate        DATE NULL,
            planType       TEXT,
            isActive       BOOLEAN
        )
      - A subscription is considered:
            * 'new' in the month of startDate
            * 'ended' in the month of endDate (if not NULL)
      - 'active_subscriptions_estimate' is computed as a running
        net of new minus ended per month.
    """

    print("\n======================================")
    print("USER STORY 6: View Subscription Growth Over Time")
    print("As a product manager, I want to see how subscriptions")
    print("grow and churn over time so that I can assess the")
    print("health of the business.")
    print("======================================\n")

    conn = psycopg2.connect(database="duolingo_project", user="isdb")
    cur = conn.cursor()

    # BEFORE — inspect Subscription table
    show_table(cur, "Subscription")

    # ANALYTICAL QUERY FOR MONTHLY SUBSCRIPTION GROWTH
    sql = """
        WITH date_bounds AS (
            SELECT
                MIN(date_trunc('month', startDate))                    AS min_month,
                MAX(
                    date_trunc(
                        'month',
                        COALESCE(endDate, CURRENT_DATE)
                    )
                )                                                      AS max_month
            FROM Subscription
        ),
        months AS (
            SELECT
                generate_series(
                    (SELECT min_month FROM date_bounds),
                    (SELECT max_month FROM date_bounds),
                    interval '1 month'
                ) AS month
        ),
        new_subs AS (
            SELECT
                date_trunc('month', startDate) AS month,
                COUNT(*)                       AS new_cnt
            FROM Subscription
            GROUP BY 1
        ),
        ended_subs AS (
            SELECT
                date_trunc('month', endDate) AS month,
                COUNT(*)                     AS ended_cnt
            FROM Subscription
            WHERE endDate IS NOT NULL
            GROUP BY 1
        )
        SELECT
            m.month::date                                          AS month,
            COALESCE(n.new_cnt, 0)                                 AS new_subscriptions,
            COALESCE(e.ended_cnt, 0)                               AS ended_subscriptions,
            COALESCE(n.new_cnt, 0) - COALESCE(e.ended_cnt, 0)      AS net_change,
            SUM(
                COALESCE(n.new_cnt, 0) - COALESCE(e.ended_cnt, 0)
            ) OVER (ORDER BY m.month)                              AS active_subscriptions_estimate
        FROM months m
        LEFT JOIN new_subs n ON m.month = n.month
        LEFT JOIN ended_subs e ON m.month = e.month
        ORDER BY m.month;
    """

    print("\nRunning SQL (subscription growth):\n", sql)

    cur.execute(sql)
    rows = cur.fetchall()

    print("\n--- Subscription Growth by Month ---")
    header = (
        f"{'Month':12}"
        f"{'New':>8}"
        f"{'Ended':>8}"
        f"{'Net Δ':>8}"
        f"{'Active (Est.)':>15}"
    )
    print(header)
    print("-" * len(header))

    for r in rows:
        month          = r[0]
        new_subs       = r[1]
        ended_subs     = r[2]
        net_change     = r[3]
        active_est     = r[4]

        print(
            f"{month:%Y-%m}"
            f"{new_subs:8d}"
            f"{ended_subs:8d}"
            f"{net_change:8d}"
            f"{active_est:15d}"
        )

    # AFTER — analytical only, table unchanged
    print("\n--- AFTER EXECUTION (analytical; data unchanged) ---")
    show_table(cur, "Subscription")

    cur.close()
    conn.close()

# Hard-coded demonstration call
view_subscription_growth()
