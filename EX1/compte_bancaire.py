class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire
        self.__solde = solde_initial
        self._operations = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self._operations.append(f"Dépôt : {montant} €")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._operations.append(f"Retrait : {montant} €")
        else:
            print("Fonds insuffisants ou montant invalide.")

    @property
    def solde(self):
        return self.__solde

    @property
    def operations(self):
        return self._operations.copy()

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"


class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde_initial=0, taux_annuel=1.5):
        super().__init__(titulaire, solde_initial)
        self.taux_annuel = taux_annuel

    def calculer_interet(self):
        interet = self.solde * self.taux_annuel / 100
        self.deposer(interet)
        self._operations.append(f"Intérêt : {interet:.2f} €")
        return interet


if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)
    compte.deposer(200)
    compte.retirer(150)
    print(compte)
    print("Solde accessible (lecture) :", compte.solde)
    print("Historique des opérations :", compte.operations)

    try:
        compte.solde = 500
    except AttributeError as e:
        print("Erreur capturée :", e)

    epargne = CompteEpargne("Sara", 2000, 2.0)
    print(epargne)
    interet = epargne.calculer_interet()
    print(f"Intérêt calculé : {interet:.2f} €")
    print("Solde après intérêt :", epargne.solde)
    print("Historique opérations :", epargne.operations)
