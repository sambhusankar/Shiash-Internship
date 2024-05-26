#task no 6

class ListMethods:
    def __init__(self, l):
        self.l = l
    #sum of the list items
    def sum(self):
        sum = 0
        for item in self.l:
            sum += item
        print(sum)

    #multiplicaton of list items
    def multiplication(self):
        multi = 1
        for item in self.l:
            multi *= item
        print(multi)

    #largest number of the list
    def large_number(self):
        large = list[0]
        for item in self.l:
            if item > large:
                large = item
        print(large)

    #smallest number of the list
    def small_number(self):
        small = list[0]
        for item in self.l:
            if item < small:
                small = item
        print(small)

    #remove duplicate from the list
    def remove_duplicate(self):
        new_list = []
        for item in self.l:
            if item not in new_list:
                new_list.append(item)
        print(new_list)

    #checing the list is empty or not
    def check_empty(self):
        if len(self.l) == 0:
            print("Yes, the list is an empty list")
        else:
            print("it is not an empty list")
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
L = ListMethods(list)
L.sum()
L.multiplication()
L.large_number()
L.small_number()
L.remove_duplicate()
L.check_empty() #sir while checking this one method kindly comment out the another methods bacuse it will throgh error if list is empty