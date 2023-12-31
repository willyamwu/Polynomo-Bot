import updatedbills
import enacted
import nomination
import CONSTANTS


def main():
    print("Target Date:", CONSTANTS.yesterday_date_string)
    command_finder()


# Asks for a command
def command_finder():
    while(True):
        user_input = input(CONSTANTS.start_up_prompt)
        if user_input == "1":
            print("Daily Update -- SELECTED")
            nomination.run()
            enacted.run()
            break
        elif user_input == "2":
            print("Print -- SELECTED")
            break
        else:
            print("INVALID INPUT")


if __name__ == "__main__":
    main()
