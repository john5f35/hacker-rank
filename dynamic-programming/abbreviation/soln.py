#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    tbl = {}
    def _sub(i, j):
        if a[i].isupper():
            return a[i] == b[j] and tbl[(i - 1, j - 1)]
        return ((a[i].upper() == b[j] and tbl[(i - 1, j - 1)]) or tbl[(i - 1, j)])

    tbl[(-1, -1)] = True
    tbl.update({(i, -1): a[i].islower() for i in range(len(a))})
    tbl.update({(-1, j): False for j in range(len(b))})

    for j in range(len(b)):
        for i in range(len(a)):
            res = _sub(i, j)
            tbl[(i, j)] = res

    return _sub(len(a) - 1, len(b) - 1)

def test_1():
    assert abbreviation("AbcDE", "ABDE")

def test_2():
    assert abbreviation("daBcd", "ABC")

def test_3():
    assert not abbreviation("daBEcd", "ABC")

def test_4():
    assert not abbreviation("AfPZN", "APZNC")

def test_5():
    a = "laalsAsaasLbbabLslalBbssaAsAlSLsbBllsSalblsssbsaaaAsabBaaAaalsssasssssLbasbbllbbLSsslbabAbSlllsbsbbalbBaSaaalbslaabAAaaabsabSlsassSshBBllbAAllsSbaLblabsaLBasBsAlLaabBbAllbaslsllsaAaAabbSallbLalsslbbblbasBAsbaBLalbBssbbAlbbbsSlsllbaLBLaaLblalBSbsBbSsbbaaSlllsblbsSaaBbassslaalblBbslLlaASASbbabbLlbalSabbBbLsbaabbalsAAbSbBbABbabbabaallBsasllbsbbsslSsbBlBlbabaalblaLsllbasasalabllSsbslLbsllbLsBlaSbssSAbsSasbsSalsabbllbbaBSBlabsBlAsbaSLbSllbsAblllSLaaAlBssSsBSLslAAlsbslbalsbSbsbalbsBabSbbsssaaabassalslllbsSLSsaLlbbBslSlSbbslsbslSLbbSbAaaaalLlSlAslsbmslbbalblLabSslassBabllSAsbbsvLllSalalbsaaaLAaSSbLbblaaSbLaalABlabsAsBsalssbBLlsLssaabsslabpSbsBaBbbSBlsaaabbblslBAblsLaASlaAlbaaSssbblalAaasbaalbLlaabbAaaaaAalsabbsllaaAsallsasBbAaslbbsbllbbllbslaBASbbSblaAbbsbbssAaBbsasLllalBlslssasbssBALAasbbsbSfasabbllbAslbalbaSSlslbbSbsaBsAalablAbbaBBsbsSbdaAsBblsblbABbLAssAbalsbssSssbBBssAsABLssblsLbllSblasllLbBsassllBbBbsbBsbllsBBsAbbLLlAslBlsAAASlaalabasaLslasBLlsslsaaslsbblbAsalSlllsLSAaLlalAalsBsaslaaaalb"
    b = "ALASALABLABBASASLSBLSSLSSASBBAASSSLBBLLSSBAASLBBASBSLAAASSSSSBBLAALSALLBASBALLBBABASLLSAAAASLBBABABLABBALBSALBLLLBSSBSSAASSBBALALBBBSLLLASASLASABBBLASAASBBABAAALBLLBSSBBLBLBLLLAALLLSSSLLSLLBSSSABSSSSSBABSBLASBASSLBSLSASLAALBSBSLAASBSSBBSBBSSLLBSLSSLLBBLSLSSLBBSAALSASLSLBSABALSASLLLSLLAASSLBASBLAAABBABSBLLASASSBABBSBBBBLBABSLAASAASSSBLALAAASBLLBBAAABBLAABASSBBBLBLABASBSLAABBBSAABBASLLBSSSBBALASBSSBBASSLSBABABBBSSAABBLBABLAAABSBBSAABLSSSLSLLBALBBBBBSBBSABLLABLSAAASLABAALSABLSLBLBASASLLSALAABAAAALB"
    assert abbreviation(a, b)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(("YES" if result else "NO") + '\n')

    fptr.close()
