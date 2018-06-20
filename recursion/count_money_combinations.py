def count_money_combinations(amount, denominations, denom_index=0, num_denom=0):
    global count_list

    if amount < 0:
        return 0

    if amount == 0:
        count_list.append(num_denom)
        return 1

    if denom_index > len(denominations) - 1 and amount > 0:
        return 0

    return count_money_combinations(amount - denominations[denom_index], denominations, denom_index, num_denom + 1) \
           + count_money_combinations(amount, denominations, denom_index + 1, num_denom)


if __name__ == '__main__':
    denominations = [1, 5, 10, 20, 50]
    amount = 79
    count_list = []
    _ = count_money_combinations(amount, denominations)
    print(count_list)
    assert min(count_list) == 7