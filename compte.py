import random 
import time
start_time = time.time()

target = random.randint(100,999)

possibles = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,25,50,75,100]
operations = ['+','-','*','/']
picked = []
maxLengthList = 6
auto = input("Do you want random variables ?(y/n) : ")
if auto == 'y':
    for i in range(6):
        index = random.randint(0,len(possibles)-1)
        picked.append(possibles[index])
        possibles.pop(index)
else:
    target = int(input("Give the target number : "))
    while len(picked)<maxLengthList:
        picked.append(int(input("Enter the number to your list : ")))

def addition(num1,num2):
    return num1+num2
def subtraction(num1, num2):
    if num1> num2:
        return num1 - num2
    else:
        return num2-num1
def multiply(num1, num2):
    return num1 * num2
def realDivision(num1, num2):
    if num1> num2:
        if (num1 / num2).is_integer():
            return int(num1 / num2)
        else:
            return 0
    else:
        if (num2/num1).is_integer():
            return int(num2/num1)
        else:
            return 0
def switch(op,num1,num2):
    op_dic = {'+':addition(num1,num2),
            '-':subtraction(num1,num2),
            '*':multiply(num1,num2),
            '/':realDivision(num1,num2),
    }
    return op_dic.get(op)


diff = 1000
best = 0
cur = ''
second = []
third = []
fourth = []
fith = []

def test(lst,answer):
    dic = {}
    global best,cur,diff
    for num in lst:
        if num == target: return answer
        else:

            for ind1 in range(len(lst)):
                for ind2 in range(len(lst)):
                    if ind1 >= ind2 : pass
                    else:    
                        for op in operations:
                            new = switch(op,lst[ind1],lst[ind2])
                            if new == 0:break
                            temp = []
                            temp.append(new)
                            for index in range(len(lst)):
                                if index != ind1 and index != ind2:
                                    temp.append(lst[index])
                            dic[answer + f'{lst[ind1]} {op} {lst[ind2]} = {new} |'] = temp
            return dic

def final_steps():
    global best,cur,diff

    for key, value in first.items():
        if isinstance(test(value,key),str):
            return(test(value,key))
        else:
            second.append(test(value,key))

    for dictio in second:
        for key, value in dictio.items():
            if isinstance(test(value,key),str):
                return(test(value,key))
            else:
                third.append(test(value,key))

    for dictio in third:
        for key, value in dictio.items():
            if isinstance(test(value,key),str):
                return(test(value,key))
            else:
                fourth.append(test(value,key))

    for dictio in fourth:
        for key, value in dictio.items():
            if isinstance(test(value,key),str):
                return(test(value,key))
            else:
                fith.append(test(value,key))  

    for dictio in fith:
        for key, value in dictio.items():
            if value[0] == target:
                return(key)
            else:
                if subtraction(value[0],target) < diff: 
                    diff = subtraction(value[0],target)
                    best = value[0]
                    cur = key
    return 0

print(f'The list of number is {picked}, the target number is {target}')
result = input("Do you want the solution ?(y/n) : ")
if result == 'y':
    first = test(picked,'')
    if final_steps() == 0:
        print(f"Can't be done, closest number is {best} with {cur}")
    else:print(final_steps())
    print(f'The list of number is {picked}, the target number is {target}')
    print("--- %s seconds ---" % (time.time() - start_time))

