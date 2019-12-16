cities = ['stockholm', 'new york', 'tokyo', 'berlin']

def contains(city):
    if city in cities:
        return True
    else:
        return False

print(contains(input('stad: ')))