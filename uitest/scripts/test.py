
def sum(a):
    def _sum(b):
        return a+b
    return _sum

print(sum(5), (5))