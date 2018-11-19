# begin of Predefine
# 'import random'는 랜덤을 사용할 수 있도록 설정하는 함수이다.
# 'RPS_List'는 가위바위보에서 선택할 수 있는 패의 종류이다. (RockPaperScissors == RPS)
# 'Message_XXXX'은 가위바위보에서 사용되는 메시지들이다.
import random
RPS_List = ['바위','보','가위']
Message_Start = "컴퓨터와 가위바위보를 시작 하겠습니다."
Message_Input = ">> 가위, 바위, 보 중 당신이 사용할 패를 입력해주세요. : "
Message_Error = "당신은 가위, 바위, 보 이외의 패를 입력하였습니다."
Message_Result = "당신은 {}이고, 컴퓨터는 {}로 {}"
# end of Predefine

# begin of function Computer_Choice
# 'Computer_Choice'는 컴퓨터가 선택할 패를 정하는 함수이다.
# Com_Choice : 컴퓨터가 선택한 패
def Computer_Choice():
    Com_Choice = random.choice(RPS_List)
    return Com_Choice
# end of function computer_choice

# begin of function Player_Choice
# 'Player_Choice'은 유저가 선택할 패를 입력받는 함수이다.
# User_Choice : 유저가 선택한 패
def Player_Choice():
    User_Choice = input(Message_Input)
    if User_Choice=='바위':
        return User_Choice
    if User_Choice=='보':
        return User_Choice
    if User_Choice=='가위':
        return User_Choice
    else:
        print(Message_Error)
        User_Input()
# end of function Player_Choice

# begin of function RPS_Rule
# 'RPS_Rule'은 가위바위보의 승리,패배의 조건 함수이다.
# result : 컴퓨터와 유저의 승패 결과
def RPS_Rule():
    if User == Computer:
        result = '비겼습니다.'
        return result
    else:
        if User=='가위':
            if Computer=='바위':
                result = '당신이 졌습니다.'
                return result
            else:
                result = '당신이 이겼습니다.'
                return result
        elif User=='바위':
            if Computer=='보':
                result = '당신이 졌습니다.'
                return result
            else:
                result = '당신이 이겼습니다.'
                return result
        elif User=='보':
            if Computer=='가위':
                result = '당신이 졌습니다.'
                return result
            else:
                result = '당신이 이겼습니다.'
                return result
        else:
            print(Message_Error)
# end of function RPS_Rule

# 함수 실행 or 테스트 출력 코드
print(Message_Start)
Computer = Computer_Choice()
User = Player_Choice()
Result = RPS_Rule()
print(Message_Result.format(User,Computer,Result))