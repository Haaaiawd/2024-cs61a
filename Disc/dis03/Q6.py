# write any code you want
from karel.stanfordkarel import *

def main():
   # your code here...
   if front_is_clear():
      move()
      if main() % 2 == 0:
         move()
   elif front_is_blocked():
      turn_left()
      move()
      turn_left()
      return 0
##错的(┬＿┬)，放弃了，希望能给点思路吧，%是禁止的