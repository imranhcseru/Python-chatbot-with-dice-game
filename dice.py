def get_result(num):
    if(num == 6):
        print("                                         -------                                            ")
        print("                                        | 0   0 |                                           ")
        print("                                        |       |                                           ")
        print("                                        | 0   0 |                                           ")
        print("                                        |       |                                           ")
        print("                                        | 0   0 |                                           ")
        print("                                         -------                                            ")
        value = num
        
    elif(num == 5):
        print("                                         -------                                            ")
        print("                                        | 0   0 |                                           ")
        print("                                        |       |                                           ")
        print("                                        |   0   |                                           ")
        print("                                        |       |                                           ")
        print("                                        | 0   0 |                                           ")
        print("                                         -------                                            ")
        value = num
    elif(num == 4):
        print("                                         -------                                            ")
        print("                                        | 0   0 |                                           ")
        print("                                        |       |                                           ")
        print("                                        |       |                                           ")
        print("                                        |       |                                           ")
        print("                                        | 0   0 |                                           ")
        print("                                         -------                                            ")
        value = num
        
    elif(num == 3):
        print("                                         -------                                            ")
        print("                                        |     0 |                                           ")
        print("                                        |       |                                           ")
        print("                                        |   0   |                                           ")
        print("                                        |       |                                           ")
        print("                                        | 0     |                                           ")
        print("                                         -------                                            ")
        value = num
        
    elif(num == 2):
        print("                                         -------                                            ")
        print("                                        |       |                                           ")
        print("                                        |       |                                           ")
        print("                                        | 0   0 |                                           ")
        print("                                        |       |                                           ")
        print("                                        |       |                                           ")
        print("                                         -------                                            ")
        value = num
        
    elif(num == 1):
        print("                                         -------                                            ")
        print("                                        |       |                                           ")
        print("                                        |       |                                           ")
        print("                                        |   0   |                                           ")
        print("                                        |       |                                           ")
        print("                                        |       |                                           ")
        print("                                         -------                                            ")
        value = num
        
    return value

def scoreboard(total_user,total_computer,result):
    print("======================================================================================================")
    print("                                                                                           ")
    print("                                     Your score : {0}                                           ".format(total_user))
    print("                                       My score: {0}                                         ".format(total_computer))
    print("                                         {0}                                                           ".format(result))
    print("                                                                                           ")
    print("======================================================================================================")


def user_try():   
    import random
    import time
    turn = int(input("                               How many turn would you play:"))
    total_user = 0
    total_computer = 0
    while(turn>0):
        print("                                        Your Turn")
        u_turn = str(input("                                Enter 'Y' to roll the dice:"))
        if(u_turn == 'y' or u_turn == 'Y'):
            num = random.randint(1,6)
            total_user += get_result(num)
        print("                                      My Turn")
        time.sleep(3)
        num = random.randint(1,6)
        total_computer += get_result(num)
        turn = turn -1

    if(total_user == total_computer):
        result = "Draw Better Try Again!"
    elif(total_user>total_computer):
        result = "You Win!"
    else:
        result = "I Win"
    scoreboard(total_user,total_computer,result)
        
def game():
    while(True):
        print("                                       Wanna Play?")
        choice = str(input("                            'Y' to Start The Game 'X' for Exit:"))
        if(choice == 'Y' or choice == 'y'):
            user_try()
        elif(choice == 'X' or choice == 'x'):
            break
        else:
            print("                                         Invalid Choice.")
if __name__=='__main__':
    main()