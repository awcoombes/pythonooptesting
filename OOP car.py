# class Elevator:
#     def __init__(self, starting_floor, manufacturer):
#         self.make = manufacturer
#         self.floor = starting_floor

# # to create the object

# lift = Elevator(1, "Otis")
# print(lift.make)
# print(lift.floor)

# class Square:
#     def __init__(self):
#       self.__height = 2
#       self.__width = 2
#     def set_side(self, new_side):
#       self.__height = new_side
#       self.__width = new_side
#     def get_height(self):
#       return self.__height
#     def set_height(self, h):
#         if h >= 0:
#           self.__height = h
#         else:
#           raise Exception("value needs to be 0 or larger")

class Square:
  def __init__(self, w, h):
    self.height = h
    self.__width = w
  
  def set_side(self, new_side):
    self.__height = new_side
    self.__width = new_side

  @property
  def height(self):
    return self.__height

  @height.setter
  def height(self, new_value):
    if new_value >= 0:
      self.__height = new_value
    else:
      raise Exception("Value must be larger than 0")
    
def change():
  a = input("What is the height of your square: ")
  try:
    a = int(a)
    square.height = a
    return True
  except ValueError:
    print("Value must be an integer")
    return False
  except Exception as e:
    print(e)
    return False

square = Square(4, 4)
while True:
  a = change()
  if a == True:
    break
print(square.height)

#pushed to git
