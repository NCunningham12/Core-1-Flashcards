import random

cards = [
    {
        "question": "FTP",
        "answer": "20/21",
        "correct": False
    },
    {
        "question": "Telnet",
        "answer": "23",
        "correct": False
    },
    {
        "question": "SMTP",
        "answer": "25",
        "correct": False
    },
    {
        "question": "POP3",
        "answer": "110",
        "correct": False
    },
    {
        "question": "IMAP",
        "answer": "143",
        "correct": False
    },
    {
        "question": "DNS",
        "answer": "53",
        "correct": False
    },
    {
        "question": "HTTP",
        "answer": "80",
        "correct": False
    },
    {
        "question": "HTTPS",
        "answer": "443",
        "correct": False
    },
    {
        "question": "RDP",
        "answer": "3389",
        "correct": False
    },
    {
        "question": "SNMP",
        "answer": "161/162",
        "correct": False
    },
    {
        "question": "DHCP",
        "answer": "67/68",
        "correct": False
    },
]

def reset_cards():
    for card in cards:
        card["correct"] = False

def restart_game():
    restart = input("\n\nWould you like to restart?\n")
    if restart.lower().startswith("y"):
        reset_cards()
        run_flashcards()
    else:
        print("\nNo problem! See you next time! :)")

def run_flashcards():
    cards1 = cards.copy()
    mistakes = 0

    while True:
        for card in cards1:
            current_card = random.choice(cards1)
            if current_card["correct"]:
                continue

            else:
                print("\n" + (current_card["question"]) + ":")
                user_answer = input("\n")

            if user_answer == current_card["answer"]:
                print("\nCORRECT!\n\n")
                current_card["correct"] = True
                cards1.remove(current_card)
            else:
                print("\nIncorrect.")
                print("Correct answer: " + current_card["answer"])
                mistakes += 1

        if cards1 == []:
            print("\n\nYou have completed all flashcards with " +
                  str(mistakes) + " mistake(s)!")
            print("Great job!")
            restart_game()
            break

print("Welcome.")
begin = input("Want to pass CompTIA Core 1 with some flashcards?\n")

if begin.lower().startswith("y"):
    print("\nProvide the port number for the following well known ports\n")
    run_flashcards()
else:
    print("\nYou probably should practice these, but do you boo")

exit()
