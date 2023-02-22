#!/usr/bin/env python
# coding: utf-8


#required libraries for program 
import re
from Bio import SeqIO

#create list of subsequences
seq_file = 'sequences.txt'
with open(seq_file, "r") as seq:
    seqs = [line.strip() for line in seq.readlines()]

#function to find subsequence matches and output results to new fastq file
def find_matches(output_file, fastq_file):
    #write to new file
    with open(output_file, "w") as output:
        #isolate read information
        for record in SeqIO.parse(fastq_file, "fastq"):
            #iterate through subsequences in seqs list
            for item in seqs:
                #only write read to new file if subsequence is in it
                if item in str(record.seq):
                    SeqIO.write(record, output, "fastq")
        print('Done creating "hit_entries.fastq" file')
        
def create_hits_file(hits_output, fastq_file):
    #write to new file 
    with open(hits_output, 'w') as out_file:
        out_file.write('subsequence\tread\t\t\t\t\t\t\t\t\t\tcount\n')
        #isolate read information
        for record in SeqIO.parse(fastq_file, "fastq"):
            sequence = str(record.seq)
            for subseq in seqs:
                count = sequence.count(subseq)
                #if there is a count greater than 1 (all should have at least 1 match), then write subsequence, the read, and the count to new file
                if count > 0:
                    out_file.write(f"{subseq}\t{sequence}\t{count}\n")
        print('Done creating "hits.txt" file')

def main():
    output_file = '/output/hit_entries.fastq'
    fastq_file = 'SRR11772358_1M_filtered_1.fastq'
    hits_output = '/output/hits.txt'
    find_matches(output_file, fastq_file)
    create_hits_file(hits_output, output_file)
if __name__ == "__main__":
    main()






