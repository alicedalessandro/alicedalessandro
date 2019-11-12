#INS
def inserction_sort(l):
    swaps = 0
    for i in range(1,len(l)):
        j = i
        while j > 0 and l[j-1]> l[j]:
            l[j], l[j-1] = l [j -1], l[j]
            j -= 1
            swaps += 1
    return swaps
s = "364185 6768 -96557 -28281 -17004 67699 41266 -34741 -94377 27226 89946 -1423 -83069 23432 -79485 -71615 -90813 73632 62092 -42399 -39771 84680 61013 80038 36090 -54004 265 -59383 -14729 -69286 -25419 -53267 -58569 -3375 -16435 64732 -51908 53778 70090 19287 -25861 -86569 31443 -97384 -29961 32079 -99266 96778 -14915 -15048 -7645 68641 22487 -12373 -74179 8185 4268 -94931 63545 -3586 -59307 -69160 -30722 7772 34706 -44202 -22700 38797 50854 15369 7088 -4510 66409 80410 26593 72673 43347 -62688 80476 -44490 13429 53517 13812 15171 91299 -49012 -46320 -50903 76992 16134 -93508 51877 -92709 92614 27264 40289 72737 34155 32605 -90380 -11296 -6828 95225 -31849 -14358 -33407 81786 36589 9462 -70206 -50124 99468 -92777 67167 -65915 21739 72555 26022 71428 66353 22595 99406 99747 -967 -64232 3397 48675 33332 75430 70245 -37765 -47166 51917 -33672 -97911 55966 -59462 69637 21329 -58728 84549 92294 60923 10607 -14083 -98673 43882 -37098 -37655 41264 87454 -81528 -73887 -70541 89309 26977 86169 48795 -49357 51288 34332 -33585 66776 52024 73062 93454 84585 14880 -3522 -26816 25385 -3463 -24343 50411 -32007 -9731 -62155 -98305 -79302 -47660 6298 -73034 -59552 -81603 64621 -75679 -92096 44020 -9979 4528 -56135 71119 -90982 -712 6277 -50347 61331 93191 10065 -58923 -89555 44784 -33304 5058 -4663 -35605 60683 8738 -52244 -77970 9464 -55812 19114 -57017 -7200 82937 -44335 -87502 -3437 86927 297 -66931 -80765 7454 46410 -71985 -64077 -4872 22624 -59687 -58005 65271 -75224 -41432 -84931 -76631 78556 97804 -52739 98415 85272 34395 -21633 78603 49970 -46191 -62909 -59490 49290 4663 -21471 -72906 24469 -84053 -74871 -6667 45925 -81443 66623 -42171 -81484 -98970 -70285 -5863 41091 -71456 24092 -81705 -22229 53389 8147 -79583 -99498 36464 68837 29430 -81907 21884 79529 -37643 -31399 -44636 92647 -6404 10589 -75255 -60111 -6789 -69948 -43059 35350 -28774 93042 6331 -15818 -97510 -15807 93910 -15288 21113 48876 86776 44091 -58480 -53166 -64282 10399 60802 42496 67386 24472 12960 75687 -52690 74337 5930 51063 -9840 -85396 16501 -78374 25656 -85895 83281 -69737 16653 20834 57709 64403 46601 -21609 -53496 -69250 81569 -29312 18981 -33892 -58051 47108 -83758 -21203 96867 83309 98895 61524 -21967 40046 -84143 -64548 -92881 72717 881 52846 -39246 42705 -32785 11688 -70599 -59145 33588 91725 -65058 -38765 -33790 6240 95546 -8124 73508 64824 -44139 52594 77770 -20128 59796 58843 93489 78742 -60188 -45397 -23245 101 19734 -41741 -93580 97279 2186 -34404 -821 -99422 7 -98631 89877 31164 79517 84547 78793 -40136 -34925 -8587 86459 -91913 92566 60860 -82326 86475 -42163 97424 -40446 73195 -79647 13617 90922 73021 -66127 -26615 17060 -32018 -98310 11663 14407 41720 -98223 94929 -69185 71303 -47255 -11453 -14200 -16259 73030 3428 -59780 4780 46615 -57890 -43872 -59927 -11938 -87062 90632 3854 -77923 -56254 -57395 16120 99335 -47282 -30333 -33196 33863 -26330 -14798 -92980 -47583 -7255 -37726 25265 -90251 98582 -62874 23533 46350 -63651 49966 97657 -72616 -93948 -12444 23313 95660 95600 17623 -38081 -21166 -2827 13107 -77495 -76965 -87084 9438 -50043 14910 69614 20058 -90176 14829 -58295 -30097 89185 86727 -95814 98892 -35271 84018 -4677 99656 97853 -15169 10785 9699 -91872 99097 79978 35139 -44683 66540 -75199 -92381 -91321 71842 21166 63703 -57155 74104 -17207 56662 -47339 24268 -98889 46486 77974 -12944 1736 -19335 -84898 75982 -80658 -34327 -68360 62587 -29055 -54198 -28330 56067 39920 15040 9840 -53877 -38516 -7195 81649 -12805 -1684 20496 -38358 15003 -19567 77180 15748 4734 95137 69298 83549 25601 -81259 -55486 -25095 17901 20472 64484 -88408 67219 84652 -38454 55580 91382 -20192 -26568 90215 43160 -77727 61314 -9759 75450 18668 44632 34542 -45225 -61036 -52461 -78681 -5075 63515 -22763 -20026 27204 59511 10952 -13883 -64394 -6947 -59665 -31432 -41773 -27668 67732 -13785 76354 -46966 -12514 32457 65251 68997 -86830 -96190 -25434 11538 -6612 50460 99533 56938 46300 31084 -64302 63425 -36563 95365 -96540 10526 -55735 -42373 -97837 68919 -81127 12620 50304 -23264 -76630 -19569 -49895 29548 66747 6697 26847 2207 21635 62115 99859 -14730 4819 -83593 -25474 4253 82696 -10376 18343 17214 40495 -60844 27706 96847 -82616 -85457 73349 -17247 650 -72570 -67564 33619 37506 9326 -28059 -15902 97708 -38255 -63531 85146 -77776 -55220 2892 58122 45906 58001 46179 41857 42035 12312 -26000 -28859 60832 -44167 -12024 -76320 92597 76644 -71620 -86244 -80847 65468 -83171 28801 -4545 44306 -8522 -77284 -38621 -79097 12234 24486 -19918 68755 -13482 -91448 -98475 -29828 -30409 -29907 98272 -18617 -28450 79225 -73073 -82329 -51796 -78725 -30868 -25239 48001 -89222 60560 30192 -75199 -58409 -66027 -6111 42969 87776 28560 44801 96085 -56239 -22655 26833 81964 74382 81437 7905 -81376 -49377 -47504 24951 95094 47498 98026 56745 -77044 15369 6865 -17248 -66351 94147 95167 -71057 79646 72065 88706 -98484 -82431 33599 -86069 -20674 19242 67652 51264 -76499 -50820 -89502 -10810 92586 -62776 95272 6840 53331 -40757 -17389 -1422 -32059 94205 64811 19761 -10563 80371 -92511 4610 9759 -62161 -83570 15943 37122 -38833 -3966 -87583 -20943 -50245 -68256 -89100 -85583 35669 51161 -24351 55464 -52261 -23165 37928 43479 37798 -20178 -17063 -49260 -84645 86388 5304 -60987 17394 193 -34720 -72662 41397 -11548 -38226 98498 61013 60040 39301 -51880 -63012 -71376 2549 16931 -93820 -70835 22669 -45662 32950 24823 -49415 -19819 83475 -35152 41023 63804 -43430 -46093 76182 58445 -38519 -3216 7973 29768 71005 -38589 -62524 31654 -71539 76646 86155 3747 -89618 -72234 -88848 -71566 -16999 -46095 -82586 758 -60444 -2339 -13165 -94172 -35012 91687 -77859 -47678 13183 51413 -22682 99145 -9193 -48929 -72158 80263 82619 -43854 -41587 60362 91546 -23843 -71540 -61152 -66203 -44776 4523 -93716 -51104 35808 90828"
l = list(map(int, s.split()))
print(inserction_sort(l))
