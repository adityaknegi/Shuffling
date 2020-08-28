import unittest
import numpy as np
from riffle import shuffle
from GRSAlgo import gsr_shuffle


class TestRiffle(unittest.TestCase):
    def test_case_1(self):
        """
        Test shuffle for same set of values, input sequence preserve
        """
        print("-------------------shuffle-----------------------------------")
        for _ in range(10):
            deck_size = np.random.randint(low=1, high=100000)
            deck = np.arange(deck_size)
            shuffle_deck = shuffle(deck)
            self.assertEqual(sum(shuffle_deck), deck_size * (deck_size - 1) // 2)
            self.assertEqual(len(deck), len(shuffle_deck))
            self.assertSetEqual(set(shuffle_deck), set(deck))

        print("input sequence preserve ok: PASS")
        print("shuffle contain unique value ok: PASS")
        print("shuffle contain same set of value as deck ok: PASS")

    def test_case_2(self):
        """
        Test gsr_shuffle for same set of values, input sequence preserve
        """
        print("-------------------gsr_shuffle-----------------------------------")
        for _ in range(5):
            deck_size = np.random.randint(low=1, high=10000)
            deck = np.arange(deck_size)
            shuffle_deck = gsr_shuffle(deck)
            self.assertEqual(sum(shuffle_deck), deck_size * (deck_size - 1)//2)
            self.assertEqual(len(deck), len(shuffle_deck))
            self.assertSetEqual(set(shuffle_deck), set(deck))

        print("input sequence preserve ok: PASS")
        print("shuffle contain unique value ok: PASS")
        print("shuffle contain same set of value as deck ok: PASS")

    def test_case_3(self):
        """
        Test shuffle for diff seed
        """

        print("-------------------------shuffle-----------------------------------")

        deck_size = 10
        deck = np.arange(deck_size)
        shuffle_deck = shuffle(deck, my_seed=2)
        self.assertSequenceEqual(list(shuffle_deck), [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

        deck_size = 100
        deck = np.arange(deck_size)
        shuffle_deck = shuffle(deck, my_seed=39)
        self.assertSequenceEqual(list(shuffle_deck),
                                 [8, 7, 6, 5, 4, 3, 2, 1, 0, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85,
                                  84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64,
                                  63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43,
                                  42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22,
                                  21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9])

        deck_size = 333
        deck = np.arange(deck_size)
        shuffle_deck = shuffle(deck, my_seed=139)
        self.assertSequenceEqual(list(shuffle_deck),
                                 [332, 331, 330, 329, 328, 327, 326, 325, 324, 323, 322, 321, 320, 319, 318, 317, 316,
                                  315, 314, 313, 312, 311, 310, 309, 308, 307, 306, 305, 304, 303, 302, 301, 300, 299,
                                  298, 297, 296, 295, 294, 293, 292, 291, 290, 289, 288, 287, 286, 285, 284, 283, 282,
                                  281, 280, 279, 278, 277, 276, 275, 274, 273, 272, 271, 270, 269, 268, 267, 266, 265,
                                  264, 263, 262, 261, 260, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248,
                                  247, 246, 245, 244, 243, 242, 241, 240, 239, 238, 237, 236, 235, 234, 233, 232, 231,
                                  230, 229, 228, 227, 226, 225, 224, 223, 222, 221, 220, 219, 218, 217, 216, 215, 214,
                                  213, 212, 211, 210, 209, 208, 207, 206, 205, 204, 203, 202, 201, 200, 199, 198, 197,
                                  196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180,
                                  179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165, 164, 163,
                                  162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146,
                                  145, 144, 143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 131, 130, 129,
                                  128, 127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112,
                                  111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94,
                                  93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73,
                                  72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52,
                                  51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                                  30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9,
                                  8, 7, 6, 5, 4, 3, 2, 1, 0])

        print("random shuffle check for different seed ok: PASS")


if __name__ == '__main__':
    unittest.main()
