print("Quelle est la vitesse de pointe d'un thon?")
print("-20 km/h")
print("-40 km/h")
print("-80 km/h")
print("Entrez une réponse:")
answer = input()
print("Vous avez répondu" + answer)
if answer == "80 km/h" :
  score = 1
  print("Bravo!")
else:
  score = 0
  print("Laréponse n'est pas correct")

  print("Vous avez répondu correctement à " + str(score) + "question sur 1")
