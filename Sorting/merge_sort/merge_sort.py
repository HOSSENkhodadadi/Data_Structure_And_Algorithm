class Sorting():
    def merge_sort(self,A, p, r):
        if p < r:
            q = ((p + r)//2)
            self.merge_sort(A, p, q)
            self.merge_sort(A, q + 1, r)
            self.merge(A, p, q, r)

    def merge(self, A, p, q , r):
        L = []
        R = []
        for i in range(p, q + 1):
            L.append(A[i])
        for j in range(q+1, r+1):
            R.append(A[j])
        L.append(float('inf'))
        R.append(float("inf"))

        # you could write like this
        # L = A[p: q+1] + [float("inf")]
        # R = A[q+1: r+1] + [float("inf")]

        i , j = 0, 0
        for k in range(p, r + 1):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1 
            else:
                A[k] = R[j]
                j += 1


# arr = [x for x in range(10)]
# arr = arr[::-1]
# print('arr: ', arr, "/n")
# sort1 = Sorting()
# sort1.merge_sort(arr, 0, len(arr)-1)
# print("sorted_arr: ", arr)