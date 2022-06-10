import csv
from sciHub_download import SciHub

class SH_parse:
  def __init__(self):
    self.sh_handler = SciHub(urls=["https://sci-hub.hkvisa.net"])

    self.auth_file = open("data/SSORC_CSMedPhys_10_20_authname_authid.csv", 'r', newline='')
    self.paper_file = open("data/SSORC_CSMedPhys_10_20_paperid_papertitle_authornames.csv", 'r', newline='')
    self.doi_file = open("data/SSORC_CSMedPhys_10_20_title_year_doi.csv", 'r', newline='')

    self.auth_iter = csv.reader(self.auth_file, delimiter=',', quotechar='"')
    self.paper_iter = csv.reader(self.paper_file, delimiter=',', quotechar='"')
    self.doi_iter = csv.reader(self.doi_file, delimiter=',', quotechar='"')
    # skip first line
    self.auth_iter.__next__()
    self.paper_iter.__next__()
    self.doi_iter.__next__()

  def next_pdf(self, save = False):
    id, title, year, doi = self.doi_iter.__next__()
    result = self.sh_handler.fetch(doi)
    if 'err' in result:
      return
    else:
      if save:
        self.sh_handler._save(result['pdf'], f"pdf/{id}.pdf")
      return result
