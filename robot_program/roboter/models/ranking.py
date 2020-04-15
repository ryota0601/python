import csv
from collections import defaultdict


class CsvModel(object):
    '''
    test
    '''
    def __init__(self):
        self.ranking_result = []
        self.data = defaultdict(int)
        self.fieldnames = ['Name', 'Count']
        self.read_csv()

    def read_csv(self):
        with open('ranking.csv', 'r+') as ranking_file:
            reader = csv.DictReader(ranking_file)
            for row in reader:
                self.data[row['Name']] = int(row['Count'])
            return self.data

    def write_csv(self):
        with open('ranking.csv', 'w+') as ranking_file:
            writer = csv.DictWriter(ranking_file, fieldnames=self.fieldnames)
            writer.writeheader()

            for restaurant, count in self.data.items():
                writer.writerow({'Name': restaurant, 'Count': count})

    def popular(self, not_list=None):
        if not_list is None:
            not_list = []

        sorted_data = sorted(self.data, key=self.data.get, reverse=True)
        for name in sorted_data:
            if name in not_list:
                continue
            return name

    def increment(self, restaurant):
        self.data[restaurant] += 1
        self.write_csv()
