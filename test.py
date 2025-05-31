import csv

def return_map_as_list_of_lists(map_number) -> list[list]:
   map = []
   with open(f'Map{map_number}.csv', 'r') as map_read:
      csvread = csv.reader(map_read)
      for row in csvread: #row is a list with one item of type string
         map.append(list(row[0])) #list() takes the strings and makes them a list of str

   return map
 
def return_position(x,y) -> str:
    return map[y][x]
 #main

map = return_map_as_list_of_lists(1)

print(return_position(4,25))
print(type(return_position(4,25)))