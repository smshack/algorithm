# 민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. 
# AAAA와 BB
# 이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 
# 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.
# 폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 보드판이 주어진다. 보드판의 크기는 최대 50이다.

# 입력 받은 X 가 연속 되는 개수를 카운팅해서 4개 이상이면 A
# 문자열을 입력 받고
line = input()
a ="AAAA"
b = "BB"
# XXXX 이면 AAAA로 바꾸고
answer =line.replace("XXXX",a)
# XX 이면 BB로 바꾸고
answer =answer.replace("XX",b)

# 위에서 다 바꿨는데 X가 있으면 변환이 안되는거니까 -1출력
if(answer.find("X")!=-1):
    print(-1)
else:
    print(answer)


