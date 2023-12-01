# Day 7:

from collections import defaultdict
from CY22 import input_load as load

input_file = load.txt_to_str('puzzle_input.txt')
data = input_file.strip()
lines = [x for x in data.split('\n')]

SZ = defaultdict(int)
filepath = []
for line in lines:
    words = line.strip().split()
    if words[1] == 'cd':
        if words[2] == '..':
            filepath.pop()
        else:
            filepath.append(words[2])
    elif words[1] == 'ls':
        continue
    elif words[0] == 'dir':
        continue
    else:
        sz = int(words[0])
        for i in range(1, len(filepath)+1):
            SZ['/'.join(filepath[:i])] += sz

total_ds = 70000000
used_ds = SZ['/']
ds_needed = 30000000
ds_to_free = used_ds - (total_ds - ds_needed)

ans1 = 0
ans2 = 1e9
for k,v in SZ.items():
    if v <= 100000:
        ans1 += v
    if v >= ds_to_free:
        ans2 = min(ans2, v)
print(ans1, ans2)