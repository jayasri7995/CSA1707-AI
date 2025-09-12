import itertools

def solve_send_more_money():
    # Letters involved in the puzzle
    letters = ('S','E','N','D','M','O','R','Y')
    # Leading letters cannot be 0
    leading = ('S','M')

    # All digits 0-9, choose permutations of 8 distinct digits
    for perm in itertools.permutations('0123456789', len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading zeros not allowed
        if any(mapping[ch] == '0' for ch in leading):
            continue

        # Convert words to numbers using mapping
        SEND  = int(mapping['S'] + mapping['E'] + mapping['N'] + mapping['D'])
        MORE  = int(mapping['M'] + mapping['O'] + mapping['R'] + mapping['E'])
        MONEY = int(mapping['M'] + mapping['O'] + mapping['N'] + mapping['E'] + mapping['Y'])

        if SEND + MORE == MONEY:
            return mapping, SEND, MORE, MONEY

    return None, None, None, None

if __name__ == "__main__":
    mapping, SEND, MORE, MONEY = solve_send_more_money()
    if mapping:
        print("Solution found:")
        for k in sorted(mapping):
            print(f"  {k} = {mapping[k]}")
        print()
        print(f"  SEND  = {SEND}")
        print(f"  MORE  = {MORE}")
        print(f"+ MONEY = {MONEY}")
        print(f"Check: {SEND} + {MORE} = {SEND + MORE}")
    else:
        print("No solution found.")
