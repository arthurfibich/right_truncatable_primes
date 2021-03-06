import math

found_primes = [[2, 3, 5, 7], 10]


def is_prime(candidate):
    for prime in found_primes[0]:
        if candidate % prime == 0:
            return False
        elif prime > math.sqrt(candidate):
            return True
    return True


def prime_list_finder(upper_bound: int):  # asymptotic runtime is in Theta((n^1.5)/ln(n)), where n is the upper bound because asymptotically, the primes occur at a rate of n/ln(n)
    if upper_bound < found_primes[1]:
        return [[x for x in found_primes[0] if x <= upper_bound], upper_bound]
    for candidate in range(found_primes[1], upper_bound + 1):

        if is_prime(candidate):
            found_primes[0].append(candidate)
        found_primes[1] = candidate
    return found_primes


def find_all_right_truncatable_primes(base: int):
    first_digits = prime_list_finder(base-1)[0]
    base_dividors = [x for x in first_digits if base % x == 0]
    appendables = [x for x in range(base) if all(x % div != 0 for div in base_dividors)]
    # print(f'The digits that can be appended in each step: {appendables}')
    current_list = [str(x) for x in first_digits]
    while current_list:
        yield current_list
        new_list = [str(current)+str(appendable) for current in current_list for appendable in appendables]
        prime_list_finder(int(math.sqrt(int(max(new_list, key=(lambda x: int(x)))))+10))    # 10 is a safety margin, I'd rather have computed some primes, that I don't need instead of missing some below
        new_list = [x for x in new_list if is_prime(int(x, base=base))]
        current_list = new_list



if __name__ == "__main__":
    result = []
    base = int(input("In which base do you want to calculate the right truncatable primes? Base: "))
    for i in find_all_right_truncatable_primes(base=base):
        result.append(i)
    base_list = [int(x) for pl in result for x in pl]
    print(f'The resulting numbers in base {base} (Maximum is: {max(base_list)}): {base_list}')
    base_10_list = [int(x, base=base) for pl in result for x in pl]
    print(f'The resulting numbers in base 10 (Maximum is: {max(base_10_list)}): {base_10_list}')
