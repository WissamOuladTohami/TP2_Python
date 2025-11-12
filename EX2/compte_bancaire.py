class CompteBancaire:
    def __init__(self, solde_initial=0.0):
        self.__solde = solde_initial
        self._operations = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self._operations.append(f"Dépôt : {montant} €")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._operations.append(f"Retrait : {montant} €")

    def get_solde(self):
        return self.__solde

    def get_operations(self):
        return self._operations.copy()


class Client:
    def __init__(self, nom):
        self.nom = nom
        self.compte = CompteBancaire()

    def afficher(self):
        print(f"Client : {self.nom}, Solde : {self.compte.get_solde()}€")
        print("Historique des opérations :", self.compte.get_operations())


if __name__ == "__main__":
    cli = Client("Yassir")
    cli.compte.deposer(300)
    cli.compte.retirer(50)
    cli.afficher()
