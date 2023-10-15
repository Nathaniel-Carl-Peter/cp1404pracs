import csv

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPIONS = 2


def load_data(filename):
    """Read data from file"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove Header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def main():
    """Generate a dictionary of wimbledon"""
    records = load_data(FILENAME)
    champion_count, countries = process_records(records)
    display_results(champion_count, countries)


def display_results(champion_count, countries):
    """Display records"""
    print(f" Wimbledon Champions:")
    for name, count in champion_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", " .join(country for country in sorted(countries)))


def process_records(records):
    """Create dictionary of countries and champions"""
    champion_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_count[record[INDEX_CHAMPIONS]] += 1
        except KeyError:
            champion_count[record[INDEX_CHAMPIONS]] = 1
    return champion_count, countries


main()

"""
Wimbledon Champions: 
Rod Laver 2
...
Lleyton Hewitt 1
Roger Federer 8
Rafael Nadal 2
Novak Djokovic 7
Andy Murray 2

These 12 countries have won Wimbledon: 
AUS, CRO, ESP, FRG, GBR, GER, NED, SRB, SUI, SWE, TCH, USA

"""
