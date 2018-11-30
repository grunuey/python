def Num_Input(massage):
	while True:
		try:
			n = int(input(massage))
			return n
			break
		except ValueError:
			print('정수를 입력해주세요.')

def Matrix_Multiply(a,b,c,d):
	n = (a * b) + (c * d)
	return n

# 함수 실행
print('2x2크기의 행렬 두개를 곱하는 프로그램 입니다.')
Message_Input = '{}번째 행렬의 {}행 {}열 값 입력 > '

A11 = Num_Input(Message_Input.format(1,1,1))
A12 = Num_Input(Message_Input.format(1,1,2))
A21 = Num_Input(Message_Input.format(1,2,1))
A22 = Num_Input(Message_Input.format(1,2,2))
B11 = Num_Input(Message_Input.format(2,1,1))
B12 = Num_Input(Message_Input.format(2,1,2))
B21 = Num_Input(Message_Input.format(2,2,1))
B22 = Num_Input(Message_Input.format(2,2,2))

C11 = Matrix_Multiply(A11,B11,A12,B21)
C12 = Matrix_Multiply(A11,B12,A12,B22)
C21 = Matrix_Multiply(A21,B11,A22,B21)
C22 = Matrix_Multiply(A21,B12,A22,B22)

print('행렬 곱셈 결과: 1행1열={}, 1행2열={}, 2행1열={}, 2행2열={}'.format(C11,C12,C21,C22))
