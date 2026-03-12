def main():
    while True:
        ## Skriv ut menyvalen
        print("1. Cat")
        print("2. Dog")
        print("3. Cow")
        print("4. Duck")
        print("5. Horse")
        print("6. Sheep")
        print("Enter x to exit")

        choice = input("Enter your selection")
        match choice.lower():
            case '1': #Cat-sound
                print("Meow meow")
            case '2': #Dog-sound
                print("Woof woof") 
            case '3': #Cow-sound
                print("Moo moo")
            case '4': #Duck-sound
                print("Quack quack")
            case '5': #Horse-sound
                print("Neigh neigh")
            case '6': #Sheep-sound
                print("Baa baa")
            case 'x': #Exit
                break
            case _:
                print(f"Unrecognized input {choice}")

if __name__ == '__main__':
    main()
