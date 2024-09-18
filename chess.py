from typing import Optional
from abc import abstractmethod


class Player:
    def __init__(self,name:str) -> None:
        """
        chess player객체를 생성합니다.
        """
        self.name=name
    
    
class ChessSet:
    def __init__(self,player1:Optional[Player],player2:Optional[Player]):
        """
        체스 게임의 한판은 set 합니다.
        """
        self.player1=player1
        self.plyaer2=player2
        



class Unit(ChessSet):
    @abstractmethod
    def move(self):
        pass
    """
    체스말 객체를 생성해줍니다.
    """

class Pawn(Unit):
    def __init__(self):
        """
        Pawn을 생성합니다.
        """
        self.move={'up':(0,1),'down':(0,-1),'right':(1,0),'left':(-1,0)}
        self.shape='Pawn'
class Bishop(Unit):
    def __init__(self):
        """
        create Bishop
        """
        self.move={}
        self.shape="Bishop"
        
class King(Unit):
    def __init__(self):
        """
        create King
        """
        self.move={}
        self.shape="King"
        
class Knight(Unit):
    def __init__(self):
        """
        create Knight
        """
        self.move={}
        self.shape="Knight"
        
    
class Queen(Unit):
    def __init__(self):
        """
        create Queen
        """
        self.move={}
        self.shape="Queen"

class Rook(Unit):
    def __init__(self):
        """
        create Rook
        """
        self.move={}
        self.shape="Rook"