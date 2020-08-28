from GRSAlgo import *
import matplotlib.pyplot as plt
from typing import List


def rising_sequences(deck: np.array) -> int:
    """
    Methode for return no of rising sequence


    Parameters
    ----------
    deck: array
        shuffle deck of cards

    Returns
    -------
    out: int
        no of rising sequence -1
    """
    sorted_index = np.argsort(deck)
    return np.sum(np.diff(sorted_index) < 0)


def total_variation(prob_distribution_kth_shuffle: np.array,
                    approx_complete_shuffle: np.array) -> float:
    """
    Methode for total variation between kth shuffle and almost complete shuffle distribution

    Parameters
    ----------
    approx_complete_shuffle: array
        completed shuffle distribution
    prob_distribution_kth_shuffle: array
        distribution of observe shuffle

    Returns
    -------
    out: float
        total variation between kth shuffle and random distribution
    """

    t_variation = np.sum(np.abs(np.subtract(prob_distribution_kth_shuffle,
                                            approx_complete_shuffle))) * 0.5
    return t_variation


def multiple_gsr_shuffle(deck_size: int,
                         k_shuffle: int,
                         samples: int
                         ) -> list:
    """
    Methods for multiple Gilbert–Shannon–Reeds shuffle

    Parameters
    ----------
    deck_size: int
        number of cards in deck
    k_shuffle: int
        number of gsr_shuffle
    samples: int
        number of sample

    Returns
    -------
    out: list
        distribution of kth shuffle observation on samples

    """

    prob_distribution_kth_shuffle = []

    for deck_i in range(samples):
        shuffle_deck = np.arange(deck_size)

        for _ in range(k_shuffle):
            shuffle_deck = gsr_shuffle(shuffle_deck)

        prob_distribution_kth_shuffle.append(rising_sequences(shuffle_deck))

    # frequency of kth shuffle
    prob_distribution_kth_shuffle = np.bincount(prob_distribution_kth_shuffle,
                                                minlength=deck_size)/samples
    return prob_distribution_kth_shuffle


def calculating_total_variations(deck_size: int,
                                 samples: int,
                                 high: int,
                                 low: int = 0,) -> List[float]:

    """
    Methods for finding total variations for deck with low(inclusive) to high(exclusive) shuffle

    Parameters
    ----------
    deck_size: int
        number of cards in deck
    samples: int
        number of sample

    low: int
        minimum number of shuffle

    high: int 
        maximum number of shuffle

    Returns
    -------
    out: list
        list of total_variation for low to high shuffle
    """

    if deck_size < 0:
        raise ValueError(" deck size should be positive")

    if low < 0 or high < 0:
        raise ValueError(" number of shuffle should be more then 0")

    if low - high > 0:
        raise ValueError("low should be less then high")

    prob_dist_of_rising_seq = []

    # creating a complete shuffle
    for exp in range(samples):
        shuffle_deck = np.random.permutation(deck_size)
        prob_dist_of_rising_seq.append(rising_sequences(shuffle_deck))

    prob_dist_approx_complete_shuffle = np.bincount(prob_dist_of_rising_seq,
                                                    minlength=deck_size)/samples

    total_variation_list = []

    for k in range(low, high):
        prob_distribution_kth_shuffle = multiple_gsr_shuffle(deck_size=deck_size,
                                                             k_shuffle=k,
                                                             samples=samples)
        # add total variation for k shuffle
        total_variation_list.append(total_variation(prob_distribution_kth_shuffle,
                                                    prob_dist_approx_complete_shuffle))

    return total_variation_list


def plot_total_variation_graph(x: List[float],
                               y: List[float],
                               deck_size: int) -> None:
    """
    Method to plot and save graph

    Parameters
    ----------
    x: list
        list of x index

    y: list
        list of y value for corresponding x value

    deck_size: int
        number of cards in deck

    Returns
    -------
    None
    """
    plt.figure(figsize=(10, 6))
    plt.grid(True)
    plt.plot(x, y, '-bo')
    plt.xticks(x)
    plt.yticks(np.linspace(0, 1, 11))
    plt.title("Total variation for Deck of {} with x number of shuffle".format(deck_size))
    plt.xlabel("Number of Shuffle")
    plt.ylabel("Total Variation")
    plt.ylim(0, 1.1)
    plt.savefig("img/{}.png".format(deck_size))
    plt.show()
    plt.pause(3)
    plt.close()


def cutoff_phenomenon(deck_size_list: List[int],
                      samples: int,
                      low: int,
                      high: int,
                      plot: bool = True) -> List[float]:
    """
    Method to find Number of shuffle for randomize deck

    Parameters
    ----------
    deck_size_list: list,int
        list of deck

    samples: int
        number of sample

    plot: bool
        True then plot graph and save otherwise no

    low: int
        minimum number of shuffle

    high: int
        maximum number of shuffle

    Returns
    -------
    min_shuffle_list: list
        list of cutoff point(min shuffle for randomized) for all deck_size_list, if None found then add -1

    """
    # find min no of shuffle
    min_shuffle_list = []
    for deck_size_i in deck_size_list:
        print("start for deck size {}".format(deck_size_i))
        total_variation_distance_list = calculating_total_variations(deck_size=deck_size_i,
                                                                     samples=samples,
                                                                     low=low,
                                                                     high=high)

        #  find min shuffle to randomized cards
        min_shuffle = np.where(np.asarray(total_variation_distance_list) < 0.5)[0]
        if len(min_shuffle) > 0:
            min_shuffle_list.append(min_shuffle[0])
            if plot:
                plot_total_variation_graph(y=total_variation_distance_list,
                                           x=list(np.arange(low, high-low + 1)),
                                           deck_size=deck_size_i
                                           )

        else:
            print("Maybe More then {} shuffles are needed".format(high))
            min_shuffle_list.append(-1)

    return min_shuffle_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--deck_size_list', default=[26, 52, 104], help='Add Deck size', type=int, nargs='+')
    parser.add_argument('--samples', default=10000, help='Add sample size', type=int)
    parser.add_argument('--plot', action='store_false', help='Add low no of shuffle')
    parser.add_argument('--low', default=1, help='Add max number of shuffle', type=int)
    parser.add_argument('--high', default=20, help='Add max number of shuffle', type=int)

    opt = parser.parse_args()
    print(opt)
    min_shuffle_list = cutoff_phenomenon(opt.deck_size_list,
                                         samples=opt.samples,
                                         low=opt.low,
                                         high=opt.high,
                                         plot=opt.plot
                                         )

    with open("output.txt", "w+") as f:
        f.write(str(min_shuffle_list))




