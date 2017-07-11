class person:

 def __init__(self, nom, prenom):
  self.nom = nom
  self.prenom = prenom
        
 def set_prenom(self,prenom):
  self.prenom = prenom
      
 def set_nom(self,nom):
  self.nom = nom

 def what_s_your_name(self):
  return "My name is "+self.prenom+" "+self.nom


p = person("Renault","Dolyveen")
print(p.what_s_your_name())
