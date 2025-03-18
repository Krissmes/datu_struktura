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
        if self.skaits == 0:
            print("Nav ko dzest!")
            return
        if self.skaits < indekss:
            print("nav tads elements")
            return
        esosais = self.sakums
        for x in range(indekss):
            esosais = esosais.next
        galva =  esosais.prev
        aste = esosais.next
        galva.next = aste
        aste.prev = galva
        self.skaits -= 1
        esosais = None

    def switch(self, indekss1, indekss2):
        if self.skaits < 1:
            print("Nav ko mainit")
            return
        if self.skaits < indekss1 or self.skaits < indekss2:
            print("nav tads elements")
            return
        pirmais = self.sakums
        for x in range(indekss1):
            pirmais = pirmais.next
        otrais = self.sakums
        for y in range(indekss2):
            otrais = otrais.next

        temp_n = pirmais.next
        temp_p = pirmais.prev
        pirmais.next = otrais.next
        pirmais.prev = otrais.prev
        otrais.next = temp_n
        otrais.prev = temp_p
        
        # temp_p_p = self.sakums
        # for z in range(indekss1 - 1):
        #     temp_p_p = temp_p_p.next

        # temp_p_n = self.sakums
        # for z in range(indekss1 + 1):
        #     temp_p_n = temp_p_n.next

        # temp_o_p = self.sakums
        # for z in range(indekss2 - 1):
        #     temp_o_p = temp_o_p.next

        # temp_o_n = self.sakums
        # for z in range(indekss2 + 1):
        #     temp_o_n = temp_o_n.next


        # temp_p_p.next = otrais
        # temp_p_n.prev = otrais
        # temp_o_p.next = pirmais
        # temp_o_n.prev = pirmais

        # temp = pirmais.prev.next
        # temp = pirmais.next.prev
        # pirmais.prev.next = otrais
        # pirmais.next.prev = otrais
        # otrais.prev.next = temp
        # otrais.next.prev = temp






saraksts = List()
saraksts.add("kakis")
saraksts.add("suns")
saraksts.add("maja")
saraksts.add("zogs")
saraksts.add("stabs")
saraksts.add("loks")

saraksts.read()
print("--------")
saraksts.switch(1,2)


saraksts.read()

# saraksts.sakums.read()
# print("=====")
# saraksts.sakums.read()



# saraksts.read()