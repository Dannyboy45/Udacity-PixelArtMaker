import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 == response:
            break
        elif option2 == response:
            break
        else:
            print_pause("Sorry, I don't understand")
    return response


def vehicle_options():
    return random.choice(['zamboni', 'motorcycle', 'tank', 'car'])


def intro():
    print_pause("You recently bought yourself a brand new % s." % rnd_veh)
    print_pause("You decide to take it for a ride.")


def gas_station(items):
    print_pause("You choose to drive to the"
                " nearest gas station to fill up on gas.")
    print_pause("You arrive at the gas station.")

    if "gas" in items:
        print_pause("You already filled up on gas, you're good to go!")

    else:
        print_pause("You top up on gas.")
        print_pause("You now have enough gas to get to the service station!")

        items.append("gas")
    print_pause("You hop back in your % s." % rnd_veh)
    drive_car(items)


def service_station(items):
    print_pause("You're on your way to the service station.")

    if "gas" in items:
        print_pause("You make it to the service station.")
        print_pause("After getting your % s inspected you find out nothing is"
                    " wrong with it." % rnd_veh)
        print_pause("All is well!")

    else:
        global remaining_walks
        remaining_walks -= 1

        print_pause("Oh no! You ran out of gas on your way to the service"
                    " station.")

        if remaining_walks == 0:
            print_pause("You're tired, you cannot walk anymore. You lost.")
            play_again()

        print_pause("You walk to the nearest gas station and fill up a small"
                    " gas tank "
                    "which you use to fill up your % s." % rnd_veh)
        print_pause("You can walk % s more time(s)." % remaining_walks)

        drive_car(items)


def drive_car(items):
    print_pause("Please enter the number for the location you want to"
                " drive to:")

    response = valid_input("1. gas station\n"
                           "2. service station\n",
                           "1", "2")

    if "1" in response:
        gas_station(items)
    elif "2" in response:
        service_station(items)


def play_game():
    global rnd_veh
    rnd_veh = vehicle_options()

    global remaining_walks
    remaining_walks = 3

    items = []
    intro()
    drive_car(items)
    play_again()


def play_again():

    response = valid_input("Would you like to play again?\n"
                           "Please say 'yes' or 'no'.\n",
                           "yes", "no")
    if "no" in response:
        print_pause("OK, goodbye!")
        exit()
    elif "yes" in response:
        play_game()


play_game()
