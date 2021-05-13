import random

bubble = [1, 2, 3, 4, 5, 6, 7, 8]
bubble
completeBubble = []
idx = 1
_len = len(bubble)
while idx <= _len:
    num = random.choice(bubble)
    bubble.remove(num)
    completeBubble.append(num)
    idx += 1
print(completeBubble)

print("버블 정렬 수행")

for i in range(_len - 1):
    for j in range(_len - i - 1):
        if completeBubble[j] > completeBubble[j + 1]:
            tmp = completeBubble[j]
            completeBubble[j] = completeBubble[j + 1]
            completeBubble[j + 1] = tmp


print(completeBubble)