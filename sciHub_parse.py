import json
import grobid_requests as scipdf
import csv
from sciHub_download import SciHub


class SH_parse:
    def __init__(self):
        self.sh_url = "https://sci-hub.hkvisa.net"
        self._sh_handler = SciHub(urls=[self.sh_url])

        self._auth_file = open("data/SSORC_CSMedPhys_10_20_authname_authid.csv", 'r', newline='')
        self._paper_file = open("data/SSORC_CSMedPhys_10_20_paperid_papertitle_authornames.csv", 'r', newline='')
        self._doi_file = open("data/SSORC_CSMedPhys_10_20_title_year_doi.csv", 'r', newline='')
        self._auth_iter = csv.reader(self._auth_file, delimiter=',', quotechar='"')
        self._paper_iter = csv.reader(self._paper_file, delimiter=',', quotechar='"')
        self._doi_iter = csv.reader(self._doi_file, delimiter=',', quotechar='"')
        # skip first line
        self._auth_iter.__next__()
        self._paper_iter.__next__()
        self._doi_iter.__next__()
        
    def _next_paper(self):
        id, title, year, doi = self._doi_iter.__next__()
        _id, paper_id, _title, authors = self._paper_iter.__next__()
        return {
                "id": id,
                "title": title,
                "year": year,
                "doi": doi,
                "paper_id": paper_id,
                "authors": authors
        }

    def next_pdf(self, save=False, save_name=None):
        paper_info = self._next_paper()
        result = self._sh_handler.fetch(paper_info['doi'])
        get_url = result["url"]
        binary = None
        if not ('err' in result):
          binary = result["pdf"]
          if save:
            self._sh_handler._save(binary, f"pdf/{paper_info['id'] if save_name is None else save_name}.pdf")
        ret_dict = paper_info.copy()
        ret_dict['url'] = get_url
        ret_dict['binary'] = binary
        return ret_dict


results = []
if __name__ == "__main__":
    parser = SH_parse()
    for i in range(50):
        result = parser.next_pdf(save=True)
        if result['binary'] is None:
            print("ERR: ", f"failed loading article with ID: {result['id']}, named: {result['title']}")
        else:
            print("LOG: ", f"loaded article with ID: {result['id']}, named: {result['title']}")
            article_dict, parsed_article = scipdf.parse_pdf_to_dict(f'pdf/{result["id"]}.pdf', fulltext=True)
            with open(f"grobid_out/{result['id']}.html", "w") as f:
                for line in parsed_article:
                    f.write(str(line))
            with open(f"recognized/{result['id']}.json", "w") as f:
                json.dump(article_dict, f, indent=4)