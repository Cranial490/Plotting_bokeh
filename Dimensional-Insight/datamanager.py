import uuid
import random
import csv

class DataHandler:
    def __init__(self, seed=5, datapoints = 10000) -> None: 
        self.data = []
        random.seed(seed)
        self.datapoints = datapoints

    def create_data(self, x_max, y_max, categories):  
        for idx in range(self.datapoints):
            id = uuid.uuid1()
            category = categories[random.randint(0,len(categories)-1)]
            x = random.randint(0, x_max)
            y = random.randint(0, y_max)
            self.data.append([category, id, x, y])
        return self.data

    def write_csv(self, header = None,  filename="datafile.csv"):
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            if header:
                csvwriter.writerow(header)
            csvwriter.writerows(self.data)

    def read_csv(self, filename):
        with open(filename) as csvfile:
            csvData = list(csv.reader(csvfile, delimiter=','))
        return csvData

filename= "datafile.csv"
header = ["Category", "ID", "X", "Y"]
data = []
x_max = 10000
y_max = 10000
categories = ["Alpha", "Beta", "Gamma", "Delta"]
dg = DataHandler(seed=10)
# print(dg.read_csv("dummyData.csv"))
dummyData = dg.create_data(x_max, y_max, categories)
dg.write_csv(header, "dummyData1.csv")

    