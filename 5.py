
import math
def compute():
	ans = math.lcm(*range(1, 21))
	return str(ans)
print(compute())