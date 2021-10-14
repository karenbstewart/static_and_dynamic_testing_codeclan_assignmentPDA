### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python
 
class CardGame:
# CardGame class not defined def __init__() missing

  def check_for_ace(self, card):
    /# should be a double equal for comparison, a single sets something to that value
    if card.value = 1:
      return True
      # else statement missing a colon after else
    else
      return False
   
# says dif not def in defining the method
#comma missing betweeen card1 and card2
  dif highest_card(self, card1 card2):
  #if method statement should be indented
  if card1.value > card2.value:
    #should be card1, not card. As card is undefind
    return card
  else:
    return card2
  


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
