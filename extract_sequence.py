#!/usr/bin/env python

# 2BL: Bioinformatics surgery session 4
# Mar 11, 2015

"""
The aim of this script is to take as input a FASTA file and a pair of
sequence coordinates and to write the FASTA-formatted region between
those specified coordinates to the command line.

Some notes:

General format of a (single sequence FASTA file
1 header line
followed by 1 or more sequence lines

>id
ACACGTACACCAGTACGGACT
ACACCACGTACCCGTACCGTA
GACCCAGTAGGACTTACCTAT

When the whole file is read into a Python-string, 
it will have the following format:

>id\nACCCCAGTAGCCATTGACCC\n

The different characters that mark the end of a line:
\n Linux, MacOSX
\r MacOS
\r\n Windows
"""


# open a FASTA file and assign it to the handle/variable "file_"
filename = 'top_secret_filename.fa'
file_ = open(filename)

# We read the file and split the resulting string by the line-end
# symbol '\n', thus creating a list [id, seq, ...]
data = file_.read().split('\n')
# We take the first two elements of that list
id_, seq = data[:2]

# These are the coordinates of our marker sequences.
# (Remember: marker coordinates are 1-based!)
start1, end1 = 125653, 125657
start2, end2 = 100230, 100234 

# We extract the sequence between the markers.
# For start2 we have to take into account that Python starts counting at 0.
# For end1 we don't, since seq[x:y] will only include characters x..(y-1).
rd_interval = seq[start2 - 1:end1]

# We can print the extracted sequence, together with its length for testing.
# print rd_interval, len(rd_interval)

# Finally, we print the extracted sequence in FASTA format to the
# command line '>rd_interval_%i-%i\n%s\n' is a formatted string,
# expecting data to be inserted at the %i and %s markers.  %i stands
# for any integer value, %s for any string We bind the data that makes
# up our desired output (the boundaries of the interval and the actual
# extracted sequence) to the formatted string using the % - operator.
# The data have to be supplied in a tuple (start2, end1, rd_interval).
sys.stdout.write('>rd_interval_%i-%i\n%s\n' % (start2, end1, rd_interval))

