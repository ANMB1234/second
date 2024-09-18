from typing import Protocol,Any
class ContactList(list["Contact"]):
    def search(self,name:str)->list["Contact"]:
        matching_contact : list["Contact"]=[]
        for contact in self:
            if name in contact.name:
                matching_contact.append(contact)
        return matching_contact


class Contact:
    all_contact=ContactList()
    
    def __init__(self,/, name:str="",email:str="", **kwargs:Any)->None:
        super().__init__(**kwargs)
        self.name=name
        self.email=email
        Contact.all_contact.append(self)
        
    def __repr__(self)->str:
        return (f"{self.__class__.__name__}("
                f"{self.name!r},{self.email!r})"
        )
class AddressHolder:
    def __init__(self,/,
                 street:str="",city:str="",state:str="",code:str="",**kwargs:Any)->None:
        super().__init__(**kwargs)#type:ignore[call-arg]
        self.street = street
        self.city=city
        self.state=state
        self.code=code
                
        
class Friend(Contact,AddressHolder):
    def __init__(self,/,phone:str="",**kwargs:Any)->None:
        super().__init__(**kwargs)
        self.phone=phone
 
class Relation(Friend):
    def __init__(self,name:str,email:str,phone:str,relationship:str)->None:
        super().__init__(name,email,phone)
        self.relationship=relationship    
        print(f.name)
class Emailable(Protocol):
    email:str
class MailSender(Emailable):
    def send_mail(self,message:str)->None:
        print(f"Sending mail to {self.email=}")
        """
        add email-related login here
        """
        
class EmailableContact(Contact,MailSender):
    pass

f=Con(name="kim")
print(f)