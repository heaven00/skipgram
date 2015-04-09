import numpy as np
import timeit


def skipgram_ndarray(sent, k=1, n=2):
    """
    This is not exactly a vectorized version, because we are still
    using a for loop
    """
    tokens = sent.split()
    matrix = np.zeros((len(tokens), k + 2), dtype=object)
    matrix[:, 0] = tokens
    matrix[:, 1] = tokens[1:] + ['']
    result = []
    for skip in range(1, k + 1):
        matrix[:, skip + 1] = tokens[skip + 1:] + [''] * (skip + 1)
    for index in range(1, k + 2):
        temp = matrix[:, 0] + ',' + matrix[:, index]
        map(result.append, temp.tolist())
    return result


def skipgram_list(sent, k=1, n=2):
    """
    Form skipgram features using list comprehensions
    """
    tokens = sent.split()
    tokens_n = ['''tokens[index + j + {0}]'''.format(index)
                for index in range(n - 1)]
    x = '(tokens[index], ' + ', '.join(tokens_n) + ')'
    query_part1 = 'result = [' + x + ' for index in range(len(tokens))'
    query_part2 = ' for j in range(1, k+2) if index + j + n < len(tokens)]'
    exec(query_part1 + query_part2)
    return result

if __name__ == "__main__":
    text = """Pretty awesome except for the mate choice data.
            Yes, in all cultures studied men ranked appearance higher than
            women did, and women ranked ambition higher than men did.
            All cultures studied also contained within them the fact
            that women do not have equal economic opportunities,
            so of course a partner with earning power is important.
            So culture is playing a part here, but all cultures studied
            had the similar economic inequities so of course produced
            this difference. *When women make their own money, their
            desire for a good-looking partner, even a younger partner,
            increases* and I'm willing to bet if we analyzed the raw
            data we'd see less stark differences between men and women
            in this realm in cultures with lesser degrees of economic
            inequality.Another interesting point about that study
            (I believe it was David Buss's surveys from the 1990s)
            is that while men ranked beauty higher than women,
            women ranked ambition higher than men -- all people,
            male and female, in all cultures, ranked intelligence
            and kindness and their top requirements in a mate"""
    print "```````````````````````````````````````````````````````````````"
    loops_list = []
    timer_lc = []
    timer_ar = []
    for index in range(3):
        loops = 100 * 10 ** index
        loops_list.append(loops)
        timer_lc.append(timeit.timeit(lambda: skipgram_list(text, 1, 2),
                        number=loops))
        timer_ar.append(timeit.timeit(lambda: skipgram_ndarray(text, 1, 2),
                        number=loops))
    print "Loops, List comprehensions, ndarray\n"
    for index in range(len(loops_list)):
        print "{0}, {1}, {2}".format(loops_list[index], timer_lc[index],
                                     timer_ar[index])
