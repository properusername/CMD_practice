print("학번:2021310269, 이름:이강민")

print("<홀수/짝수 판별 프로그램>")

cnt = 0

while True:
    number = int(input("\n>>>양의 정수 입력:"))

    if number>0:
        if number%2==0:
            print("=> 입력한 정수는 짝수 입니다.")
        else:
            print("=> 입력한 정수는 홀수 입니다.")
        cnt+=1

    else:
        print("=> 입력한 정수 %d은(는) 양의 정수가 아닙니다."%number)
        print("=> 0보다 큰 양의 정수를 입력하세요.")

    
    
    select = input("\n계속 실행하시겠습니까?(계속:enter, 종료:'0'):")

    if select == "0":
        break

print("\n%d회 반복, 홀수/짝수 판별 프로그램 종료"%cnt)
