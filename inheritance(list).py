from pprint import pprint

class ContactList(list["Contact"]):
    def search(self,name:str)-> list["Contact"]:
        matching_contacts:list["Contact"]=[]
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contact=ContactList()
    def __init__(self, name:str,email:str)->None:
        self.name=name
        self.email=email
        Contact.all_contact.append(self)
        
    def __repr__(self)->str:
        return(
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}"
            f")"
        )
        

class Supplier(Contact):
    def order(self,order:"Order")->None:
        print(f"""
              If this were a real system we would send 
              f'{order}'order to '{self.name}'
              """)
a=Contact('김도훈1','solfwolf@nate.com')
b=Contact("1","asdf")
c=Contact("김도훈2","asdf")
result=[z.name for z in Contact.all_contact.search("훈도김")]

print(result)