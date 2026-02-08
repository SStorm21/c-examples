class nmap():
    def __init__(self, name, age, role,data):
        self.name = name
        self.age = age
        self.role = role
        self.data = data
        self.data = self.name +" "+ self.age +" "+ self.role


member1 = nmap("storm"," 18"," admin"," ")

print(member1.data)