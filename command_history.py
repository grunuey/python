# Basic setting
# history_text : 유저가 입력한 값 중 저장된 내용
# history_list : historytext에 저장할 값 갯수 제한 수치
history_text=['G','R','U','N','U','E','Y']
history_list=7

# begin of function user_input
# "user_input"은 유저가 값을 입력할 수 있도록 하는 함수이다.
# (input) 입력값
# n : 임의의 숫자 또는 문자
##def user_input():
n=input('> ')
# end of function user_input

# begin of function history_add
# "history_add"는 유저가 입력한 값을 저장하는 함수이다.
##def history_add():
history_text.append(n)
# end of function history_add

# begin of function history_limit
# "history_limit"은 유저가 입력하여 저장되는 목록 갯수를 조정하는 함수이다.
# history_text에 저장된 값이 history_list에 설정된 수보다 많으면 가장 처음 저장된 값을 삭제한다.
##def history_limit():
if len(history_text)>history_list:
    del history_text[0]
# end of function history_limit

# begin of function history_print
# "history_print"은 저장된 목록의 값들을 출력하는 함수이다.
##def history_print():
for history_text in history_text:
    print(history_text,end=" ")
else:
    print()
# end of function history_print