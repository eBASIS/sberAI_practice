from cv2 import sort
from sciHub_parse import SH_parse
years = {}
if __name__ == "__main__":
    parser = SH_parse()
    while True:
        result = parser.next_pdf(save=False)
        year = result['year']
        if not year in years.keys():
            years[year] = {
                "ok" : 0,
                "all" : 0
            }
        years[year]["all"] += 1
        if result['binary'] is None:
            print("ERR:", f"failed loading article with ID: {result['id']}, year: {year}")
        else:
            years[year]["ok"] += 1
            print("SUCCESS:", f"loaded article with ID: {result['id']},  year: {year}")
        print(*sorted(years.items()))