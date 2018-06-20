def count_money_combinations(amount, denominations):



if __name__ == '__main__':
    denominations = [1, 5, 10, 20, 50]
    amount = 79
    count_list = []
    _ = count_money_combinations(amount, denominations)
    print(count_list)
    assert min(count_list) == 7