# note #4 p.27 ~
# 과제 21 ~ 24

# 과제 21
text = input('문자열을 입력해 주세요: ')
text = text.replace('Hello','Hi')
print(text)

# 과제 22 입력해 주세요: ')
text2 = input('문자열을 입력해 주세요: ')
print("/".join(text2))

# 과제 23
name = input('이름을 입력해 주세요: ')
new_name = name.lower()
print(new_name.rjust(10))

# 과제 24
price = input('가격들을 입력해 주세요: ')
prices = list(map(int, price.split(";")))
prices.sort(reverse=True)

for p in prices:
    print(str(p).rjust(9))