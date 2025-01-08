from tkinter import Tk
from gui import PileVisualizer
from pile import Pile

if __name__ == "__main__":
    root = Tk()  # Crée la fenêtre principale Tkinter
    pile = Pile(taille_max=10)  # Initialise une pile avec une taille maximale
    app = PileVisualizer(root, pile)  # Crée l'interface avec la pile associée
    root.mainloop()  # Lance la boucle principale de l'application
