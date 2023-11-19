OFFSET = 1000
MAX_R = 2000

n = int(input())
segments = []

cur = 0

for _ in range(n):
    distance, direction = tuple(input().split())
    distance = int(distance)

    if direction == 'L':
        section_left = cur - distance
        section_right = cur
        cur -= distance
    else:
        section_left = cur
        section_right = cur + distance
        cur += distance

    segments.append([section_left, section_right])

checked = [0] * (MAX_R + 1)

for x1, x2 in segments:
    x1 , x2 = x1 +OFFSET,x2+OFFSET
    for i in range(x1, x2):
        checked[i] += 1

cnt = 0
for elem in checked:
    if elem >= 2:
        cnt += 1
print(cnt)