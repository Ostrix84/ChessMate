class chess:
    def __init__(self,tab):
        bite


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



class tour(piece):

    def deplacement(self,dx,dy):
        if(dx!=0 and dy!=0):
            print('Erreur la tour ne se déplace que sur les cotés.')
        else:
            piece.set_y(self,piece.get_y(self)+dy)
            piece.set_x(self,piece.get_x(self)+dx)


class fou(piece):

    def deplacement(self,dx,dy):
        if(abs(dx)!=abs(dy)):
            print('Erreur le fou se déplace uniquement en diagonale')
        else:
            piece.set_y(self,piece.get_y(self)+dy)
            piece.set_x(self,piece.get_x(self)+dx)



class cavalier(piece):

    def deplacement(self,dx,dy):
        if((abs(dx)==2*abs(dy))or(abs(dy)==2*abs(dx))):
            piece.set_y(self,piece.get_y(self)+dy)
            piece.set_x(self,piece.get_x(self)+dx)       
        else:
            print('Erreur le cavalier ne se déplace pas comme ca.')


class roi(piece):

    def deplacement(self,dx,dy):
        if((abs(dx)>1)or(abs(dy)>1)):
            print('Le roi est plus lent que ça.')
        else:
            piece.set_y(self,piece.get_y(self)+dy)
            piece.set_x(self,piece.get_x(self)+dx)


class dame(piece):

    def deplacement(self,dx,dy):
        if(((abs(dx)<2)and(dy==0))or((abs(dy)<2)and(dx==0))or(abs(dx)==abs(dy))):
            piece.set_y(self,piece.get_y(self)+dy)
            piece.set_x(self,piece.get_x(self)+dx)
        else:
            print("La dame n'a pas tout les pouvoirs non plus")


pion1=pion(0,0,1,0)
tour1=tour(0,0,0,0)
cavalier1=cavalier(0,1,0,0)
fou1=fou(0,2,0,0)
roi1=roi(0,4,0,0)
dame1=dame(0,3,0,0)





