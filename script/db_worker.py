import sqlite3


def get_max_test_group_number(cursor):
    cursor.execute(""" SELECT max(group_test_id) from statistics""")
    max_id = cursor.fetchone()[0]
    if (max_id == None):
        return -1
    return max_id


def add_new_test_results(timings, concentrate_params):
    conn = sqlite3.connect("statistics.db")
    cursor = conn.cursor()

    group_id = get_max_test_group_number(cursor) + 1

    for i in range(len(timings)):
        cursor.execute("""INSERT into statistics VALUES (?, ?, ?)""", (group_id, timings[i], concentrate_params[i]))
    conn.commit()
    conn.close()



if __name__ == '__main__':
    conn = sqlite3.connect("statistics.db")
    cursor = conn.cursor()

    # Создание таблицы
    cursor.execute("""CREATE TABLE statistics
                    (group_test_id int, time_sec int, attention_switch real)
                """)