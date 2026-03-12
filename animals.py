def main():
    while True:
        ## Skriv ut menyvalen
        print("1. Cat")
        print("2. Dog")
        print("3. Duck")
        print("Enter x to exit")

        choice = input("Enter your selection")
        match choice.lower():
            case '1': #Cat-sound
                print("Meow, meow")
            case '2': #Dog-sound
                print("Woof, woof")
            case '3': #Duck-sound
                print("Quack, quack")
            case 'x': #Exit
                break
            case _:
                print(f"Unrecognized input {choice}")

if __name__ == '__main__':
    main()
