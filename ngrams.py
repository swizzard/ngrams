def ngrams(n, xs, pad_right=None, pad_left=None):
    """
    Generate ngrams
    :param n: size of ngrams
    :type n: int
    :param xs: sequence to turn into ngrams
    :type xs: list
    :param pad_right: token to use when right-padding ngrams at end of sequence
    :param pad_left: token to use when left-padding ngrams at start of sequence
    :NB: if pad_left is None (the default), no left-padding will occur
    >>> xs = range(0,10)
    >>> list(ngrams(3, xs)) # doctest: +NORMALIZE_WHITESPACE
    [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7],
     [6, 7, 8], [7, 8, 9], [8, 9, None], [9, None, None]]
    >>> list(ngrams(2, xs, pad_right=-1)) # doctest: +NORMALIZE_WHITESPACE
    [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9],
     [9, -1]]
    >>> list(ngrams(3, xs, pad_left=-1)) # doctest: +NORMALIZE_WHITESPACE
    [[-1, -1, 0], [-1, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5],
     [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, None], [9, None, None]]
    >>> list(ngrams(3, []))
    []
    >>> list(ngrams(3, ['a', 'b']))
    [['a', 'b', None], ['b', None, None]]
    >>> list(ngrams(2, ['a', 'b']))
    [['a', 'b'], ['b', None]]
    """
    i = 0
    if pad_left is not None:
        j = 1
    else:
        j = n
    cap = len(xs)
    while True:
        if i == cap:
            raise StopIteration
        if j >= cap:
            diff = n - (cap - i)
            yield xs[i:] + [pad_right] * diff
        else:
            ldiff = n - j
            if pad_left is not None and ldiff > 0:
                yield [pad_left] * ldiff + xs[i:j]
                i -= 1
            else:
                yield xs[i:j]
        i += 1
        j += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
