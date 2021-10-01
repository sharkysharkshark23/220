"""
Name:Thomas Scola
traffic.py
Problem: calculate average car on each road for each day
Certification of Authenticity: I certify that this is entirely my own work.

"""
def main():
    n_roads = eval(input("Enter the number of roads surveyed: ")) #input the num of roads
    car_total = 0
    average = 0
    car_average = 0

    for num in range(n_roads): #first loops
        strng = str(num + 1)
        n_days = eval(input("Enter the number of days road " + strng + " was surveyed: "))
        total = 0

        for num2 in range(n_days): #second loop
            strng2 = str(num2 + 1)
            n_cars = eval(input("Enter the number of cars traveled on day " +strng2+ ":"))
            total += n_cars

            average = total / n_days
            car_total += n_cars
            car_average = car_total / n_roads

        print("Road " + strng + " average vehicles per day: ", round(average, 2))
    print("Total number of vehicles traveled on all roads: ", round(car_total, 2))
    print("Average number of vehicles per road: ", round(car_average, 2))

if __name__ == '__main__':
    main()