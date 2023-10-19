
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result

# print(raise_to_power(3,4))

def risiko(attacker, defender):
    attacker.sort(reverse=True)
    defender.sort(reverse=True)

    num_comparisons = min(len(attacker), len(defender))
    
    armies_lost = 0
    
    for i in range(num_comparisons):
        if attacker[i] > defender[i]:
            armies_lost += 1
    
    return armies_lost

print(risiko([3, 6, 4], [2, 5, 3]))  
print(risiko([3, 6], [6, 4, 4]))     
print(risiko([3, 1], [1]))            