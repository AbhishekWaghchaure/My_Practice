len = int(input("Enter the lenght of the list you want :"))
cut_list = []
for i in range (len):
    element = (input(f"Enter the {i}th element of the list :"))
    cut_list.append(element)
print(f" The custom list created by you is : ")

## Remove the nth Element from the list
word = "geeks"
n = 2

counter = 0

for i in range(0, len(cut_list)):
    if cut_list[i] == word:
        counter += 1
        if counter == n:
            del cut_list[i]
            
print(f"After the removal of nth element {cut_list}")
