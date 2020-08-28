import numpy as np
import argparse


def should_drop_right_gsr(n_left: int,
                          n_right: int) -> bool:
    """
    Gilbert–Shannon–Reeds method for drop card from right or left

    Parameters
    ----------
    n_left: int
        size of left deck
    n_right:
        size of right deck

    Returns
    -------
    out: bool
        True then drop right deck
        False then drop left deck
    """

    if n_right > 0 and n_right > 0:

        return np.random.binomial(n=1, p=n_right / (n_left + n_right)) == 1

    elif n_right == 0 and n_left > 0:
        return False

    elif n_left == 0 and n_right > 0:
        return True
    else:
        raise ValueError("n_left or n_right value error")


def get_random_number_for_right_deck_gsr(n: int) -> int:
    """
    Gilbert–Shannon–Reeds method for split deck into two parts, righ and left sub-deck

    Parameters
    ----------
    n: int
        size of deck

    Returns
    -------
    out: int
         returns random integer between 0 and n (inclusive)

    """
    if n > 0:
        return np.random.binomial(n=n, p=1 / 2)

    raise ValueError(" n is negative or 0, it should be positive")


def gsr_shuffle(orig_deck: np.array) -> np.array:
    """
    Gilbert–Shannon–Reeds method for shuffling array without changing original array

    Parameters :
        orig_deck which has to be shuffle

    return:
        shuffle deck

    """

    if isinstance(orig_deck, list):
        orig_deck = np.asarray(orig_deck)

    orig_deck_size = orig_deck.shape[0]
    orig_right_deck_size = get_random_number_for_right_deck_gsr(orig_deck_size)
    left_deck_size = orig_deck_size - orig_right_deck_size

    shuffle_deck = np.empty(orig_deck.shape, dtype=np.int32)

    right_deck_size = orig_right_deck_size
    for i in range(orig_deck_size):

        if should_drop_right_gsr(left_deck_size, right_deck_size) is True:
            # Drop one bottom card from right deck
            shuffle_deck[i] = orig_deck[right_deck_size - 1]
            right_deck_size -= 1
        else:
            # Drop one bottom card from left deck
            shuffle_deck[i] = orig_deck[orig_right_deck_size + left_deck_size - 1]
            left_deck_size -= 1

    return shuffle_deck


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--deck_size', default=52, help='Add Deck size', type=int)
    opt = parser.parse_args()
    print(opt)
    deck = np.arange(opt.deck_size)
    shuffle_deck = gsr_shuffle(deck)
    print(shuffle_deck)

