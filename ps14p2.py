# I am going to attempt this via watching the video and trying to understand


class Student:

  def __init__(self, first, last, code, credits):
    self.first = first
    self.last = last
    self.code = code
    self.credits = credits
    if code == "I":
      self.tutuion = credits * 250
    else:
      self.tutuion = credits * 500

  def fullname(self):
    return '{} {}'.format(self.first, self.last)


sdnt_1 = Student('Corey', 'Schafer', 'I', 5)
sdnt_2 = Student('Test', 'User', 'O', 5)

print(sdnt_2.fullname(), sdnt_2.code, sdnt_2.tutuion)
