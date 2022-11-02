import time
from playsound import playsound

user_input = int(input("Enter the number of seconds: "))


def create_counter(input: int):
    while input > 0:

        min: int = input//60
        sec: int = input % 60

        print(f"{min}:{sec}")
        time.sleep(1)

        input -= 1

    print("Time Up!")
    playsound('sound.wav')


create_counter(user_input)
