def hi():
 return 'Hello git hub'


def by():
 return 'good by git hub '

def day():
  return 'days'

def hello():
 return 'hello'

class Bird:

   def __init__(self):
     print('Bird is ready')

   def whoisThis(self):
     print('Bird')

   def swim(self):
     print('Swim faster')

# child class
class Penguin(Bird):

   def __init__(self):
     # call super() function
     super().__init__()
     print('Penguin is ready')

   def whoisThis(self):
     print('Penguin')

   def run(self):
     print('Run faster')

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

