def greet():
    name = input("Enter your name: ")
    hometown = input("Where are you from? ")
    print('Very nice to meet you, {}!'.format(name), f'from {hometown}!')

def main():
    greet()

if __name__ == "__main__":
    main()

