# note #3 p.51 ~
# 과제 11 ~ 20

# 과제 11
nums = list(map(int, input('숫자 5개를 입력하세요: ').split()))
char = input('문자 1개를 입력하세요: ')
nums.append(char)
print(nums)

# 과제 12
nums = list(map(int, input('숫자 5개를 입력하세요: ').split()))
del nums[-2:]
print(nums)

# 과제 13
nums = list(map(int, input('숫자 5개를 입력하세요: ').split()))
for index, value in enumerate(nums, start=101):
    print(index, value)

# 과제 14
a = [10, 20, 30, 40, 30, 20, 10]
print(a.count(20))

# 과제 15
nums = list(map(int, input('숫자 10개를 입력하세요: ').split()))
print('최저값: ', min(nums))
print('최고값: ', max(nums))

# 과제 16
nums = list(map(int, input('숫자 10개를 입력하세요: ').split()))
nums.remove(min(nums))
nums.remove(max(nums))
print('최저값과 최고값을 제외한 나머지 값들의 합은: ', sum(nums))

# 과제 17
a = [10, 20, 30, 40, 30, 20, 10]
a = [i for i in a if i != 20]
print(a)

# 과제 18
mylist = [i for i in range(0, 10)]
print(mylist)

# 과제 19
mylist2 = [i for i in range(1, 21) if i % 2 == 1]
print(mylist2)

# 과제 20
start, end = (map(int, input('두 정수를 입력하세요: ').split()))
powers = [2 ** i for i in range(start, end +1)]

if len(powers) >= 2:
    del powers[1]
if len(powers) >= 1:
    del powers[-1]

print(powers)
