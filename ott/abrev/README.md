ott osm abbreviator
===================

Will take an OSM street name like 834 Southeast Lambert Street, and turn it into 834 SE Lambert St.  Will also break out the disparate name and street type and any prefix/suffix.

To see the parser run, try the following:
  bin/python ott/abrev/test.py
-or-
  bin/python ott/abrev/osm_abbr_tester.py

There's also ott/abrev/rename_streets.py, which has code to grab street names from a table in postgres, and rename the contents, etc...  (it's a bit more involved, and a bit ugly).

NOTE: the rename code is not very fast (especially, the rename_streets.py / database stuff)...basically, I got the code running reasonably well from a street parsing / abbreviating standpoint, and didn't have time to further refine or performance tune...
