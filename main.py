from dad_jokes_functions import *


def main():

    heading()

    while True:
        user = input("I have lots of cool jokes! Give me a topic:")
        print("\n")
        joke(user)
        again = input("Do you want to hear another joke?(Y/N) ").lower()
        print("\n")

        if again == "y":
            continue
        else:
            print("Thanks for reading my corny jokes :)")
            print("Come again next time!!!")
            break


if __name__ == "__main__":
    main()
