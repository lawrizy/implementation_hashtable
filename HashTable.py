class HashTable():
    def __init__(self):
        self.taille = 100
        self.memoire = [None for i in range(self.taille)]
    def get_hash(self,chaine):
        return ord(chaine[0])
    def set_in_dico(self,cle,valeur):
        self.memoire[self.get_hash(cle)] = valeur
    def get_in_dico(self,cle):
        return self.memoire[self.get_hash(cle)]