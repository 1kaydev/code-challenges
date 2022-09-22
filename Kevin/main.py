arr = [1,1,3,2,1]

def main(arr):
  greater = 0
  for num in arr:
    if (num > greater):
      greater = num
  count_arr = [0] * 100
  for i in range (0, len(arr)):
    count_arr[arr[i]] += 1
  return count_arr
  
print(main(arr))