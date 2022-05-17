original_num = set(range(1, 10001)) # 중복함수 제거를 위한 set함수
generated_num = set() # 중복 처리를 위한 셀프 넘버 배열

# 1 ~ 10001번까지 반복문이 돌면서 i에 대한 i + i[j].. = i 에 넣어주고 이렇게 생성된 셀프 넘버를
# generated_num 에 add를 통해서 넣어준다. 그 뒤에 org_num - generated_num 을 뺀 값이 답

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = sorted(original_num - generated_num)
for i in self_num:
    print(i)
