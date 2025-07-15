lines = [line for line in open('9.txt')]

cnt = 0
for line in lines:
    mas = sorted([int(x) for x in line.split()])
    if 0 < mas[0] < 90 and mas[1] == mas[2] == 90 and mas[3] > 90 and sum(mas) == 360: cnt += 1

print(cnt)



