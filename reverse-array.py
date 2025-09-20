# arr=[10,40,23,45]
# reverse_arr=arr[::-1]
# print("reverse array is:",reverse_arr)

# arr=[10,20,30,40]
# arr.reverse()
# print("reverse array is:",arr)

# using loop
arr=[10,20,30,40,50]
n=len(arr)
reverse_arr=[]

for i in range(n-1,-1,-1):
    reverse_arr.append(arr[i])
print("reverse array is:",reverse_arr) 
# print must be outside the loop