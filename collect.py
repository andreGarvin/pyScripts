data = [ 'andre', 'dave', 'andre', 'jessica' ]

# the collection of how many counts it found in the list
collection = {}

# counter
j = 0

# goes through each item the list
while j < len( data ):
      
      # inserts them into the dictionary
      collection[data[j].lower()] = 0

      # goes through each item in the list
      for i in data:
          
	  # checks to see if the item is the same
	  # as the current item being checked how
	  # many times it appers in the list
          if i.lower() == data[j]:
             
	     # increments the value in the dictionary
             collection[i.lower()] += 1

      # increment to the next current item
      j+=1

# checks to see if the the item occurs 2 or more times
meta_data = []
for p in collection:
    if collection[p] >= 2:
       meta_data.append( p )

print meta_data
