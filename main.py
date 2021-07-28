print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))
health = 10

if age < 18:
    print("You are not old enough to play this game")
else:

    print("Let's play!")
    print("You are starting with", health, " health")
    l_or_r = input("First choice..left or right(left/right)?")
    if l_or_r == "left":
        answr = input(
            "Nice! you reach a lake,do you swim across  or go around(across/around)?"
        )
        if answr == "around":
            answr = input(
                "You reach a forest and you see a cabin.Do you go inside cabin or move forward(inside/move)?"
            )

            if answr == "inside":

                health -= 10
                print("There is a killer inside! you've been killed!")
                print("health:", health, "You lost!")

            else:

                answr = input(
                    "You reach a cliff.There is no way out!Do you jump or go back to forest(jump/go back)?"
                )
                if answr == "jump":
                    health -= 10
                    print("You've died!")
                    print("health:", health, "You lost!")

                else:
                    print("You can't go back,you've lost the way!")
                    health -= 10
                    print("health:", health, "You lost!")

        else:
            print(
                "You reached the other side of the lake,but bit by a crocodile.You've lost 5 health."
            )
            health -= 5
            answr = input(
                "Now you see a person who sleeping on the ground.Do you wake him up or leave him(wake him up/leave)?"
            )
            if answr == "wake him up":
                print("The person helps you to go back to your home.")
                print("You win!")
            else:
                answr = input(
                    "You see a hungry wolf,it starts to chase you.You see two paths.left or right(left/right)?"
                )
                if answr == "left":
                    health -= 5
                    print("You reach the end of the path,Wolf attacks you!")
                    print("health:", health, "You lost!")
                else:
                    answr = input(
                        "You manage to escape from wolf.There is a table full of meals.Do you eat or leave(eat/leave)?"
                    )
                    if answr == "eat":
                        health -= 5
                        print("You are poisoned!")
                        print(
                            "health:",
                            health,
                            "You lost!",
                        )
                    else:
                        health -= 5
                        print(
                            "Now you are starving,you feel exhausted.You can't keep going anymore"
                        )
                        print(
                            "health:",
                            health,
                            "You lost!",
                        )
    else:
        print("Too bad!You fall into a hole and you can't get out")
        health -= 10
        print(
            "health:",
            health,
            "You lost!",
        )

print("\nThank you for playing! :)")
