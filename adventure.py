#Alan
#Adventure
#a simple text based adventure game
def adventure_game():
    print("You have to escape this secret room. There's two ways out, one good one not so good. Good luck :P")
    door_one=input("You have two doors to go through. One contains a snake and another contains a heavily mutated rat. Pick one by typing snake or rat. ")
#Door One
    if door_one == "rat":
        exit_one=input("That rat was HUGE.. You made it to the next door, but you are kinda bruised. Two more doors, one will let you out to freedom and one won't. Left or right? ")
        if exit_one == "right":
            print("You made it out of the room! You have been given 6.7 million dollars as a reward! You are now out of debt and successful! Everyone loves you now! <3")
        elif exit_one == "left":
            print("You exited into another room filled with exposed electrical wires. Must be a terrible death for you! Sorry :(")
#Door Two
    elif door_one == "snake":
        exit_two=input("The snake bit you! You made it to the next door, but you're very weak. You either get out or you don't. Left or right? ")
        if exit_two == "left":
            print("You made it out! Sadly, the snake's venom killed you before you made it out.")
            print("Achievement Unlocked: Sad Ending")
        elif exit_two == "right":
            print("You seem to have made it to a hospital. You end up in a hospital bed but die due to significant blood loss. Turns out the hospital wasn't a real hospital.. Oops. :(")
    print("Thanks for playing <3")
adventure_game()
