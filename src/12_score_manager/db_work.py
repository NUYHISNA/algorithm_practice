# 데이터 베이스 생성
import sqlite3

con = sqlite3.connect("score.db")
cur = con.cursor()
cur.execute("CREATE TABLE score(name, Korean, math, english, kind)")

con.close()