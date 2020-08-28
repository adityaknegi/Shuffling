import numpy as np
import argparse


def should_drop_from_right_deck(n_left: int,
                                n_right: int,
                                my_seed: int = None) -> bool:
    """
    Parameters
    ----------
    n_left: int
        size of left deck
    n_right: 
        size of right deck
    my_seed: int
        sudo random generator
    Returns
    -------
    out: bool
        True then drop right deck
        False then drop left deck
    
    """
    
    if n_left > 0 and n_right > 0:
        # if 1 then return False else True
        if my_seed:
            np.random.seed(my_seed)
        should_right = np.random.randint(low=0, high=2)
        return should_right == 1
    elif n_left == 0 and n_right > 0:
        return True
    elif n_right == 0 and n_left > 0:
        
        return False
    else:
        raise ValueError(" n_left or n_right ")
    

def get_random_number_for_right_deck(n: int,
                                     my_seed: int = None
                                     ) -> int:

    """   
    Parameters
    ----------
    n: int
        size of deck
    my_seed: int
        sudo random generator

    Returns
    -------
    out: int
         returns random integer between 0 and n (inclusive)
         
    """
    if my_seed:
        np.random.seed(my_seed)
    return np.random.randint(low=0, high=n + 1)


def shuffle(orig_deck: np.array,
            my_seed: int = None
            ) -> np.array:
    """

    shuffles array or list without changing original array and return shuffle array

    Parameters
    ----------
    orig_deck : array_like
        The array or list to be shuffled.
    my_seed: int
        sudo random generator
    Returns
    -------
    out: array
        return shuffle deck
    
    """

    if isinstance(orig_deck, (list, tuple)):
        orig_deck = np.asarray(orig_deck)

    shuffle_deck = np.empty(orig_deck.shape, dtype=np.int32)
    orig_deck_size = orig_deck.shape[0]

    # randomly divided into two parts,'left' and 'right' 'sub-decks'
    orig_right_deck_size = get_random_number_for_right_deck(orig_deck_size, my_seed)
    left_deck_size = orig_deck_size - orig_right_deck_size
    right_deck_size = orig_right_deck_size

    for i in range(orig_deck_size):

        if should_drop_from_right_deck(left_deck_size, right_deck_size, my_seed) is True:
            # Drop bottom card from right deck
            shuffle_deck[i] = orig_deck[right_deck_size - 1]
            right_deck_size -= 1
        else:
            # Drop bottom card from left deck
            shuffle_deck[i] = orig_deck[orig_right_deck_size + left_deck_size - 1]
            left_deck_size -= 1

    return shuffle_deck


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--deck_size', default=52, help='Add Deck size', type=int)
    parser.add_argument('--my_seed', default=None, help='Add seed value', type=int)

    opt = parser.parse_args()
    print(opt)
    deck = np.arange(opt.deck_size)
    shuffle_deck = shuffle(deck, my_seed=opt.my_seed)
    print(shuffle_deck)
