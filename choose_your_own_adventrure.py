name = input("Type your adventurer name! ")
print("Welcome " + name)

option = input("You are on a dirt road and you have an option to go left or right. Which do you pick? ").lower()

if option == "left":
    option = input("You come across a raging river! Do you swim across or go around? (swim/around) ")

    if option == "swim":
        option = input("You made it across! But you meet a scary stranger. Do you greet them or walk away? (greet/walk) ")

    if option == "walk":
        print("Oh no! The scary stranger was offended and they... You lose!")

        if option == "greet":
            print("Yay! The scary stranger wasn't so scary and they gave you a bag of gold! YOU WIN!")

    if option == "around":
        print("You went around and met a dead end! Game over! ")
  

elif option == "right":
    option = input("You meet a cute cat! Do you pet the cat or walk away? (pet/walk) ")

    if option == "pet":
        print("You made a new friend! But this is a dangerous adventure so you lose!")

    if option == "walk":
        option = input("The cat is sad...but you now have come across a bag of gold! Do you take it or leave it? (take/leave) ")
        if option == "take":
            print("You stole? Tut tut. Game over!")
        if option == "leave":
            print("Well done for leaving the bag of gold! You have been rewarded with winning the game!")

else:
    print("You lose!" + name + "." + " Try again next time!")
