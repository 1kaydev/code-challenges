arr = [[112, 42, 83, 119],[56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
print(len(arr))
def main(arr):
  total = 0
  for i in range (0, int(len(arr)/2)):
    for j in range(0, int(len(arr)/2)):
      total += max(arr[i][j],arr[i][len(arr)-j-1],arr[len(arr)-i-1][j],arr[len(arr)-i-1][len(arr)-j-1])
  return total
print(main(arr))