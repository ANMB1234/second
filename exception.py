from typing import List

class EvenOnly(List[int]):
    def append(self,value:int)->None:
        if not isinstance(value,int):
            raise TypeError("Only integers can be added")
        
        if value %2 !=0:
            raise ValueError("Only even numbers can be added")
        super().append(value)
        
e= EvenOnly()
e.append(2)

from typing import NoReturn

def never_returns()->NoReturn:
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"
    
    