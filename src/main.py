from god import god_kr

if __name__=="__main__":
    bot=god_kr()

    while True:
        user_input=input("You: ")
        response=bot.ask(user_input)
        print("Krishna:", response)
