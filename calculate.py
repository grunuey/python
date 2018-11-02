# begin of function add
# "add"는 두 수를 더해 그 결과를 반환하는 함수이다.
# (input) 입력값
# a : 임의의 숫자
# b : 임의의 숫자
# (output) 출력
# c : a와 b의 합
def add(a,b):
    c=a+b
    return c
# end of function add

# begin of function multiply
# "multiply"는 두 수를 곱해 그 결과를 반환하는 함수이다.
# (input) 입력값
# a : 임의의 숫자
# b : 임의의 숫자
# (output) 출력
# c : a와 b의 곱
def multiply(a,b):
    c=a*b
    return c
# end of function multiply

# begin of function subtract
# "subtract"는 a에서 b의 차를 그 결과로 반환하는 함수이다.
# (input) 입력값
# a : 임의의 숫자
# b : 임의의 숫자
# (output) 출력
# c : a에서 b의 차
def subtract(a,b):
    c=a-b
    return c
# end of function subtract

# begin of function divide
# "divide"는 a에서 b로 나눈 몫을 그 결과로 반환하는 함수이다.
# (input) 입력값
# a : 임의의 숫자
# b : 임의의 숫자
# (output) 출력
# c : a에서 b로 나눈 몫
def divide(a,b):
    c=a/b
    return c
# end of function divide

# begin of function remainder
# "remainder"는 a에서 b로 나눈 나머지 값을 그 결과로 반환하는 함수이다.
# (input) 입력값
# a : 임의의 숫자
# b : 임의의 숫자
# (output) 출력
# c : a에서 b로 나눈 나머지 값
def remainder(a,b):
    c=a%b
    return c
# end of function remainder

# begin of function hexagonal
# "hexagonal"는 10진수 a를 16진수 값으로 변환하는 함수이다.
# (input) 입력값
# a : 임의의 숫자
# (output) 출력
# c : 10진수 a를 16진수 값으로 변환한 값
def hexagonal(a):
    c=hex(a)
    return c
# end of function hexagonal

# begin of function integ
# "integ"는 16진수 a를 10진수 값으로 변환하는 함수이다.
# (input) 입력값
# a : 임의의 숫자
# (output) 출력
# c : 16진수 a를 10진수 값으로 변환한 값
def integ(a):
    c=int(str(a),16)
    return c
# end of function integ