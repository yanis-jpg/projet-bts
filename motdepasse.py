mdp = input("Entre ton mot de passe : ")

if len(mdp) < 8:
    print("Mot de passe faible 😕")
elif any(c.isdigit() for c in mdp) and any(c.isupper() for c in mdp):
    print("Mot de passe fort 💪")
else:
    print("Mot de passe moyen 🙂")
