# -*- coding: utf-8 -*-
"""Quiz_Game.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KDSRzKjjm7DgMQoNDiSUMwa5Y7Tau6M2
"""

print("Welcome to my Valorant Quiz!!!")

playing = input("Do you want to start the quiz? ")

if playing.lower() != 'yes':
  quit()

print("Let's start with the first question:")
score=0

answer = input("\nQ1) What was Valorant's old name?\nA) Project A\nB) Counter Attack\nC) Leage of Agents\nD) VALO-07\n")

if answer.lower() == 'a':
  print("Correct!!")
  score+=1
else:
  print("Wrong, the correct answer is Project A...")

answer = input("\nQ2) This voiceline belongs to which agent?\n'I know exactly where they are'\nA) Brimstone\nB) Viper\nC) Cypher\nD) Neon\n")

if answer.lower() == 'c':
  print("Correct!!")
  score+=1
else:
  print("Wrong, the correct answer is Cypher...")

answer = input("\nQ3) Which of the following guns can kill an opponent with 1 headshot no matter the distance?\nA) Bulldog\nB) Vandal\nC) Odin\nD) Phantom\n")

if answer.lower() == 'b':
  print("Correct!!")
  score+=1
else:
  print("Wrong, the correct answer is Vandal...")

answer = input("\nQ4) This voiceline belongs to which agent?\n'The hunt begins'\nA) Reyna\nB) Viper\nC) Pheonix\nD) Jett\n")

if answer.lower() == 'a':
  print("Correct!!")
  score+=1
else:
  print("Wrong, the correct answer is Reyna...")


answer = input("\nQ5) How many knives are there in Jett's ultimate ability?\nA) 4\nB) 5\nC) 6\nD) 3\n")

if answer.lower() == 'b':
  print("Correct!!")
  score+=1
else:
  print("Wrong, the correct answer is 5...")

answer = input("\nQ6) This voiceline belongs to which agent?\n'Fire in the hole'\nA) Astra\nB) Fade\nC) Raze\nD) Yoru\n")

if answer.lower() == 'c':
  print("Correct!!")
  score+=1
else:
  print("Wrong, the correct answer is Raze...")

answer = input("\nQ7) Which of the following weapons give the same damage no matter the distance?\nA) Bulldog\nB) Phantom\nC) Spectre\nD) Ghost\n")

if answer.lower() == 'a':
  print("Correct!!")
  score+=1
else:
  print("Wrong, the correct answer is Bulldog...")

answer = input("\nQ8) Which agent is from India?\nA) Neon\nB) Harbor\nC) Viper\nD) Astra\n")

if answer.lower() == 'b':
  print("Correct!!")
  score+=1
else:
  print("Galat, Harbor hai sahi jawab...")

answer = input("\nQ9) Which of the following agents can heal themselves?\nA) Viper\nB) Brimstone\nC) Skye\nD) Reyna\n")

if answer.lower() == 'd':
  print("Correct!!")
  score+=1
else:
  print("Wrong, the correct answer is Reyna...")


answer = input("\nQ10) Which agent is the oldest in valorant?\nA) Sage\nB) Brimstone\nC) Viper\nD) Skye\n")

if answer.lower() == 'b':
  print("Correct!!")
  score+=1
else:
  print("Wrong, the correct answer is Brimstone...")

percent = (score/10) * 100

if percent >= 40 and percent <= 70:
  print("\nCongratulations you passed the quiz, but you can still improve I believe...")
elif percent < 40:
  print("\nI'm sorry to inform you that you did not pass the quiz...")
else:
  print("\nCongratulationss!!!!\nI have to say you do know a lot about the game...")

