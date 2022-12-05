### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python
#go through code and spot bug..put in comments not correct things

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:#if statement expect double equal instead of assignment
      return True
    else# : is missing
      return False
   

  dif highest_card(self, card1 card2):#def instead dif, and coma after card1
  #if else statement indentation
  if card1.value > card2.value:
    return card# card1 instead card
  else:
    return card2
  


def cards_total(self, cards):
  total #should initialize total (give it value)
  for card in cards:
    total += card.value
    return "You have a total of" + total #should use str() to convert total in string
  
```
