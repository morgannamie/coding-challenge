# coding-challenge
Almaden coding challenge repository 

## General Information
* This program is designed to retrieve genomic sequences/reads from "SRR11772358_1M_filtered_1.fastq" that contain matches for subsequences 
from "sequences.txt" and output results to a file titled "hit_entries.fastq"
* The program will then count occurrences of the provided subsequences in each sequence from "hit_entries.fastq"
* Result: two files will be created, "hits.txt", containing the subsequences, the read they are present in, and the count for number of times they appear in each read (files will be saved in directory in which you are running the program)
* Examples of those output files are in this repository 

## Libraries
* regex 
* Biopython

## Installations
* Biopython
* pip install biopython

## Docker Information
* Docker image created for this program (see Dockerfile)
* Save Dockerfile to a desired directory
* To Build/Run Docker image:
```
Step 1 (build image): docker build -t python-codingchallenge .
Step 2 (run container): docker run -v $(pwd):/output/ python-codingchallenge
* This should create the output files
```
* Alternatively, image be pulled from DockerHub repository using the bash script provided titled "invoke.sh"
```
Give permission: chmod +x invoke.sh
Calling script: ./invoke.sh 
* This should pull the image from the repository and create the output files
```

