FROM python:latest
#add python script and necessary files

ADD Almaden_coding_challenge.py /
ADD sequences.txt /
ADD SRR11772358_1M_filtered_1.fastq /

#need to install dependencies
RUN pip install regex biopython
#map volume



CMD ["python", "Almaden_coding_challenge.py"]
