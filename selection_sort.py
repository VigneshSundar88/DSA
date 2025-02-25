##Selection Sort Algorithm

#1) Order elements in ascending order in the same array without using extra memory
#2) Find the minimum element in the array from 0th index to the final (keep incrementing in the loop)
#3) Swap it to the 0th position
#4) Take the element that was in the 0th position and fill it in the position from where the minimum element was taken

unordered_list = [2, 7, 4, 1, 5, 3]

for i in range(0, len(unordered_list)): #n+1
    for j in range(i+1, len(unordered_list)): #n(n-1) = n^2-n 
        if(unordered_list[j] < unordered_list[i]): #n(n-1) = n^2-n
            min_ele = unordered_list[j] #1
            initial_ele = unordered_list[i] #1
            unordered_list[j] = initial_ele #1
            unordered_list[i] = min_ele #1
print(unordered_list) #1 

#total = 2n^2-n+6