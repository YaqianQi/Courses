def check_prime(num):
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
              # print(num,"is not a prime number")
              # print(i,"times",num//i,"is",num)
               return False
       else:
           return True
           #print(num,"is a prime number")

res = [x if check_prime(x)!= True else (x,'prime')for x in range(10,51)]
print(res)