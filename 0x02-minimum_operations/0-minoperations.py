#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    my_count = 0
    whiteboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if whitboard == 0:
            # init (the first copy all and paste)
            whiteboard = done
            done += whiteboard
            my_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            whiteboard = done
            done += whiteboard
            my_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif whiteboard > 0:
            # paste
            done += whiteboard
            my_count += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return my_count
