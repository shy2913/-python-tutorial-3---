'''for i in range(5):
    print(i) '''
names = ['철수', '영희', '바둑이', '귀도', '비단뱀']

'''for i in range(4):
    name = names[i]
    print('{}번:{}'.format(i+1, name))'''
# 계속 학생 수가 증가할 때는 range()안에 숫자 대신 names리스트 안에 들어있는 이름의 수를 집어넣는 게 낫습니다.

for i in range(len(names)):  # lens함수는 실행인자로 전달받은 항목에 변수가 몇 개 있는 지 돌려준다.
    name = names[i]
    print('{}번:{}'.format(i+1, name))
