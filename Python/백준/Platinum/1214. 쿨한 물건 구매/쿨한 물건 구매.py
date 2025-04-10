def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def least_common_multiple(a, b):
    return a // greatest_common_divisor(a, b) * b

required_total, first_package_size, second_package_size = map(int, input().split())

if first_package_size < second_package_size:
    first_package_size, second_package_size = second_package_size, first_package_size

minimum_total_amount = float('inf')

for first_package_count in range(0, min(required_total, least_common_multiple(first_package_size, second_package_size)) + first_package_size, first_package_size):
    remaining_amount = max(required_total - first_package_count, 0)
    second_package_total = (remaining_amount // second_package_size) * second_package_size
    if second_package_total < remaining_amount:
        second_package_total += second_package_size
    current_total_amount = first_package_count + second_package_total
    if minimum_total_amount > current_total_amount:
        minimum_total_amount = current_total_amount

print(minimum_total_amount)