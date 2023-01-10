import numbers

"""
def check_non_int(num):
        try:
            #if isinstance(num,int):
            num=int(num)
            return num
        except ValueError:
             return('Please enter an integer')"""

"""def string2int(sti):
    try:
        num1= input("Enter 1st no:")
        num2= input("Enter 2nd no:")
        return num
    except ValueError:
        raise SyntaxError('not an integer') """

"""def handle_int_inp():
    try:
        num1 = int(input("enter no:"))
        num2 = int(input("enter no:"))
        #res=num1+num2
        res_sum = num1 + num2
        print(res_sum)
        #return res_sum
    except ValueError as e:
        print("Not a proper integer! Try it again")
handle_int_inp()"""


"""
inp1 = input("Input: ")
inp2 = input("Input: ")
try:
    a = int(inp1)
    b = int(inp2)
except ValueError:
    print("invalid input", inp1 & inp2, ". You should enter a number. Please retry")                
"""
        #except ValueError:
         #   num1=float(num1)
          #  return num1
"""        
num1= input("Enter 1st no:")
num_1 = string2int(num1)
print("num1",type(num_1))
num2= input("Enter 2nd no:")
num_2 = string2int(num2)
print("num2",type(num_2))
#print(type(num1))
#print(type(num2))

if isinstance(num1,int) and isinstance(num1,int):
    num1 = int(num1)
    num2 = int(num2)
elif isinstance(num1,float) and isinstance(num1,float):
    num1 = float(num1)
    num2 = float(num2)

res = num1 + num2
print(res)

#print(type(num1))
#print(type(num2))
#if int(num1) or float(num2):
    #5.3res = num1 + num2



#print(isinstance(num1,numbers.Number))


#print(type(num1))
#print(type(num2))
#res = num1 + num2
#print("The sum is ",res)
"""

def chk_user_inp(usr_inp1,usr_inp2):
    try:
        # Convert it into integer
        val1 = int(usr_inp1)
        val2 = int(usr_inp2)
        res_sum = val1 + val2
        print(res_sum)
        #return res_sum
    except ValueError:
        try:
            # Convert it into float
            val1 = float(usr_inp1)
            val2 = float(usr_inp2)
            res_sum = val1 + val2
            print(res_sum)
            #return res_sum
        except ValueError:
            print("No input is not a number. It's a string")

inp1 = input("Enter num: ")
inp2 = input("Enter num: ")
chk_user_inp(inp1,inp2)
   