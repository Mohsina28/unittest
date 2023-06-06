class Person:
    name = []
    
    # def __init__(self, name=[]):
    #     if type(name) == list:
    #         self.name += name
    #     else:
    #         self.name.append(name)

    def set_name(self,name):
        self.name.append(name)
        return len(self.name) - 1
    
    def get_name(self,user_id):
        if user_id > len(self.name):
            return "no such user exists"
        else:
            return self.name[user_id-1]

if __name__ == "__main__":
    names=["Mohsina","Salma","Banu"]
    p1 = Person(names)
    print(p1.get_name(1))