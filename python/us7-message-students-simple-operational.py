# us7-message-students-simple-operational.py
# SIMPLE / OPERATIONAL

import psycopg2

def show_table(cur, table_name):
    print(f"\n--- {table_name} ---")
    cur.execute(f"SELECT * FROM {table_name};")
    for row in cur.fetchall():
        print(row)

def send_message(sender_id, reciever_id, message_text):
    print("\n======================================")
    print("USER STORY 7: Message Students")
    print("As an instructor, I want to send feedback")
    print("so that I can communicate within the platform.")
    print("======================================\n")

    conn = psycopg2.connect(database="duolingo_project", user="isdb")
    cur = conn.cursor()

    # BEFORE
    show_table(cur, "Messages")

    # Insert query
    sql = (
        "INSERT INTO Messages (message, senderID, recieverID) "
        f"VALUES ('{message_text}', '{sender_id}', '{reciever_id}');"
    )


    print("\nRunning SQL:\n", sql)
    cur.execute(sql)
    conn.commit()

    # AFTER
    print("\n--- AFTER EXECUTION ---")
    show_table(cur, "Messages")

    cur.close()
    conn.close()

# hard-coded test call
send_message("cmay", "afels", "Great improvement this week!")
