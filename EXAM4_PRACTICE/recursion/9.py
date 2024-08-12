def first_k(n, k):
    if n == 1:
        return 0

    #The recursive call returns how many
    #even numbers it has already included in the
    #sum
    x = first_k(n - 1, k)

    #If x == k it means I have added first
    #k even numbers
    if x == k:
        return x
    else: #If x != k (it means it is x < k as
        # k is a positive number, then print
        # more even numbers)
        if n % 2 == 0:
            print(n)
            return x + 1
        else:
            return x

first_k(10, 10)
print("-------")
first_k(10, 3)
