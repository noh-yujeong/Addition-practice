import time

def menu_list():
    print(""" -----------------------------------------------------------------------------------                 
                                                        
                                                                                                            
                                            ll|||||||||||||||||||||||||lllllllllllllllllll                                       
                                          llll|||||||||||||||llllllllllllllllllll||||||||||||||||||||                    
                                         lllll                       llllll               
                                        llllll                        llllll|||          
                                       lllllll|||                          lllll|||l            
                                      lllllll||||||l                          ||||llllll  
                                           lll                          ||||llllll         
                                           lll                          |||llllll          
                                           lll                          |||||||
                                           ||||                         |||lllll           
                                           lll                         ||llll             
                                           lll                         lllll              
                                           lll                        lllll                
                                           lll                       lllll                    
                                           lll                      lllll                                   
                                           lllllllllllllllllllllllllllll||||||||||||||||||||||||||||                                           
                                           llllllllllllllllllllllllllll||||||||||||||||||||||||||||                                            
                                                                                                            
         """)
    print("------------------------------We have 4 types of Medical Product----------------------------------------")
    for i in range(1,5):
        print("------------------------------------------(",i,") ",dict_product_type[i][0],"------------------------------------------")
        print(dict_product_type[i][0],"`s price is ",dict_product_type[i][1],"won")
        time.sleep(0.5)
        print("we have", dict_product_type[i][0],": #",dict_product_amount[i])
        print("-----------------------------------------------------------------------------------------------------")
        time.sleep(1)
        
    
def visitor_information():
    flag=0
    access_admin=0
    while flag==0:
        ask=input("Do you want to buy something from us?:(Y or N)").upper()
        if ask=='Y':
            ask =True
            flag=1
        elif ask=='N':
            access_admin=input("Are You admisnistrator?:(Y or N)").upper()
            if access_admin=='Y':
                administrator()
                ask=False            
                flag=1
            elif access_admin=='N':
                ask=False            
                flag=1
            else:
                print("Sorry, You should give the Answer with Y or N!!!")
                time.sleep(0.5)
                print("Again I want to ask.")
                time.sleep(0.5)
        else:
            print("Sorry, You should give the Answer with Y or N!!!")
            time.sleep(0.5)
            print("Again I want to ask.")
            time.sleep(0.5)
    return ask



def get_order(dict_product_type,dict_product_amount):
    order=[]
    while True:
        type_of_product=int(input(">> Please Enter the type What you want to buy: "))
        if type_of_product!=1 and type_of_product!=2 and type_of_product!=3 and type_of_product!=4:
            print("You should enter the type between 1 to 4! ")
            time.sleep(0.5)
            continue
        else:
            amount_of_product=int(input(">>Please Enter the amount What you want to buy: "))
            time.sleep(0.5)
            if amount_of_product>dict_product_amount[type_of_product]:
                count=amount_of_product-dict_product_amount[type_of_product]
                print("there is some stocks of product ",type_of_product," less than you want.\n")
                print( "especially, product %d is now lack"%count)
            else:
                match.append(type_of_product)
                order.append(type_of_product)
                price=amount_of_product*(dict_product_type[type_of_product][1])
                small_order=[]
                small_match=[]
                small_order.append(amount_of_product)
                small_order.append(price)
                small_match.append(amount_of_product)
                small_match.append(0)
                match.append(small_match)
                order.append(small_order)
                break
    return order

#order=[1,[1,800]]->1번제품(type_of_product),1개(amount_of_product)
def get_money(order):
    payment=int(input("Your payment: "))
    i=payment//100
    while i>0:
        print(" kerplunk ")#딱하고 떨어지다라는 뜻
        time.sleep(0.2)
        i=i-1
    print("You paid %d."%payment)
    match[1][1]=payment
    if payment<int(order[1][1]):
        lack_price=order[1][1]-payment
        time.sleep(1)
        print("You have to give us, ",order[1][1],"and you paid ",payment," so you have to give more",int(lack_price))
        time.sleep(1)
        flag=0
        while flag==0:
            answer=int(input("(0)do you want to give us Or (1)do you want to give up to buy product?"))
            if answer==1:
                print("Thank you for using our service, 1st! I hope to see you again! Bye!")
                flag=1
                time.sleep(1)
                break
            elif answer==0:
                while payment!=order[1][1]:
                    extra_payment=int(input("pay more: "))
                    i=extra_payment//100
                    while i>0:
                        print(" kerplunk ")
                        time.sleep(0.2)
                        i=i-1
                    print("You paid %d."%extra_payment)
                    time.sleep(1)
                    match[1][1]=match[1][1]+extra_payment
                    if match[1][1]==order[1][1]:
                        time.sleep(0.5)
                        inventory(order)
                        print("You paid all!, It means " ,order[1][0], "of the product named ",dict_product_type[order[0]][0]," will come out! now:) ")
                        accumulated_orders(order)
                        time.sleep(0.5)
                        flag=1
                        break
                    elif match[1][1]>=order[1][1]:
                        time.sleep(1)
                        print("You paid too much, You give us more ", -(order[1][1]-match[1][1]))
                        time.sleep(1)
                        print("I will give you change, ",match[1][1]-order[1][1])
                        a=(match[1][1]-order[1][1])//100
                        while a>0:
                            print(" kerplunk ")#딱하고 떨어지다라는 뜻
                            time.sleep(0.5)
                            a=a-1
                        inventory(order)
                        print("You paid all!, It means " ,order[1][0], "of the product named ",dict_product_type[order[0]][0]," will come out! now:) ")
                        accumulated_orders(order)
                        time.sleep(0.5)
                        match[1][1]=order[1][1]
                        flag=1
                        break
                    elif match[1][1]<=order[1][1]:
                        time.sleep(1)
                        print("You have to pay  more", order[1][1]-match[1][1])
                        time.sleep(1)
                        continue
            else:
                print("You have to give us the answer which is 0 or 1.")
                time.sleep(1)
                continue
    elif payment==int(order[1][1]):
        time.sleep(0.5)
        inventory(order)
        print("You paid all!, It means ", order[1][0], "of the product named ",dict_product_type[order[0]][0]," will come out! now:) ")
        accumulated_orders(order)
        time.sleep(3)
    else:
        time.sleep(0.5)
        print("You paid too much, You give us more ", -(order[1][1]-match[1][1]))
        time.sleep(1)
        print("I will give you change, ",match[1][1]-order[1][1])
        a=(match[1][1]-order[1][1])//100
        while a>0:
            print(" kerplunk ")#딱하고 떨어지다라는 뜻
            time.sleep(0.5)
            a=a-1
        inventory(order)
        print("You paid all!, It means ", order[1][0], "of the product named ",dict_product_type[order[0]][0]," will come out! now:) ")
        accumulated_orders(order)
        time.sleep(2) 
    

def try_to_buy(count):

    while True:
        menu_list()
        #print(dict_accumulated_orders)
        count=count+1
        print("----------------------------------------------")
        print("Hi, This time, Your Visiting is ",count," times!:)")
        time.sleep(1.5)
        controller=visitor_information()
        if controller==False:
            print("Okay, Then Please visit us later~!.")
            break
        else:
            confirm_order=get_order(dict_product_type,dict_product_amount)
            ordered_type=confirm_order[0]
            print("You ordered %s."%dict_product_type[ordered_type][0])
            time.sleep(1.5)
            print("and the ordered amount is ",confirm_order[1][0])
            time.sleep(1.5)
            print("so, the total price is %d."%confirm_order[1][1])
            time.sleep(2)
            print("----------------------------------------------")
            print("Therefore, You have to give us %d won.:)"%confirm_order[1][1])
            print("----------------------------------------------")
            time.sleep(1.5)
            get_money(confirm_order)

def inventory(order):
    a=order[0]
    dict_product_amount[a]=dict_product_amount[a]-order[1][0]

def accumulated_orders(order):
    dict_accumulated_orders[order[0]][0]=dict_accumulated_orders[order[0]][0]+order[1][0]
    dict_accumulated_orders[order[0]][1]=dict_accumulated_orders[order[0]][1]+order[1][1]
    
def administrator():
    print("Hi, administrator!")
    for i in range(1,5):
        print("------------------------------------------(",i,") ",dict_product_type[i][0],"------------------------------------------")
        print("We earn money from selling the ",dict_product_type[i][0]," and the profit is ",dict_accumulated_orders[i][1]," won")
        time.sleep(0.5)
        print("Especially, we Sell", dict_product_type[i][0],": #",dict_accumulated_orders[i][0])
        time.sleep(0.5)
        print("So, we have, Now,", dict_product_type[i][0],": #",dict_product_amount[i])
        print("-----------------------------------------------------------------------------------------------------")
        time.sleep(1)
    
#if__name__=="__main__":##########################################

#변수지정
dict_product_type={1:['ToothBrush',800],2:['ToothPaste',600],3:['Tylenol',300],4:['MuscleSpray',900]}
dict_product_amount={1:100,2:100,3:100,4:100}
dict_accumulated_orders={1:[0,0],2:[0,0],3:[0,0],4:[0,0]}
match=[]
count=0

#함수 부르기(호출)
try_to_buy(count)

