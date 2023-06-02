''''Exercise: Python Dict and Tuples
We have following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	32
Pakistan21

Using above create a dictionary of countries and its population
Write a program that asks user for three type of inputs,
print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21
add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.
Solution'''

pop_data = {"china":143, "india":136, "usa":32, "pakistan":21}

print(pop_data)

def add():
    country=input("Enter country name to add ")
    country = country.lower()
    if country in pop_data:
        print("Country already exist in our dataset. Terminating")
        return
    p = input(f"Enter population for {country}")
    pop_data[country] =p
    print_all()

def remove():
    country = input("Enter country name to remove ")
    country = country.lower()
    if country not in pop_data:
        print("Country not exist in our dataset. Terminating")
        return
    del pop_data[country]
    print_all()

def query():
    country = input("Enter country name to remove ")
    country = country.lower()
    if country not in pop_data:
        print("Country not exist in our dataset. Terminating")
    else:
        print(f"Total Population of {country} is {pop_data[country]}")



def print_all():
    for country, p in pop_data.items():
        print(pop_data)



def main():
    op=input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower()== 'query':
        query()
    elif op.lower()== 'print':
         print_all()

if __name__ == '__main__':
    main()