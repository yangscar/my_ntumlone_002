__author__ = 'neuralyang'

def Ein(N, sigma=0.1, d=8):
    return sigma**2*(1-float(d+1)/N)


print(Ein(500))
print(Ein(10))
print(Ein(1000))
print(Ein(25))
print(Ein(100))