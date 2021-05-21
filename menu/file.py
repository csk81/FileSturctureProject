import os
from menu import constant as c


class Menu:

    def __init__(self):
        self.path = 'menu/Menu.txt'     #Holds the path of Menu file
        self.file = open(self.path,'a+')
        self.Menu = self.menu_content() #Store the content of file into self.Menu Var
        self.items = self.get_item()


    
    def menu_content(self):
        with open(self.path,"r") as menu:
            data = menu.readlines()
        return data

    def get_item(self):
        items = [(idx,item.split(":")[0]) for idx,item in enumerate(self.Menu)]
        return items


######################################################################3
#    def get_idx(self,cat):
#        with open(self.path,'r') as f: data = f.readlines() 
#        f.close()
#        data = [cat.strip() for cat in data]
#        try:
#            idx = data.index(cat)
#        except ValueError:
#            idx = None
#        
#        return idx 
######################################################################3

    def create_file(self):
        files = os.listdir('menu')
        if "Menu.txt" in files :
            return None
        with open(self.path,'w') as n:
            pass
        n.close()
        return "Created a new file"
    



    def add_items(self,items,price,catogery):
        self.file.write(items+c.SEP+price+c.SEP+catogery+c.NEXT)
        print("Successfull Added")     

        



