#!/usr/bin/env python

# 2BL: Bioinformatics surgery session 1
# Jan 28, 2015

# open a BLAST output file and assign it to the handle/variable "file_"
# remember: "file" is reserved and should not be used as a variable name
file_ = open('Go5_mock_C_vseffector_tab.txt')

# step through the file, line by line, or "for each line in file, do ..."
for line in file_: 
    # split the line into columns (line.split() assumes columns 
    # are separated by tab (\t) or space
    # the .strip() removes the newline character from the end of the line *)
    columns = line.strip().split()
    # get the evalue from the line 
    # located in column 11, but Python starts counting from 0
    evalue = float(columns[10])
    # if the evalue is below a threshold, in this case 0.5
    if evalue < 0.5:
        # then print the line
        # *) if we did not .strip() the line as above
        # the "print line" would add an extra line-break (\n)
        # after each line
        print line
        
        # for Yogesh, to extract FASTA sequences from a tab-separated file
        # replace "print line" with the following three lines
        # id_ = columns[0]
        # sequence = columns[whereever the sequence is located]
        # print '>%s\n%s\n' % (id_, sequence)
        #
        # this prints a so-called "formatted string", which
        # can be constructed from the data you are processing
        # %s means: any string, and \n is the line-break
        # so '>%s\n%s\n' translates to: 
        # >STRING1
        # STRING2
        # which looks just like a FASTA record.
        # % (id_, sequence) then provides the two strings
        # so that the result will be
        # >ID
        # SEQUENCE


# remember the script is executed "python blastParse.py > output.txt"
        
