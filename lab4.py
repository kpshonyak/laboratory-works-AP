class Conference:
    
    public_str = "публічне поле"
    
    def __init__(self,name ="", participants = 0, ticket_price = 0, place ="",public_int= 0 ):
        self.__name = name
        self.__participants = participants
        self.__ticket_price = ticket_price
        self.__place = place
        self.__public_int = public_int

        print("Конференція",self.__name,"створена")
    
    def __del__(self):
        print("Конференція",self.__name,"видалена")     


    def get_name(self):
        return self.__name
    
    def get_participants(self):
        return self.__participants

    def get_ticket_price(self):
        return self.__ticket_price

    def get_place(self):
        return self.__place
    
    # def get_public_int(self):
    #     return self._public_int 
    

    def set_name(self, name):
        self.__name = name

    def set_participants(self, participants):
        self.__participants = participants

    def set_ticket_price(self, ticket_price):
        self.__ticket_price = ticket_price

    def set_place(self, place):
        self.__place = place
    


    
    def __str__(self):
        return f"Конференція '{self.__name}' у місті {self.__place} з {self.__participants} учасниками. Ціна квитка: {self.__ticket_price} селф паблик :{self.__public_int}" 
       

    def __repr__(self):
       return f"Conference(name={self.__name}, participants={self.__participants}, ticket_price={self.__ticket_price}, city={self.__place})"
    
def find_participants(conferences):
    largest_conference = conferences[0]  
    for conference in conferences:
        if conference.get_participants() > largest_conference.get_participants():
            largest_conference = conference
    return largest_conference

def main():
    conf1 = Conference("Робота 2в команді",100,500,'Одеса')
    conf2 = Conference("Войті в Айті",100,100,'Львів')
    conf3 = Conference("Web Technology",10,400,'Харьків')

    conferences = [conf1, conf2, conf3]
    largest_conference = find_participants(conferences)
    print('Конференція з найбільшою кількістю учасників:', largest_conference.get_name())


    for conference in conferences:
        print(conference)




    print(repr(conf1))
    # print(repr(conf2))
    # print(repr(conf3))

main()