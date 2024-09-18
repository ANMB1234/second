


class OutOfStock(Exception):
    pass
class InvalidItemType(Exception):
    pass
class ItemType:
    def __init__(self,name:str)->None:
        self.name=name
        self.on_hand=0
        
        
class Inventory:
    def __init__(self,stock: list[ItemType]):
        pass
    
    def lock(self, item_type: ItemType)->None:
        """context enter 
        작업하는동안 아무도 재고를 조작할 수 없도록 품목을 잠근다.
        """
        pass
    def unlock(self,item_type:ItemType)->None:
        """context exit
        stock type is unlocked
        """
    def purchase(self,item_type:ItemType)->int:
        """품목이 잠겨있지 않으면 문제가 있으므로 ValueError를 발생한다."""
        if item_type.name=="Widget":
            raise OutOfStock(item_type)
        elif item_type.name=="Gadget":
            return 42
        else:
            raise InvalidItemType(item_type)
        
widget=ItemType("Widget")
gadget=ItemType("Gadget")
inv=Inventory([widget,gadget])

item_to_buy = widget


try:
    inv.lock(item_to_buy)
    num_left=inv.purchase(item_to_buy)
except InvalidItemType:
    print(f"Sorry, we don't sell {item_to_buy.name}")
except OutOfStock:
    print("Sorry, that item is out of stock.")
else:
    print(f"Purchase complete. There are {num_left} {item_to_buy.name}s left")
finally:
    inv.unlock(item_to_buy)

