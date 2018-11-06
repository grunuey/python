# 함수에 대한 코멘트
- 우선 각 함수는 되도록 return 값을 가지도록 하는것이 좋다. 예를 들면 user input 같은 경우
> def user_input():
>	n = input('>')
>	return n
과 같이 return 값을 명시하고 다른 유닛에서 사용할 수 있도록 해주는게 좋다.

- 전반적으로, 명령어의 입력과 출력에 대해 class를 선언한 후 해당 클래스의 method 함수로 나머지 함수를 정의하는 것이 일반적이다. text append와 같은 것들은 command text 클래스의 append method로 처리할 수 있다.

- history limit 역시 같은 방식으로 클래스의 자료 크기를 제한함으로서 정의할 수 있다.

- history print 도 method로 구현이 가능하다.

# markdown 문서화 역시 반드시 동반되어야 한다.
