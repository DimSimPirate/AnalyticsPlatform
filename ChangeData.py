import csv

accessToken = 'pk.eyJ1IjoiZGltc2ltcGlyYXRlIiwiYSI6ImNqN2xlaDBrcjB4Y3IycXBrYmQ1NTJqOXYifQ._QznbTre_3HrSVnIHnDH-g'
incomeFilePath = 'incomeData.csv'
postCodesPath = 'NSWPostcodes.csv'
columnHeaders = ''
geojsonData = []
suburbRowLength = 18
suburbs = {}




def getPostcodeInfo():

    with open (postCodesPath) as csvfile:

        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row[4])
            if row[4] == "Delivery Area":
                suburb = {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [row[5], row[6]]
                    },
                    'properties': {
                        'name': row[1]
                    }
                }
                suburbs[row[1]] = suburb

getPostcodeInfo()
print(suburbs)

def getIncomeInfo():
    with open (incomeFilePath) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rangeCounter = 0
        incomes
        suburb = ''

        buffer = 10
        currentSuburb = ''
        rangeCounter = buffer
        incomes = []
        while rangeCounter < len(reader):
            currentSuburb = reader[rangeCounter][1]
            for i in range(0, suburbRowLength - 1):
                row = reader[rangeCounter]
                incomes[i] = int(row[3])
                rangeCounter = rangeCounter + 1
        createGeojson(currentSuburb, incomes)

def createGeojson(currentSuburb, incomes):
    return


#def write_json(self, features):
#    return
#{
#  "features": [
#    {
#      "type": "Feature",
#      "properties": {
#        "title": "Lincoln Park",
#        "description": "A northside park that is home to the Lincoln Park Zoo"
#      },
#      "geometry": {
#        "coordinates": [
#          -87.637596,
#          41.940403
#        ],
#        "type": "Point"
#      }
#    },
