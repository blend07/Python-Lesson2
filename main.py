#collections

lista = [1,2,3,4,4]

tuples =(1,2,3,4)

dictionaries = {
    "klasa8" : 10,
    "klasa10" : 20,
}

#sets

my_set = {1,2,3}

print(my_set)

your_set = set([1,2,3])

print(your_set)

set1 = {1,2,3,4}
set2 = {4,5,6}

#set1.update(set2)
#print(set1)

unionsets = set1.union(set2)

intersection = set1.intersection(set2)

print(unionsets)

print(intersection)

diferencesets = set1.difference(set2)

print(diferencesets)

darsejSet = {"Milan", "Chelsea", "Liverpool", "Barcelona"}

darsejSet.add("Real Betis")

print(darsejSet)

darsejSet.remove("Barcelona")

print(darsejSet)

print(len(darsejSet))

darsejSet.clear()

LisaList = [1,2,3,4,55,6,6,6]

unique_list = set(LisaList)

print(unique_list)
