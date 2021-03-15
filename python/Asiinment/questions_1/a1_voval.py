vol = {
  "a": 0,
  "e": 0,
  "i": 0,
  "o": 0,
  "u": 0,
  
}
# for k in vol:
#   print(k,vol[k])
a = input('Enter a String:- ')
print(len(a))
for i in a:
    if i=='a':
      vol[i]=vol[i]+1
    if i=='e':
      vol[i]=vol[i]+1
    if i=='i':
      vol[i]=vol[i]+1
    if i=='o':
      vol[i]=vol[i]+1
    if i=='u':
      vol[i]=vol[i]+1
print("Each vowel repeated as -")
for k in vol:
  print(k,vol[k])
    
    
