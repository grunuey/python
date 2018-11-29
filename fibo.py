def Fibonacci_Sequence():
	list = [0,1]
	print('n번째의 피보나치 수를 구하는 프로그램입니다.')
	
	while True:
		try:
			print
			print('자연수를 입력해주세요.')
			n = int(input('> '))

		except ValueError:
			print('자연수가 입력되지 않았습니다.')

		else:
			if n < 1:
				print('자연수가 입력되지 않았습니다.')

			elif n >= 1:
				break

			else:
				print('자연수가 입력되지 않았습니다.')

	i = 0

	while i < n and n > 1:
		Add = list[i] + list[i+1]
		list.append(Add)
		i += 1

	print('{}번째 피보나치 수는 {}입니다.'.format(n,list[n-1]))

# 함수 실행
Fibonacci_Sequence()