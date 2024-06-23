import random

print("Welcome.")
begin = input("Want to pass CompTIA Core 1?\n")

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

def run_flashcards():

  while True:
    for card in cards:
      if card["correct"] == True:
        continue
      else:
        print("\n\n" + card["question"] + ":")
        user_answer = input("\n")

        if user_answer == card["answer"]: 
          print("\nCORRECT!\n\n")
          card["correct"] = True
        else:
          print("\nIncorrect.\n\n")
          print("Correct answer: " + card["answer"])

    end = input("Would you like to end the session?\n")
    if end.lower().startswith("y"):
      print("Sounds good. Have a good day!")
      break
    else:
      print("Let's try again!")
      continue

if begin.lower().startswith("y"):
  print("\nName the following well known ports\n")
  run_flashcards()
else:
  print("Maybe later then")
  exit()