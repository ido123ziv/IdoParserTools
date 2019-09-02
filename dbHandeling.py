import sqlite3
'''connect to db'''
conn = sqlite3.connect(dbFile)
c = conn.cursor()

'''
the initial creation of the DB
c.execute("""CREATE TABLE IF NOT EXISTS notifications(
        client TEXT,
        cust TEXT,
        server TEXT,
        tech TEXT,
        link TEXT,
        text TEXT,
        time TEXT)
        """)
'''

'''add a line to the table'''
def insertToDB(n):
    with conn:
        c.execute("INSERT INTO notifications VALUES (:client, :cust, :server, :tech, :link, :text, :time)",
                  {'client':n.client, 'cust':n.cust, 'server': n.server, 'tech':n.tech, 'link':n.link, 'text':n.text, 'time':n.time})
        conn.commit()

'''check if we already added to db'''
def ifInDatabase(n):
    with conn:
        c.execute("SELECT * FROM notifications WHERE tech=:tech AND link=:link AND cust=:cust",
                  {'tech': n.tech, 'link': n.link, 'cust': n.cust})
        b = c.fetchall()
        if not b:
            return False
    return True

conn.commit()
