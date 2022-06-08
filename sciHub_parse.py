import csv
from scihub import SciHub
from scidownl import scihub_download
# sh_handler = SciHub()
# result = sh_handler.fetch('https://ieeexplore.ieee.org/document/9666083/')

# if result:
#   with open('output.pdf', 'wb+') as fd:
#       fd.write(result.pdf)
# auth_file = open("data/SSORC_CSMedPhys_10_20_authname_authid.csv", 'r', newline='')
# paper_file = open("data/SSORC_CSMedPhys_10_20_paperid_papertitle_authornames.csv", 'r', newline='')
# auth_iter = csv.reader(auth_file, delimiter=',', quotechar='|')
# paper_iter = csv.reader(paper_file, delimiter=',', quotechar='|')

# for i in range(10):
#   #print("auth", auth_iter.__next__())
#   #print(paper_file.readline())
#   print(paper_iter.__next__())
paper = "https://doi.org/10.1145/3375633"
paper_type = "doi"
out = "./paper/one_paper.pdf"
scihub_download(paper, paper_type=paper_type, out=out)
