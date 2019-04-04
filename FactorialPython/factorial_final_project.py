def factorial(number):
    product = 1  

    for i in range(number): 
        print (product, " * ", i+1)
        product = product * (i+1) 
    return product

#input_key = int(input("please introduce an integer number: ")) 
#factorial_input_user = factorial(input_key)
#print (factorial_input_user)
   
    