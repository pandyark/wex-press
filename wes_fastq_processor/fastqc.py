import yaml
from wes_main.run_wes_analysis import log


config=''

with open("example.yaml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        log.ERROR(exc)

def run_fastqc(r1_fastq, r2_fastq):
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        log.ERROR(exc)