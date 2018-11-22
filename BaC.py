# begin of Predefine
# 'import random'는 랜덤을 사용할 수 있도록 설정하는 함수이다.
import random

Message_Start = '[숫자 야구 게임을 시작합니다]'
Message_Rule = '>> 중복되지 않는 숫자 조합의 세자리 숫자를 9회말까지 맞춰주세요.'

Message_Input = '숫자를 입력하세요 >> '
Message_NoNum = '>> 숫자 이외의 값이 입력되었습니다.'
Message_NoRange = '>> 세자리 이외의 숫자가 입력되었습니다.'
Message_Same = '>> 중복된 숫자의 조합이 입력되었습니다.'

Message_Result = '>> {}회말 - S:{} , B:{} , O:{}'

Message_WinEnd = '>> 정답입니다. 숫자 야구 게임을 종료합니다.'
Message_LoseEnd = '>> 정답은 {}입니다. 숫자 야구 게임을 종료합니다.'
# end of Predefine

# begin of function BaC_Answer
# 'BaC_Answer'는 숫자야구 게임의 정답을 정하는 함수이다.
# 각 자릿수의 숫자들은 중복되면 안된다.
# BaC_Answer : 숫자 야구 게임의 정답
def Create_Answer():
	BaC_List = list(range(10))
	BaC_1st = random.choice(BaC_List)
	BaC_2nd = random.choice(BaC_List)
	while BaC_2nd == BaC_1st:
		BaC_2nd = int(random.choice(BaC_List))
		continue
	BaC_3rd = random.choice(BaC_List)
	while BaC_3rd == BaC_1st:
		BaC_3rd = random.choice(BaC_List)
		continue
	while BaC_3rd == BaC_2nd:
		BaC_3rd = random.choice(BaC_List)
		continue
	BaC_Answer = BaC_1st*100 + BaC_2nd*10 + BaC_3rd
	return BaC_Answer
# end of function BaC_Answer

# begin of function User_Input
# 'User_Input'은 유저가 입력한 문자를 받는 함수이다.
# User_Num : 중복되지 않는 숫자 조합의 세자리 숫자
def User_Input():
	while True:
		User_Num = input(Message_Input)
		if len(User_Num) == 3:
			try:
				# 입력값 각자리 숫자로 변환 설정
				Check_1st = int(int(User_Num)/100)
				Check_2nd = int((int(User_Num)-(Check_1st*100))/10)
				Check_3rd = int(User_Num)-(Check_1st*100)-(Check_2nd*10)
			except ValueError:
				# 변환 값이 숫자가 아니어서 메시지 처리
				print(Message_NoNum)
			else:
				# 중복된 숫자가 있어서 메시지 처리
				if Check_1st - Check_2nd == 0:
					print(Message_Same)
				elif Check_1st - Check_3rd == 0:
					print(Message_Same)
				elif Check_2nd - Check_3rd == 0:
					print(Message_Same)
				# 중복되지 않는 숫자 조합의 세자리 숫자 처리(종료)
				else:
					break
		else:
			# 세자리 이상/이하의 숫자로 메시지 처리
			print(Message_NoRange)
	return User_Num
# end of function User_Input

########## 함수 실행 or 테스트 코드
print(Message_Start)
print(Message_Rule)

# 정답 생성
Answer_Num = Create_Answer()

# 자리수별 정답 설정
Answer_1st = int(int(Answer_Num)/100)
Answer_2nd = int((int(Answer_Num)-(Answer_1st*100))/10)
Answer_3rd = int(Answer_Num)-(Answer_1st*100)-(Answer_2nd*10)

# 진행 횟수 확인용 변수 설정
Inning_Count = 0

# 정답 비교 및 유저 입력을 반복적으로 진행하도록 설정
while True: 
	# 입력값을 받음
	Input_Num = int(User_Input())

	# 자리수별 입력값 설정
	Input_1st = int(int(Input_Num)/100)
	Input_2nd = int((int(Input_Num)-(Input_1st*100))/10)
	Input_3rd = int(Input_Num)-(Input_1st*100)-(Input_2nd*10)

	# 비교 결과 초기화 처리
	Strike_Count = 0
	Ball_Count = 0
	Out_Count = 3
	
	# 정답과 입력 값이 같으면 종료(승리)되도록 설정
	if Input_Num - Answer_Num == 0:
		print(Message_WinEnd)
		break
	# 10번째 시도에서는 숫자 게임이 종료(패배)되도록 설정
	elif Inning_Count == 9:
		print(Message_LoseEnd.format(str(Answer_Num)))
		break
 	# 정답과 입력 값을 비교 설정 (스트라이크/볼/아웃)
	else:
		# 첫번째 자리수 스트라이크 확인
		if Input_1st - Answer_1st == 0:
			Strike_Count += 1
		# 두번째 자리수 스트라이크 확인
		if Input_2nd - Answer_2nd == 0:
			Strike_Count += 1
		# 세번째 자리수 스트라이크 확인
		if Input_3rd - Answer_3rd == 0:
			Strike_Count += 1
		else:
			# 첫번째 자리수 볼 확인
			if Answer_1st == Input_2nd:
				Ball_Count += 1
			if Answer_1st == Input_3rd:
				Ball_Count += 1
			# 두번째 자리수 볼 확인
			if Answer_2nd == Input_1st:
				Ball_Count += 1
			if Answer_2nd == Input_3rd:
				Ball_Count += 1
			# 세번째 자리수 볼 확인
			if Answer_3rd == Input_1st:
				Ball_Count += 1
			if Answer_3rd == Input_2nd:
				Ball_Count += 1

	# 진행 횟수 계산
	Inning_Count += 1

	# 비교 결과 계산 및 표시
	Out_Count -= Strike_Count + Ball_Count
	print(Message_Result.format(Inning_Count,Strike_Count,Ball_Count,Out_Count))