class chess:
    def __init__(self,tab):


class piece:
    def __init__(self,couleur,x,y,nb_coup):
        self.__couleur=couleur          #0 pour noir, 1 pour blanc
        self.__x=x
        self.__y=y
        self.__nb_coup=nb_coup

    def get_x(self):
        return self.__x

    def set_x(self,x):
        self.__x=x

    def get_y(self):
        return self.__y

    def set_y(self,y):
        self.__y=y
    
    def get_nb_coup(self):
        return self.__nb_coup

    def set_nb_coup(self,nb_coup):
        self.__nb_coup=nb_coup

    def print_coordonne(self):
        print("x = ",self.get_x(), " y = ",self.get_y())

    def deplacement(self,dx,dy):
        if ((self.__x+dx>7)or(self.__y+dy>7)):
            print("Erreur: deplacement trop important")
            return False
        else:
            self.set_nb_coup(self.get_nb_coup()+1)
            return True
    
    

class pion(piece):
    
    def deplacement(self,dy):
        if((piece.get_nb_coup(self)==0 and dy>2)or(piece.get_nb_coup(self)>0 and dy>1)):
            print("Erreur : deplacement non autorise")
        else:
            if(super().deplacement(0,dy)):
                piece.set_y(self,piece.get_y(self)+dy)
                piece.set_nb_coup(self,piece.get_nb_coup(self)+1)
    


pion1=pion(1,0,1,0)
pion1.print_coordonne()
pion1.deplacement(2)
pion1.print_coordonne()

tab=((5,5),(6,6),(7,7))
print(tab[0][1])





