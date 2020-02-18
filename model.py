class Etudiant:
    def __init__(self, numero, prenom, nom, niveau):
        self.numero = numero
        self.prenom = prenom
        self.nom = nom
        self.niveau = niveau

    def __repr__(self):
        return "Etudiant-> numero:%s prenom:%s nom:%s niveau:%s" % (self.numero, self.prenom, self.nom, self.niveau)

    def __contains__(self, item):
        return self.numero == item


def getSum(l):
    return l[0] + getSum(l[1:]) if l else 0


class Cours:
    def __init__(self, code, intitule, niveau):
        self.code = code
        self.intitule = intitule
        self.niveau = niveau

    def __repr__(self):
        return "Cours-> code:%s intitule:%s  niveau:%s" % (self.code, self.intitule, self.niveau)

    def __contains__(self, item):
        return self.code == item


class Note:
    def __init__(self, numeroEtudiant, codeCours, note):
        self.numeroEtudiant = numeroEtudiant
        self.codeCours = codeCours
        self.note = note

    def __repr__(self):
        return "Note-> numeroEtudiant:%s codeCours:%s  note:%s" % (self.numeroEtudiant, self.codeCours, self.note)


class BD:
    def __init__(self, etudiantList=[], coursList=[], notesList=[]):
        self.etudiantList = etudiantList
        self.coursList = coursList
        self.notesList = notesList

    def __repr__(self):
        return "Base de Donne-> \n etudiantList:%s \n coursList:%s  \n notesList:%s" % (
            self.etudiantList, self.coursList, self.notesList)

    def ajouterEtudiant(self, numero, prenom, nom, niveau):
        etudiant = Etudiant(numero, prenom, nom, niveau)
        self.etudiantList.append(etudiant)

    def supprimerEtudiant(self, etudiant):
        self.etudiantList.remove(etudiant)

    def ajouterEtudiant1(self, etudiant):
        self.etudiantList.append(etudiant)

    def modifierInfoEtudiant(self, numero, changePrenom=None, changeNom=None, changeNiveau=None):
        for student in self.etudiantList:
            if student.numero == numero:
                if changePrenom is not None:
                    student.prenom = changePrenom
                if changeNom is not None:
                    student.nom = changeNom
                if changeNiveau is not None:
                    student.niveau = changeNiveau

    # Cours
    def ajouterCours(self, code, intitule, niveau):
        cours = Cours(code, intitule, niveau)
        self.coursList.append(cours)

    def supprimerCours(self, cours):
        self.coursList.remove(cours)

    def ajouterCours1(self, cours):
        self.coursList.append(cours)

    def modifierInfoCours(self, code, changeIntitule=None, changeNiveau=None):
        for cours in self.coursList:
            if cours.code == code:
                if changeIntitule is not None:
                    cours.intitule = changeIntitule

                if changeNiveau is not None:
                    cours.niveau = changeNiveau

    # Note
    def ajouterNote(self, numeroEtudiant, codeCours, note):
        for etudiant in self.etudiantList:
            if etudiant.numero == numeroEtudiant:
                for cours in self.coursList:
                    if cours.code == codeCours:
                        note = Note(numeroEtudiant, codeCours, note)
                        self.notesList.append(note)

    def deleterNote(self, numeroEtudiant, codeCours):
        for note in self.notesList:
            if note.codeCours == codeCours and note.numeroEtudiant == numeroEtudiant:
                self.notesList.remove(note)

    def modifierNote(self, numeroEtudiant, codeCours, nouvelleNote):
        for note in self.notesList:
            if note.codeCours == codeCours and note.numeroEtudiant == numeroEtudiant:
                note.note = nouvelleNote

    def moyenneClasse(self, codeCours):
        nbEtudiant = len(self.etudiantList)
        sum = 0
        for cours in self.notesList:
            if cours.codeCours == codeCours:
                sum += cours.note
        moy = sum / nbEtudiant
        return moy

    def moyenneEtudiant(self, id):
        nbCours = 0
        sum = 0
        for cours in self.notesList:
            if cours.numeroEtudiant == id:
                sum += cours.note
                nbCours += 1
        moy = sum / nbCours
        return moy

    def noteClasse(self, id):
        l = []
        for cours in self.notesList:
            if cours.codeCours == id:
                l.append(cours)

        return l


v = BD()
v.etudiantList
[]
e = Etudiant(1, "elio", "maroun", "b")
v.ajouterEtudiant1(e)
v.ajouterEtudiant(2, "r", "m", "c")
v.etudiantList
c = Cours(11, "java", 1)
v.ajouterCours1(c)
v.ajouterNote(1, 11, 14)
v.ajouterNote(2, 11, 16)
# x = filter(lambda x: x == id, v.notesList)
# x(11)


# Consulter les notes d’une classe
list(filter(lambda x: x.codeCours == 11, v.notesList))
#  Consulter les notes d’un étudiant
list(filter(lambda y: y.numeroEtudiant == 1, v.notesList))
