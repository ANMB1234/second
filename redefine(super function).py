class ContactList(list["Contact"]):
    def search(self,name:str)->list["Contact"]:
        matching_contact : list["Contact"]=[]
        for contact in self:
            if name in contact.name:
                matching_contact.append(contact)
        return matching_contact


class Contact:
    all_contact=ContactList()
    
    def __init__(self, name:str,email:str)->None:
        self.name=name
        self.email=email
        Contact.all_contact.append(self)
        
    def __repr__(self)->str:
        return (f"{self.__class__.__name__}("
                f"{self.name!r},{self.email!r})"
        )
        
        
class Friend(Contact):
    def __init__(self,name:str,email:str,phone:str)->None:
        super().__init__(name,email)
        self.phone=phone
 
class Relation(Friend):
    def __init__(self,name:str,email:str,phone:str,relationship:str)->None:
        super().__init__(name,email,phone)
        self.relationship=relationship       
        
f=Relation("kython","kython@private.com","010-2984-8885","Friends")
print(f.name)