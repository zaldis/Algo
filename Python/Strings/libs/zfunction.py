def get_z_function(text):
    """
        Z-function algorithm

        Complexity: O(n)

        text - input string
        n - length of input string
        l, r - boundaries of the current largest common prefix
               in positions 0 and i
        z - resulting z-function
    """
    n = len(text)
    z = [0] * n
    l = r = 0

    for i in range(1, n):
        if i < r:
            z[i] = min(z[i - l], r - i + 1)
        while i + z[i] < n and text[z[i]] == text[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z


if __name__ == '__main__':
    text = 'abababacababad'
    expected_zfunc = [0, 0, 5, 0, 3, 0, 1, 0, 5, 0, 3, 0, 1, 0]
    z_func = get_z_function(text)
    print('Input text: ', text)
    print('Expected z-function: ', expected_zfunc)
    print()
    print('Executed z-function: ', z_func)
