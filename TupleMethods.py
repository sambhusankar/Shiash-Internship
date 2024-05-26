#task no 6 tuple
#creating a tuple with different datatypes
tuple1 = (1, 1.1, "sankar", True, None)

#creating a tuple with number a print a item
num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(num_tuple[2])

#unpacking tuple with different variables
person = ("sankar", 21, "software engineer")
name, age, proffesion = person
print("my name is", name, "i am ", age, "year old and i am a ", proffesion)

#adding an item in tuple
#tuples are immutable we can't direct change it to achive this we need to change its data type
courses = ("web developer", "data scientist", "devops", "AIML", "cyber security")
new_course = "IoT engineering"
temp_list = list(courses)
temp_list.append(new_course)
courses = tuple(temp_list)
print(courses)

#getting the 5th elements from last and fast from tuple
friends = ("narendra modi", "mukesh ambani", "bill gates", "elon musk", "steave jobs", "sundar pichai")
print("5th element form fast is ", friends[5])
print("5th element from last is ", friends[-5])

#find repeated element from tuple
daily_spends = (50, 100, 0, 50, 50, 70, 100, 100, 0)
repeated_elements = []
for i in range(len(daily_spends)):
    for j in range(i+1,len(daily_spends)):
        
        if daily_spends[i] == daily_spends[j] and daily_spends[i] not in repeated_elements:
            repeated_elements.append(daily_spends[i])
            

print(repeated_elements)


