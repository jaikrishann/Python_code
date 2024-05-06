class Father:
    son_name = 'mohan'
    son_age = "15"
    _son_id = 'mohan@gmail.com'
    __son_pass = "444"
     

    def display(self):
        print(self.son_name,"public variable")
        print(self._son_id,"protected variable")
        print(self.__son_pass,"private variable")

class Son(Father):
    pass
    
obj = Son()
print(obj._son_pass)





# obj = Father()        
# print(obj.__dict__)


