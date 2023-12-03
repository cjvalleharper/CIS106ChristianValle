# I am going to attempt this via watching the video and trying to understand


class Employee:
  def __init__(self,first,last,pay,rate):
      self.first = first
      self.last = last
      self.pay = pay
      self.rate = rate
      self.email = first + '.' + last + '@company.com'
      self.bonus = rate * pay

  def fullname(self):
    return '{} {}'.format(self.first, self.last, self.rate, self.bonus)

emp_1 = Employee('Corey', 'Schafer', 50000, 5)
emp_2 = Employee('Test', 'User', 60000, 4)

#print(emp_1)
#print(emp_2)


#emp_1.first = 'Corey'
#emp_1.last = 'Schafer' 
#emp_1.email = 'Corey.Schafer@company.com'
#emp_1.pay = 50000

#emp_2.first = 'Test'
#emp_2.last = 'User' 
#emp_2.email = 'Test.User@company.com'
#emp_2.pay = 60000

#print(emp_1.email)
#print(emp_2.email)

print(emp_1.fullname(),emp_1.rate, emp_1.bonus)


#print('{} {}'.format(emp_1.first, emp_1.last))






