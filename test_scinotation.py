#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_scinotation.py
2018/11/18 21:41:19



Copyright 2018 Daniel Belasco Rogers dan@planbperformance.net
"""

import sys
import time
from gpx2spatialite import gpx


def main():
    """
    """
    starttime = time.time()
    gpx_path = 'tests/data/GreenwichMeridianWalk-Viking.gpx'
    extracted_points = gpx.extractpoints(gpx_path)

    # print geom field from trkpoints returned by extractpoints
    for point in extracted_points[0]:
        print(point[7])

    print("--- {} seconds ---".format(time.time() - starttime))


if __name__ == '__main__':
    sys.exit(main())
