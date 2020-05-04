import numpy as np
import rcovdata


def get_gom(lseg, rxyz, rcov, amp):
    # s orbital only lseg == 1
    nat = len(rxyz)
    om = np.zeros((nat, nat))
    if lseg == 1:
        for iat in range(nat):
            for jat in range(nat):
                d = rxyz[iat] - rxyz[jat]
                d2 = np.vdot(d, d)
                r = 0.5/(rcov[iat]**2 + rcov[jat]**2)
                om[iat][jat] = np.sqrt( 4.0*r*(rcov[iat]*rcov[jat]) )**3 \
                    * np.exp(-1*d2*r) * amp[iat] * amp[jat]

    return om


def get_fp_nonperiodic(rxyz, types):
    rcov = []
    amp = [1.0] * len(rxzy)
    for x in types:
        rcov.append(rcovdata.rcovdata[x][2])
    gom = get_gom(1, rxyz, rcov, amp)
    fp = np.linalg.eigvals(gom)
    return fp

def get_fpdist_nonperiodic(fp1, fp2):
    return np.sqrt(np.vdot(fp1, fp2)) / len(fp1)







