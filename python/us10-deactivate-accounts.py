# us7-deactivate-subscription-trigger-operational.py
# COMPLEX / OPERATIONAL (uses a trigger function)

import psycopg2

def show_table(cur, table_name):
    print(f"\n--- {table_name} ---")
    cur.execute(f"SELECT * FROM {table_name};")
    for row in cur.fetchall():
        print(row)

def setup_deactivation_trigger():
    """
    USER STORY 7: Auto-Deactivate Ended Subscriptions (Trigger)
    As a system administrator, I want subscriptions to be
    automatically marked inactive once their end date has passed
    so that user access is kept in sync without manual updates.

    Assumptions:
      - Subscription(
            subscriptionID SERIAL PRIMARY KEY,
            userID         TEXT,
            startDate      DATE,
            endDate        DATE NULL,
            planType       TEXT,
            isActive       BOOLEAN DEFAULT TRUE
        )
      - We create a BEFORE INSERT OR UPDATE trigger that:
            * If NEW.endDate < CURRENT_DATE, sets NEW.isActive = FALSE
            * Otherwise leaves NEW.isActive unchanged
    """

    print("\n======================================")
    print("USER STORY 7: Auto-Deactivate Ended Subscriptions (Trigger)")
    print("======================================\n")

    conn = psycopg2.connect(database="duolingo_project", user="isdb")
    conn.autocommit = True
    cur = conn.cursor()

    # BEFORE — inspect current Subscription data
    show_table(cur, "Subscription")

    # CREATE OR REPLACE TRIGGER FUNCTION + TRIGGER
    trigger_sql = """
        -- Ensure column exists (optional, comment out if not needed)
        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM information_schema.columns
                WHERE table_name = 'subscription'
                  AND column_name = 'isactive'
            ) THEN
                ALTER TABLE Subscription
                    ADD COLUMN isActive BOOLEAN DEFAULT TRUE;
            END IF;
        END;
        $$;

        -- Trigger function to deactivate subscriptions whose endDate has passed
        CREATE OR REPLACE FUNCTION deactivate_subscription_on_end()
        RETURNS TRIGGER AS $$
        BEGIN
            IF NEW.endDate IS NOT NULL AND NEW.endDate < CURRENT_DATE THEN
                NEW.isActive := FALSE;
            END IF;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;

        -- Drop and recreate trigger for idempotency
        DROP TRIGGER IF EXISTS trg_deactivate_subscription_on_end
            ON Subscription;

        CREATE TRIGGER trg_deactivate_subscription_on_end
        BEFORE INSERT OR UPDATE OF endDate
        ON Subscription
        FOR EACH ROW
        EXECUTE FUNCTION deactivate_subscription_on_end();
    """

    print("\nRunning SQL to create trigger and function:\n")
    print(trigger_sql)

    cur.execute(trigger_sql)

    print("\nTrigger function and trigger created successfully.")

    # OPTIONAL: simple demonstration of how the trigger behaves.
    # (Assumes at least one row exists; safe-guard with WHERE 1=1 LIMIT 1.)
    demo_sql = """
        -- Set the endDate of one sample subscription to 'yesterday'
        -- so that the trigger marks isActive = FALSE.
        UPDATE Subscription
        SET endDate = CURRENT_DATE - INTERVAL '1 day'
        WHERE subscriptionID = (
            SELECT subscriptionID
            FROM Subscription
            ORDER BY subscriptionID
            LIMIT 1
        );
    """

    print("\nRunning optional demo UPDATE to show deactivation effect:\n")
    print(demo_sql)
    cur.execute(demo_sql)

    # AFTER — show Subscription again to confirm isActive changed
    print("\n--- AFTER EXECUTION (trigger operational) ---")
    show_table(cur, "Subscription")

    cur.close()
    conn.close()

# Hard-coded demonstration call
setup_deactivation_trigger()
