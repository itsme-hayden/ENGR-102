#quiz lock in

import numpy

f = open("module12quizF24.txt",'r')

arr = numpy.arange(100).reshape(10, 10)
c = 0

dick = {
    '0':0,
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0
}

for i in f:
    dick[i.strip()] += 1
    numpy.put(arr, [c], [i])
    c += 1
f.close()
print(dick)
print(arr[6])
c5 = 0
r7 = 0
for i in arr:
    c5 += i[4]
for i in arr[6]:
    print(i)
    r7 += i
#print(c5)
#print(r7)
mode_max = 0
mode = -100
for i in range(10):
    mode_max = max(mode_max, dick[str(i)])
    if dick[str(i)] == mode_max:
        mode = i
print(mode)

key = (r7 - c5 + mode)
print(key)
txt = "IOUBWRMCLNLIOMAVPETGINERMHRNSFOSPAG"

i = 0
ans = ""
while len(ans) != len(txt):
    ans += txt[i]
    i = (i + key) % len(txt)
    print(i)
print(ans)
print(len(txt))


