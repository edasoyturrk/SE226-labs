def factorial(x):
    if x==0 or x==1:
        return 1;
    else:
        return x * factorial(x-1)

step = lambda x,n: ((-1)**n) * (x**(2*n+1)) / factorial(2*n+1)

def sine_x(x,n):
    x=x*numpy.pi/180
    total = 0
    for i in range(n):
        total+=step(x,i)
    return total
x = float(input("Enter x in degrees: "))
n = int(input("Enter number of terms (n): "))
    
ftotal = 0

def function(n):
    """
    Computes the n-th harmonic number recursively.
    Uses a global variable ftotal to store the sum.
    """
    global ftotal
    if n == 0:  
        return
    function(n - 1)  
    ftotal += 1 / n  


n = int(input("Enter n for harmonic function: "))
function(n)
print(f"Harmonic function result for {n} = {ftotal}")
    

    
