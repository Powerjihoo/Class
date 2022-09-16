def calculate(cal):    
    if cal == '+':
        print('##계산기' , first_num , '+' , second_num ,'=', first_num+second_num)
    elif cal == '-':
        print('##계산기' , first_num , '-' , second_num ,'=', first_num-second_num)
    elif cal == '/':
        if second_num==0:
            print('0으로는 나누면 안됩니다 ㅠㅠ')
        else:
            print('##계산기' , first_num , '/' , second_num ,'=', int(first_num/second_num))
    elif cal == '**':
        print('##계산기' , first_num , '**' , second_num ,'=', first_num**second_num)
    else :
        print('올바른 계산식을 입력해주십시오')
   
first_num=int(input('첫번째 수를 입력하세요 : '))
cal=input('계산을 입력하세요(+,-,/,**) : ')
second_num=int(input('두번째 수를 입력하세요 :'))     
calculate(cal)