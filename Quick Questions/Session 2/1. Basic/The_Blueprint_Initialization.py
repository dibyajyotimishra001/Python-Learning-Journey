class Fighter:
    def __init__(self, name, fighting_style, stamina):
        self.name = name
        self.fighting_style = fighting_style
        self.stamina = stamina
        
user_1 = Fighter("Gemini", "Snake Harsira", int(90))
print(user_1.name, user_1.fighting_style, user_1.stamina)

user_2 = Fighter("Raj", "Cleve and Dismental(Jujustu)", int(100))
print(user_2.name, user_2.fighting_style, user_2.stamina)