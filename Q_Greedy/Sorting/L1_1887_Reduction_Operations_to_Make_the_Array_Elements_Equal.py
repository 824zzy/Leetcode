""" https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
greedy sorting from largest to smallest
"""
from header import *


class Solution:
    def reductionOperations(self, A: List[int]) -> int:
        cnt = Counter(A)
        pref = 0
        ans = 0
        for i, (_, f) in enumerate(sorted(cnt.items(), reverse=True)):
            if i != len(cnt) - 1:
                ans += f + pref
                pref += f
        return ans


"""
[5,1,3]
[1,1,1]
[1,1,2,2,3]
[23383,27160,22681,104,35290,35397,40862,40138,21702,30026,39313,1834,15048,41640,11614,36095,38304,11848,6004,36113,16731,2128,44114,4618,5455,1094,29688,955,49424,49519,18429,16356,17606,7176,40948,12099,22573,19025,4556,10976,10462,16726,34563,11020,43035,17886,42481,46635,19300,29800,46048,21103,32539,31050,7484,1549,20448,25334,22502,27586,12324,16936,7128,16611,47852,33431,13703,39692,28289,1365,14771,1171,26039,9599,2316,47110,10501,29208,46178,33182,44445,27962,35698,14458,41339,45551,33856,29547,14628,34335,42501,2012,25881,44231,37739,21054,43243,41350,27938,3853,48330,19570,8237,13903,3110,20080,4636,5010,20340,19522,48749,10369,27275,37024,16539,8546,556,36748,2485,38705,14261,37374,30203,11241,46139,40827,33350,2453,24771,13134,22737,6490,13485,37578,44182,28374,38759,12722,32267,6844,43645,25564,19404,33038,32755,1128,21322,40117,26367,18439,1186,10287,13164,21479,36920,8857,22223,28131,13962,17468,44202,6319,24854,35890,22535,45031,35018,31753,34900,15378,4281,47545,2648,5550,8718,11122,10916,35273,13958,17565,49750,21774,39336,33154,16731,24125,22207,22301,7466,19086,15414,39583,46866,32034,8871,38009,36122,6834,21020,2565,26647,4797,24919,9656,8194,22342,7517,40317,38497,24776,5024,37407,36063,14662,37092,5358,17481,23914,19370,36992,35016,7492,30001,18166,7061,2999,19382,812,40218,43937,954,6009,27102,7544,2623,12316,15705,38457,27592,10619,7574,29551,10970,44623,15822,10417,48760,6740,28515,24791,35582,19270,36059,16608,46637,31262,20609,6563,13607]
"""
