# 데이터 베이스 생성
import sqlite3

con = sqlite3.connect("score.db")
cur = con.cursor()
# score 테이블 - name(학생이름),Korean(국어점수), math(수학점수), english(영어점수), kind(m-중간/f-기말)
cur.execute("CREATE TABLE score(name, Korean, math, english, kind)")

con.close()