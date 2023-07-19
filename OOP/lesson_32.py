class DefenedVector:

    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp

        return False


v1 = [1, 2, 3]
v2 = [3, 4, 5]

try:
    with DefenedVector(v1) as dv:
        for idx, i in enumerate(dv):
            dv[idx] += v2[idx]
except:
    print("Error")

print(v1)