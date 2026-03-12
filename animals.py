def main():
    while True:
        ## Skriv ut menyvalen
        print("1. Cat")
        print("2. Dog")
        print("3. Cow")
        print("Enter x to exit")

        choice = input("Enter your selection")
        match choice.lower():
            case '1': #Cat-sound
                print("Mjau, mjau")
            case '2': #Dog-sound
                print("voff, voff")
            case '3ä': #Cow-sound
                print("Muuu, muuu")
            case 'x': #Exit
                break
            case _:
                print(f"Unrecognized input {choice}")

if __name__ == '__main__':
    main()
