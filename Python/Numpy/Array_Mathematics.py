import numpy as np
n, m = (int(s) for s in input().split())
a, b = (np.fromiter((s for _ in range(n) for s in input().split()), dtype=np.int64).reshape((n, m)) for _ in range(2))
print("\n".join(str(op(a, b)) for op in (np.add, np.subtract, np.multiply, np.floor_divide, np.mod, np.power)))