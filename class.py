class pound:
    
    def __init__(self, rare=False):
        
        self.rare = rare
        if self.rare:
            self.value = 1.25
        else: 
            self.value = 1.00
    
    self.colour = "gold"
    self.num_edges = 1
    self.diameter = 22.5 #mm
    self.thickness = 3.15 #mm
    self.head = True
    
    