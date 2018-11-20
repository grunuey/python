# begin of Predefine
# 'import random'는 랜덤을 사용할 수 있도록 설정하는 함수이다.
# 'Hand_List'는 묵찌빠에서 선택할 수 있는 패의 종류이다.
# 'User_State'는 공격, 수비, 미결정에 관련된 상태를 나타낸다. (0=미결정, 1=공격, 2=수비)
# 'Message_XXXX'은 묵찌빠에서 사용되는 메시지들이다. 
import random
Hand_List = ['묵','찌','빠']
User_State = 0
Message_Start = '[ 컴퓨터와 묵찌빠를 시작합니다. ]'
Message_Input = '묵, 찌, 빠 중 하나를 선택하세요. : '
Message_Error = '에러가 발생했습니다.'
Message_Choice = '> 묵, 찌, 빠 이외의 패를 선택하셨습니다.'
Message_Hand = '> 당신은 {}, 컴퓨터는 {} 입니다.'
Message_Trun = '> 공격, 수비를 결정하겠습니다.'
Message_Attack = '> 당신이 공격입니다.'
Message_Defense = '> 당신이 수비입니다.'
Message_Win = '[ 같은 패로 당신이 승리하였습니다. ]'
Message_lose = '[ 같은 패로 당신이 패배하였습니다. ]'
# end of Predefine

# begin of function Computer_Choice
# 'Computer_Choice'는 컴퓨터가 선택할 패를 정하는 함수이다.
# Com_Choice : 컴퓨터가 선택한 패
def Computer_Choice():
    Com_Choice = random.choice(Hand_List)
    return Com_Choice
# end of function computer_choice

# begin of function Player_Choice
# 'Player_Choice'은 유저가 선택할 패를 입력받는 함수이다.
# User_Choice : 유저가 선택한 패
def Player_Choice():
    User_Choice = input(Message_Input)
    if User_Choice == '묵':
        return User_Choice
    if User_Choice == '찌':
        return User_Choice
    if User_Choice == '빠':
        return User_Choice
    else:
        while User_Choice not in ['묵','찌','빠']:
            print(Message_Choice)
            User_Choice = input(Message_Input)
            continue
        return User_Choice
# end of function Player_Choice

# begin of function Hand_Check
# 'Hand_Check'은 유저와 컴퓨터의 패를 비교하는 함수이다.
# result : 비교에 따른 값 결정 (0 = 비기는 패, 1 = 유저가 이기는 패, 2 = 유저가 지는 패)
def Hand_Check():
    if User == Computer:
        result = 0
        return result
    else:
        if User == '찌':
            if Computer == '묵':
                result = 2
                return result
            else:
                result = 1
                return result
        elif User== '묵':
            if Computer == '빠':
                result = 2
                return result
            else:
                result = 1
                return result
        elif User == '빠':
            if Computer == '찌':
                result = 2
                return result
            else:
                result = 1
                return result
        else:
            result = 3
            print(Message_Error)
# end of function Hand_Check

############################ 함수 실행 or 테스트 출력 코드
print(Message_Start)
print(Message_Trun)
Computer = Computer_Choice()
User = Player_Choice()
User_State = Hand_Check()
print(Message_Hand.format(User,Computer))
while User_State in [0,1,2]:
    if User_State == 0:
        print(Message_Trun)
        Computer = Computer_Choice()
        User = Player_Choice()
        Result = Hand_Check()
        User_State = Result
        print(Message_Hand.format(User,Computer))
    elif User_State == 1:
        print(Message_Attack)
        Computer = Computer_Choice()
        User = Player_Choice()
        Result = Hand_Check()
        print(Message_Hand.format(User,Computer))
        if Result == 0:
            print(Message_Win)
            break
        else:
            User_State = Result
    elif User_State == 2:
        print(Message_Defense)
        Computer = Computer_Choice()
        User = Player_Choice()
        Result = Hand_Check()
        print(Message_Hand.format(User,Computer))
        if Result == 0:
            print(Message_lose)
            break
        else:
            User_State = Result
    else:
        print(Message_Error)