# Bubble Sort Algorithm

#1) Order elements in the same array without using extra memory
#2) Loop through the array to compare the left element to the right
#3) If the left element is greater then right swap the elements


unordered_list = [2, 7, 4, 1, 5, 3]

for i in range(0, len(unordered_list)):
    for j in range(0, len(unordered_list)-1):
        if(unordered_list[j] > unordered_list[j+1]):
            max_val = unordered_list[j]
            unordered_list[j] = unordered_list[j+1]
            unordered_list[j+1] = max_val
print(unordered_list)