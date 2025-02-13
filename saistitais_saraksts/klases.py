class Node:
    def __init__(self,saturs, pirms=None, pec=None):
        self.info = saturs
        self.next = pec
        self.prev = pirms

    def read(self):
        print(self.info)


class List:
    def __init__(self):
        self.sakums = None
        self.skaits = 0
        return

    def add(self, jaunais, indekss =-1):
        if indekss == -1 or indekss >= self.skaits:
            if self.sakums == None:                #tas ir lai pieliktu gala
                self.sakums = Node(jaunais)
            else:
                pedejais = self.sakums
                while pedejais.next:
                    pedejais = pedejais.next
                pedejais.next = Node(jaunais, pirms=pedejais)         #lidz sejienei
        else:
            if indekss == 0:
                elements = Node(jaunais, pec = self.sakums)
                self.sakums.prev = elements
                self.sakums = self.sakums.prev
            else:
                aste = self.sakums
                for i in range(indekss):
                    aste = aste.next
                galva = aste.prev
                elements = Node(jaunais, galva, aste)
                galva.next = elements
                aste.prev = elements
        self.skaits += 1
        return

    def read(self):
        if self.sakums == None:
            print("Saraksts ir tukšs")
        esosais = self.sakums
        
        while esosais:
            esosais.read()
            esosais = esosais.next
        return

    def pop(self):
        if self.skaits == 0:
            print("Nav ko dzest!")
            return
        if self.skaits == 1:
            self.sakums = None
            self.skaits = 0 
            return
        pirmspedejais = self.sakums
        while pirmspedejais.next.next:
            pirmspedejais = pirmspedejais.next

        pirmspedejais.next = None
        self.skaits -= 1
        return
    def pop_cool(self, indekss):
        print("majasdarbs")

    def switch(self, indekss1, indekss2):
        elements1 = self.sakums
        for x in range(indekss1):
            elements1 = elements1.next
            print(elements1)
        
        elements2 = self.sakums
        for x in range(indekss2):
            elements2 = elements2.next
            print(elements2)

        elements1.info, elements2.info = elements2.info, elements1.info
        






saraksts = List()
saraksts.add("kakis")
saraksts.add("suns")
saraksts.add("maja")
saraksts.add("zogs")
saraksts.add("stabs")


saraksts.read()

saraksts.sakums.read()
print("=====")
saraksts.sakums.read()

saraksts.switch(1,4)

saraksts.read()