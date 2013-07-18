# Copyright 2011, TriMet
#
# Licensed under the GNU Lesser General Public License 3.0 or any
# later version. See lgpl-3.0.txt for details.
#
import os
import sys
import time
from ott.abrev.osm_abbr_parser import OsmAbbrParser


def main():
    parser = OsmAbbrParser()
    data = parser.dict("834 Southeast Lambert Street")
    print data

if __name__ == '__main__':
    start_seconds = time.time()
    start_time = time.localtime()
    print time.strftime('begin time: %H:%M:%S', start_time)

    main()

    end_time = time.localtime()
    print time.strftime('end time: %H:%M:%S', end_time)
    process_time = time.time() - start_seconds
    print 'processing time: %.0f seconds' %(process_time)
