# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  first = word.find(start)
  last = word.find(end)
  if first > -1 and last > -1:
    return word[first+1:last]
  else:
    return word
# Uncomment these function calls to test your function:
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"
