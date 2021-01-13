"""
다음의 값이 주어졌을 때

l = [10, 20, 25, 27, 34, 35, 39]

n번 순회를 결정합니다. 예를 들어 2번 순회면

l = [35, 39, 10, 20, 25, 27, 34]

여기서 변하기 전 원소와 변한 후 원소의 값의 차가 가장 작은 값을 출력하는 프로그램을 작성하세요.

예를 들어 2번 순회했을 때 변하기 전의 리스트와 변한 후의 리스트의 값은 아래와 같습니다.

**순회전_리스트 = [10, 20, 25, 27, 34, 35, 39]
순회후_리스트 = [35, 39, 10, 20, 25, 27, 34]
리스트의_차 = [25, 19, 15, 7, 9, 8, 5]**

39와 변한 후의 34 값의 차가 5이므로 리스트의 차 중 최솟값 입니다.
따라서 39와 34의 인덱스인 6과 39와 34를 출력하는 프로그램을 만들어주세요.

**입력**
순회 횟수는 : 2

**출력**
index : 6
value : 39, 34
"""


def rotation_list(l, n):
    rotated = l[-n:] + l[:-n]
    min_value = 999
    idx = 0
    for i in range(len(l)):
        if min_value > abs(l[i] - rotated[i]):
            min_value = abs(l[i] - rotated[i])
            idx = i
    print(f'index: {idx}')
    print(f'value: {l[idx]}, {rotated[idx]}')


if __name__ == '__main__':
    L = [10, 20, 25, 27, 34, 35, 39]  # 기존 입력 값
    N = int(input('순회 횟수는: '))
    rotation_list(L, N)
