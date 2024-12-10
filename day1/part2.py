import os, sys
sys.path.append(os.path.abspath('./'))

from part1 import list1, list2

print(list1)
print(list2)

counts = {}
n = 0
for i in list1:
    counts[i] = list2.count(i)

similarity_score = []
for key, value in counts.items():
    score = key * value
    similarity_score.append(score)

print(sum(similarity_score))