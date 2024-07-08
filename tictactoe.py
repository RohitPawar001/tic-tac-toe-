import random 

gameboard = ["-","-","-","-","-","-","-","-","-"]
available_places = [0,1,2,3,4,5,6,7,8]
winner = None
game_running = True

def game_board():
    print(gameboard[0]," | ",gameboard[1]," | ",gameboard[2])
    print("--------------")
    print(gameboard[3]," | ",gameboard[4]," | ",gameboard[5])
    print("--------------")
    print(gameboard[6]," | ",gameboard[7]," | ",gameboard[8])   
                  
def computer_choice():
    random_choice = random.choice([0,1,2,3,4,5,6,7])
    if gameboard[random_choice] == "-":
        gameboard[random_choice] = "O"
        available_places.remove(random_choice)
            
def checkwinner():
    global game_running
    if check_hori(gameboard):
        print(f"the winner is {winner}")
        game_running = False
    elif check_vert(gameboard):
        print(f"the winner is {winner}")
        game_running = False
    elif check_diag(gameboard):
        print(f"the winner is {winner}")
        game_running = False
    elif "-" not in gameboard:
        print("its a tie")
        game_running = False

def check_hori(gameboard):
    global winner
    if gameboard[0]==gameboard[1]==gameboard[2] and gameboard[0] != "-" :
        winner = gameboard[0]
        return True
    elif gameboard[3]==gameboard[4]==gameboard[5] and gameboard[3] != "-" :
        winner = gameboard[3]
        return True
    elif gameboard[6]==gameboard[7]==gameboard[8] and gameboard[6] != "-" :
        winner = gameboard[6]
        return True
    
def check_vert(gameboard):
    global winner
    if gameboard[0]==gameboard[3]==gameboard[6] and gameboard[0] != "-":
        winner = gameboard[3]
        return True
    elif gameboard[1]==gameboard[4]==gameboard[7] and gameboard[1] != "-" :
        winner = gameboard[4]
        return True
    elif gameboard[2]==gameboard[5]==gameboard[8] and gameboard[2] != "-":
        winner = gameboard[2]
        return True
    
def check_diag(gameboard):
    global winner
    if gameboard[0]==gameboard[4]==gameboard[8] and gameboard[4] != "-" :
        winner = gameboard[0]
        return True
    elif gameboard[2]==gameboard[4]==gameboard[6] and gameboard[2] != "-" :
        winner = gameboard[2]
        return True
    
def play():
    while game_running:
            
        place = int(input(f"enter the place to put your mark on from {available_places}"))
        if place in available_places and gameboard[place] == "-":
            gameboard[place] = "X"
            available_places.remove(place)
            checkwinner()
            computer_choice()
            game_board()
            checkwinner()
        else:
            print("the place has been already taken please enter another position")
            
def main():
    choice = input("do you want to play the game (y/n)").lower()
    if choice == "y":
       print("you : X \n computer : O")
       play()
    else:
        print("thank you")

if __name__ == "__main__":
    main()