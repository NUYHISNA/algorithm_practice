import sqlite3

"""
기능 명세
1.학생들에 대한 중간/기말 성적 입력
2. 한 학생의 성적 출력 (조회)
3.평균 보여주기
4.메뉴 출력
0.엑셀 파일로 출력
0.엑셀 성적 입력 -> 프로그램에 입력
0.생기부 입력
0.출석, 지각 학생 수업 일수 관리
"""

def print_menu():
    print("학생 성적 관리 프로그램")
    print("1.학생성적 입력")
    print("2.한 학생 성적 출력")
    print("3.평균 계산/보여주기")
    print("4.메뉴 출력")
    print("종료 하기 위해서 exit 입력을 해주세요.")

def input_score():
    print("==== 1. 학생성적 입력 ====")
    print("학생이름 국어 수학 영어 구분 순서대로 입력해주세요")
    print("ex) 홍길동 98 85 95 M")
    value = input().split(" ")
    if len(value) != 5:
        print("입력값을 입력하세요.")
        return
    if (value[4] !="M") and (value[4] != "F"):
        print("M/F 로 중간/기말을 구분해주세요.")
        return
    con = sqlite3.connect("score.db")
    cur = con.cursor()
    cur.execute(f'INSERT INTO score VALUES('{value[0]}','{value[1]}','{value[2]}','{value[3]}','{value[4]}')')
    con.commit()
    con.close()
    print(input_value.split(" "))

def run():
    """
    프로그램 실행 시작점
    """
    is_working = True
    while(is_working):
        print_menu()
        user_input = input("원하시는 메뉴를 선택하세요:")
        if user_input == '1':
            input_score()
        elif user_input == '2':
            print("한 학생 성적 출력\n")
        elif user_input == '3':
            print("평균 계산/보여주기\n")
        elif user_input == '4':
            print("메뉴 출력\n")
        elif user_input == 'exit' :
            print("프로그램을 종료합니다.")
            is_working = False
 
#run()           
input_score()