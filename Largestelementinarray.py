# Find largest element in an array (list in Python)
arr=[10,20,33,16,87,75]
# Assume first element is largest
largest=arr[0]
for num in arr:
    if num>largest:
        largest=num
print("largest elememt is:",largest)
