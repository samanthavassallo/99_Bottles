#Sam Vassallo
beers = int(input("How many beers are on the wall?"))
def sing(beers):
    for i in range(beers):
        print(beers,"bottles of beer on the wall",beers,"bottles of beer")
        beers = beers - 1
        print("take on down pass it around", beers , "bottles of beer on the wall")
sing(beers)

#n = int(input("what number do you want to use"))
def SumofSquares(n):
    for _ in range (n):
        total = 0
        for _ in range (n):
            total = total + n**2
            n=n-1
        print(total)
#SumofSquares(n)
"""
    n = 0
    for i in range(1, n+1):
        n = n + (n * n)
    return n 
  """  
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
def table(n):
    num1 = 1
    num2 = 1
    num3 = 1
    for _ in range (n):
        for _ in range (n):
            print(num1, end="    ")
            num1=num1+num2
        print()
        num1=num3+1
        num2=num2+1
        num3=num3+1
        
#table(5)
        
    

        
    
