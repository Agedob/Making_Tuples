my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
def tup(arr):
    for key,value in arr.iteritems():
        v = (key,value)
        print v
tup(my_dict)