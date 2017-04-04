import sys
import math

print(18)
nums = []
for line in sys.stdin:
    for word in line.split():
        nums.append(float(word))

nums.reverse()
for num in nums:
    print("%.4f" % math.sqrt(num))
