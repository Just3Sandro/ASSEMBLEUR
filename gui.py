import tkinter as tk  # Importer Tkinter pour l'interface graphique
from pile import Pile  # Importer la classe Pile pour la simulation

class PileVisualizer:
    def __init__(self, root, pile):
        """
        Initialise l'interface graphique pour la visualisation de la pile.
        :param root: La fenêtre principale (Tkinter root).
        :param pile: Une instance de la classe Pile.
        """
        self.root = root
        self.pile = pile

        # Définir le titre et la taille de la fenêtre
        self.root.title("Visualisation de la Pile")
        self.root.geometry("300x500")

        # Zone d'affichage graphique de la pile
        self.canvas = tk.Canvas(root, width=300, height=400, bg="white")
        self.canvas.pack(pady=10)

        # Zone de saisie pour ajouter une valeur dans la pile
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        self.value_entry = tk.Entry(self.input_frame, width=10)
        self.value_entry.pack(side=tk.LEFT, padx=5)

        self.push_button = tk.Button(
            self.input_frame, text="Push", command=self.push_value
        )
        self.push_button.pack(side=tk.LEFT, padx=5)

        # Bouton pour retirer un élément
        self.pop_button = tk.Button(root, text="Pop", command=self.pop_value)
        self.pop_button.pack(pady=5)

        # Bouton pour réinitialiser la pile
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_stack)
        self.reset_button.pack(pady=5)

    def push_value(self):
        """Récupère une valeur entrée par l'utilisateur et l'ajoute à la pile."""
        valeur = self.value_entry.get()
        if valeur:
            self.pile.push(valeur)
            self.value_entry.delete(0, tk.END)  # Efface la zone de saisie
            self.refresh_stack()

    def pop_value(self):
        """Retire l'élément au sommet de la pile."""
        self.pile.pop()
        self.refresh_stack()

    def reset_stack(self):
        """Réinitialise complètement la pile."""
        self.pile.stack = []  # Vider la pile
        self.refresh_stack()

    def refresh_stack(self):
        """Met à jour l'affichage de la pile."""
        self.canvas.delete("all")  # Efface l'affichage précédent
        stack = self.pile.get_stack()
        for i, val in enumerate(stack):
            # Dessiner les rectangles représentant chaque élément de la pile
            x1, y1 = 50, 400 - (i + 1) * 40
            x2, y2 = 250, 400 - i * 40
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            self.canvas.create_text(150, (y1 + y2) // 2, text=val, fill="white")
