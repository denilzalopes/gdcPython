class Option:
    def __init__(self, label, correct=False):
        self.label = label
        self.correct = correct

class Question:
    def __init__(self, label, options):
        self.label = label
        self.options = options

    def show(self):
        print(self.label)
        for option in self.options:
            print("- " + option.label)
        print("Entrez une réponse:")
        answer = input()
        if self.is_correct(answer):
            print("Bravo!")
            return True
        else:
            print("La réponse n'est pas correcte")
            return False

    def is_correct(self, answer):
        for option in self.options:
            if option.label == answer:
                return option.correct
        return False

# Initialisation du score
score = 0

# Liste des questions sous forme d'objets `Question`
questions = [
    Question("Quelle est la vitesse de pointe d'un thon?", [
        Option("20 km/h"), 
        Option("40 km/h"), 
        Option("80 km/h", True)  # Option correcte
    ]), 
    Question("Les poissons ont-ils tous des écailles?", [
        Option("Oui", False), 
        Option("Non", True)  # Option correcte
    ])
]

# Boucle sur chaque question
for question in questions:
    if question.show():
        score += 1

# Affichage du score final
print("Vous avez répondu correctement à " + str(score) + " questions sur " + str(len(questions)))
