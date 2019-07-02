class Materia:

    def __init__ (self, materiaName, materiaType):
        self.Name = materiaName
        self.Type = materiaType
        self.URL = ""
        self.Description = ""
        self.Location = ""
        self.Levels = []
        self.Locations = []
        self.Price = None
        self.CanPurchase = False
