import uuid
import random
import csv

class DataHandler:
    def __init__(self, seed=5) -> None: 
        random.seed(seed)

    def create_data(self, x_max, y_max, categories, datapoints):  
        data = []
        for idx in range(datapoints):
            id = uuid.uuid1()
            category = categories[random.randint(0,len(categories)-1)]
            x = random.randint(0, x_max)
            y = random.randint(0, y_max)
            data.append([category, id, x, y])
        return data

    def write_csv(self, data, header = None,  filename="datafile.csv"):
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            if header:
                csvwriter.writerow(header)
            csvwriter.writerows(data)

    def read_csv(self, filename):
        #TODO Handle file not exist
        try:
            with open(filename) as csvfile:
                csvData = list(csv.reader(csvfile, delimiter=','))
            return csvData
        except OSError as e:
            print(e)
            exit()

    def generate_dummy_data(self,filename, datapoints = 10000 , header = ["Category", "ID", "X", "Y"], categories = ["Alpha", "Beta", "Gamma", "Delta"]):
        filename= filename
        header = header
        x_max = 10000
        y_max = 10000
        categories = categories
        dummyData = self.create_data(x_max, y_max, categories, datapoints)
        self.write_csv(dummyData, header, filename)
