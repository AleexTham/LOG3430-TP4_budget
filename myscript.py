import os

# Définir les hachages de commit pour le bisect (mauvais et bon)
badhash = "c1a4be04b972b6c17db242fc37752ad517c29402"  # Dernier commit où les tests échouent
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"  # Dernier commit où tout fonctionne

# Lancer le bisect avec les hachages donnés
os.system(f"git bisect start {badhash} {goodhash}")

# Exécuter git bisect en utilisant la commande pour tester les commits
os.system("git bisect run python manage.py test")

# Réinitialiser le bisect pour éviter tout impact ultérieur
os.system("git bisect reset")
