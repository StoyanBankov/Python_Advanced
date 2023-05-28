def nums(a):

    sum_positives = 0
    sum_negatives = 0

    for el in a:
        if el >= 0:
            sum_positives += el
        else:
            sum_negatives += el

    print(sum_negatives)
    print(sum_positives)

    if abs(sum_negatives) > abs(sum_positives):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = list(map(int, input().split()))
nums(numbers)
