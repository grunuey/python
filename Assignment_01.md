2018년 11월 2일 금요일 오늘의 과제는 아래와 같다 ㅋㅋㅋ

1. 계산기에 사용되는 기본적인 연산 유닛들을 각각 함수로 구현하고 calculate.py 파일로 저장한다.
- 필수 구현해야 하는 함수는 아래와 같다.
add(a,b) - 두 수를 더함
multiply(a,b) - 두 수를 곱함
subtract(a,b) - 두 수의 차(a-b)를 구함
divide(a,b) - a를 b로 나눈 몫을 구함
remainder(a,b) - a를 b로 나눈 나머지를 구함
hex(a) - 10진수를 16진수로 변환함
oct(a) - 16진수를 10진수로 변환함

- 각 함수는 아래와 같은 형식으로 작성되어야 한다.
# begin of function add
# "add" 는(은) 두 수를 더해 그 결과를 반환하는 함수이다.
# (input) 입력값
# a: 임의의 숫자
# b: 임의의 숫자
# (output) 출력값
# c: a와 b의 합
def add(a,b)
	c = a+b
	return c
# end of function add

2. main.py 파일을 terminal에서 vim을 이용하여 생성한 후 열어서 아래와 같은 기능을 할 수 있도록 편집한다.
- main.py 파일을 실행하면 아래와 같은 안내 문구를 출력해야 한다.
"My first python program: Calculator"
"Select a number through 1~7 to choose a function."
"(1)add (2)multiply (3)subtract (4)divide (5)remainder (6)hex (7)oct"
- 위의 문구를 출력 후 아래와 같은 모양으로 사용자의 키 입력을 받는다.
>
- 숫자 키 입력을 받으면 입력받은 숫자를 아래와 같은 양식으로 출력한다.
"You entered function number #."
- 이후 프로그램을 종료한다.
