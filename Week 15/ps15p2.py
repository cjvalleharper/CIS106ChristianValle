# I am going to attempt this via watching the video and trying to understand


#main
class Car:

  def __init__(self, make, model, sticker):
    self.make = make
    self.model = model
    self.sticker = sticker
    self.discount = sticker * .9

  

# sub class
class Sport(Car):
  
 def __init__(self, make, model, sticker):
  super().__init__(make, model,sticker)
  self.pricewithoptions = 0
  
  for y in range(1):
    SportsWheelsChoice = input("Would you like to add wheels? (Y/N): ")
    if SportsWheelsChoice == "Y": self.pricewithoptions += 1000
  

    SportsEngineChoice = input("Would you like to add Sports Engine? (Y/N): ")
    if SportsEngineChoice == "Y": self.pricewithoptions += 3000
  

    SportsIntChoice = input("Would you like to add wheels? (Y/N): ")
    if SportsIntChoice == "Y": self.pricewithoptions += 2000
  



 def info(self):
    return '{} {} - Sticker price: {}, Discounted price: {}, Price with options: {}'.format(self.make, self.model, self.sticker, self.discount, self.pricewithoptions)


car = Car('Dodge', 'Van', 100)
sport = Sport('Fancy', 'Vroom', 1)

#print(sport.pricewithoptions)
print(sport.info())
