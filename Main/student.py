class student:
    
    raise_mark=0.5
    
    def __init__( self , firstname , lastname , mark):
        self.firstname=firstname
        self.lastname=lastname
        self.mark=mark
        
    def maill(self) :
        return f"{self.firstname}.{self.lastname}@tu.io.com"
    
    def full_name(self):
        return f"{self.firstname} {self.lastname}"
    
    def inc_mark(self) : 
        self.mark=float(self.raise_mark + self.mark)
