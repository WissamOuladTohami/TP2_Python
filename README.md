## Exercice 1 — Compte bancaire
- Créer la classe `CompteBancaire` avec `_titulaire` (protégé) et `__solde` (privé).  
- Méthodes `deposer(montant)` et `retirer(montant)` avec validation.  
- Propriété `solde` accessible en lecture seule.  
- Ajouter un historique des opérations `_operations`.  
- Extension : créer la classe dérivée `CompteEpargne` avec un taux d’intérêt et méthode `calculer_interet()`.

  ### L'éxécution du Programme :

  <img width="1523" height="376" alt="EX1" src="https://github.com/user-attachments/assets/86f84bd9-6faf-4ab5-8568-4e056cc2b8a2" />


---

## Exercice 2 — Client et Compte bancaire via composition
- Créer la classe `Client` avec un nom et une instance de `CompteBancaire`.  
- Méthode `afficher()` pour afficher le nom du client et le solde de son compte.  
- Illustrer la relation de composition « Client possède un CompteBancaire ».  
- Extension : afficher l’historique des opérations du compte via le client.

    ### L'éxécution du Programme :

  <img width="1551" height="405" alt="EX2" src="https://github.com/user-attachments/assets/3083d737-6385-4d46-aef3-3c1d42b2ad78" />
