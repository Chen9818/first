def o():
    B=10
    def INNER(x):
        return 5*x+B
    return INNER()

B=5
f=o()
print(f(B))