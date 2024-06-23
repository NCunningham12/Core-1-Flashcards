print("Welcome.")
begin = input("Type 'OK' to begin")

cards = [
  {
    "question": "FTP",
    "answer": "20/21"
  },
  {
    "question": "Telnet",
    "answer": "25"
  },
  {
    "question": "SMTP",
    "answer": "25"
  },
  {
    "question": "POP3",
    "answer": "110"
  },
  {
    "question": "IMAP",
    "answer": "143"
  },
  {
    "question": "DNS",
    "answer": "53"
  },
  {
    "question": "HTTP",
    "answer": "80"
  },
  {
    "question": "HTTPS",
    "answer": "443"
  },
  {
    "question": "RDP",
    "answer": "3389"
  },
  {
    "question": "SNMP",
    "answer": "161"
  },
  {
    "question": "DHCP",
    "answer": "67/68"
  },
]

def run_flashcards():
  return


if begin.upper() == "OK":
  run_flashcards()
else:
  print("Maybe later then")
  exit()