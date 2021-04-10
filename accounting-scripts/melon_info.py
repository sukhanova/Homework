"""Print out all the melons in our inventory."""


# from melons import melon_names, melon_seedlessness, melon_prices


# def print_melon(name, seedless, price):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])


#SOLUTION:
# importing data from melons.py file
from melons import melons

def get_all_melons(melons):
    """Print each melon with corresponding attribute information. """
#we keep in melon_info price, flesh color, rind color and average weight
    #loop over melons dictionary to get melon name and rest of attributes 
    for melon, melon_info in melons.items():
        print(f"{melon.upper()}:")
        #loop over rest of melon attributes to retrieve rest of data and print them in format key: value
        for key, value in melon_info.items():
            print(f"{key}: {value}")
        #print statement to separate each record for better readability
        print()

get_all_melons(melons)