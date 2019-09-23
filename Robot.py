class Robot:
    def __init__(self, language, continent, greeting):
        self.language = language
        self.continent = continent
        self.greeting = greeting

    def print_self(self):
        print("In Uzbek " + self.greeting)

    def print_self2(self):
        print("In English " + self.greeting)

    def print_self3(self):
        print("In Africa " + self.greeting)

    def print_self4(self):
        print("In France " + self.greeting)

gr_uz = Robot("Uzbek", "Tashkent", "Assalam Alaykum")
gr_en = Robot("English", "London", "Hello")
gr_af = Robot("African", "Niger", "Hola")
gr_fr = Robot("France", "Parij", "Bonjour")


gr_uz.print_self()
gr_en.print_self2()
gr_af.print_self3()
gr_fr.print_self4()














