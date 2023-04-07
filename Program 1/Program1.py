def highest_rainfall(cities, rainfall):
    largest = rainfall[0]
    city = cities[0]
    for i in range(len(cities)):
        if rainfall[i] > largest:
            largest = rainfall[i]
            city = cities[i]
    return (city, largest)

def smallest_rainfall(cities, rainfall):
    smallest = rainfall[0]
    city = cities[0]
    for i in range(len(cities)):
        if rainfall[i] < smallest:
            smallest = rainfall[i]
            city = cities[i]
    return (city, smallest)

def mean(rainfall):
    total = 0
    for i in range(len(rainfall)):
        total += rainfall[i]
    return total/len(rainfall)
def number_of_cities_greater(mean, rainfall):
    count = 0
    for i in range(len(rainfall)):
        if mean < rainfall[i]:
            count += 1 
    return count

def main():
    cities = []
    rainfall_length = []
    myFile = open("rainfall.txt","r")
    lines = myFile.readlines()
    for line in lines:
        city, rainfall = line.split(" ")
        cities.append(city)
        rainfall_length.append(float(rainfall)*2.54)
    print('Highest Rainfall: ' + str(highest_rainfall(cities, rainfall_length)))
    print('Lowest Rainfall: ' + str(smallest_rainfall(cities, rainfall_length)))
    print('Average Rainfall: ' + str(mean(rainfall_length)))
    print('Number Of Cities Above Average Rainfall: ' + str(number_of_cities_greater(mean(rainfall_length), rainfall_length)))
    
if __name__ == '__main__':
    main() 

