import pymysql


def connect():
    con = pymysql.connect(
        host="1.12.246.2",
        port=3306,
        user="sxy",
        password="Shao264419",
        database="zezhong"
    )
    cur = con.cursor()
    return con, cur


def execute_query(query):
    con, cur = connect()
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()


def fetchone(query):
    con, cur = connect()
    cur.execute(query)
    data = cur.fetchone()
    cur.close()
    con.close()
    return data


def fetchall(query):
    con, cur = connect()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    con.close()
    return data
