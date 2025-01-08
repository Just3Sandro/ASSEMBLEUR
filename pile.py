class Pile:
    def __init__(self, taille_max=10):
        self.taille_max = taille_max
        self.stack = []

    def push(self, valeur):
        if len(self.stack) < self.taille_max:
            self.stack.append(valeur)
        else:
            print("Pile pleine !")

    def pop(self):
        if self.stack:
            return self.stack.pop()
        print("Pile vide !")
        return None

    def peek(self):
        return self.stack[-1] if self.stack else None

    def get_stack(self):
        return self.stack

