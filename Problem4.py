#Problem4.py
#Project Euler problem 7

from NumberTests import isPrime


def main():
 index=0
 for num in range(2,10001):
   if isPrime(num)==True:
     list=(num)
     print (list)
  
     

    


  

          



if __name__ == '__main__':
  main()