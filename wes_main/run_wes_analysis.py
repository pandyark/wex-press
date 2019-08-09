import os
import argparse
import logging as log
from datetime import date

parser = argparse.ArgumentParser(description='Whole exome data analysis pipeline to generate variant annotation results from various starting '
                                     'datatype inputs: fastq|sam|bam|vcf')
parser.add_argument("--project", dest='project_name', required=True, help='give name to this project.')
parser.add_argument("--wd", dest='working_directory', required=True, help='path to working directory')
parser.add_argument("--dt", dest="input_datatype", required=True, help='type of input data, values fastq, sam, bam, vcf')

args = parser.parse_args()
work_dir = args.working_directory
data_type = args.input_datatype
project = args.project_name

log.basicConfig(filename='{}-{}-{}.log'.format(project, data_type, str(date.today())), filemode='a', format='%(name)s - %(levelname)s - %(message)s')

import os
root_dir = 'C:/Users/sid/Desktop/test'


def get_r1_fastq(dir, sample_name):
    try:
        for f in os.listdir(dir):
            if "R1" in f and sample_name in f:
                return f
    except Exception as e:
        print("Error occured while finding {} R1 fastq file:\n{}", sample_name, e)


def get_r2_fastq(dir, sample_name):
    try:
        for f in os.listdir(dir):
            if "R2" in f and sample_name in f:
                return f
    except Exception as e:
        print("Error occured while finding {} R2 fastq file:\n{}", sample_name, e)


def get_bam(dir, sample_name):
    try:
        for f in os.listdir(dir):
            if f.endswith(".bam") and sample_name in f:
                return f
    except Exception as e:
        print("Error occured while finding {} bam file:\n{}", sample_name, e)


def haplotype_caller(reference, subdir, dbSNP, ):
    for subdir, dirs, files in os.walk(work_dir):
        read1= get_r1_fastq(subdir)
        read2= get_r2_fastq(subdir)
        print("samtools index -r1 " + str(read1) + " -r2 " + str(read2) + " -o " + str(subdir))
        bam_file = get_bam(subdir)
        print(bam_file)


def main():
    print("hello")
if __name__ == '__main__':

    log.warning('This will get logged to a file')
    print("Starting analysis")
    main()





