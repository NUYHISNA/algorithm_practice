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
    pass

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