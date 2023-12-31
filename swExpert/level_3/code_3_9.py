T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    cnt = 0
    for i in range(b+1) :
        po = i * i
        po1 = str(po)
        po2 = po1[::-1]
        i2 = str(i)
        i3 = i2[::-1]
        if po1 == po2 and po <= b and po >= a and i2 == i3:
            cnt += 1
    print('#{} {}'.format(test_case,cnt))

'''
앞으로 읽어도 뒤로 읽어도 똑같은 문자열을 팰린드롬 혹은 회문이라고 부른다. 어떠한 실수 N이 양의 정수이며, 십진수로 표현했을 때 팰린드롬이면 이 수를 팰린드롬 수라고 부른다.
어떠한 양의 정수 N에 대해서, N과 √N이 모두 팰린드롬이면 이 수를 제곱 팰린드롬 수 라고 부른다.
예를 들어, 121은 제곱 팰린드롬 수인데, 121이 팰린드롬이며, 121의 제곱근인 11 역시 팰린드롬이기 때문이다.

A 이상 B 이하 제곱 팰린드롬 수는 모두 몇 개인가?

[입력]
첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스의 첫 번째 줄에 A, B 가 주어진다. (1 ≤ A ≤ B ≤ 1000)

[출력]
각 테스트 케이스 마다 한 줄씩, 제곱 팰린드롬 수의 개수를 출력하라.

'''
