#Kensho Kuremoto
#5/June/2025
#Homework 3, Part 1

#Any comments without numbers are just there to explain what’s going on in my head.

#Lists

#1.Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22, 90, 0, -10, 3, 22, 48]
#2.Display the number of elements in the list.
print(len(numbers))
#3.Display the 4th element of this list.
print(numbers[3])
#4.Display the sum of the 2nd and 4th element of the list.
print(numbers[1] + numbers[3])
#5.Display the 2nd-largest value in the list.
sorted_numbers = sorted(numbers)
print(sorted_numbers[-2])
#6.Display the last element of the original unsorted list
print(numbers[-1])
#7.Display the sum of all of the numbers divided by two.
sum_half_numbers = sum(numbers) / 2
print(sum_half_numbers)
#8.Print whether the median or the mean of the numbers is higher
mean = sum(numbers) / len(numbers)

import statistics
median = statistics.median(numbers)
print(median)
#I really struggled with calculating the median, but the internet came to the rescue and showed me there’s a super handy thing called `median`.

if median > mean:
    print(median)
else:
    print(mean)

#Dictionaries1-movie

#1)Define the dictionary with title, year, and director
movie = {
    'title': 'Spirited Away',
    'year': 2001,
    'director': 'Hayao Miyazaki'
}

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

#2)budget and revenue
movie['budget'] = 2_000_000_000
movie['revenue'] = 31_680_000_000

profit = movie['revenue'] - movie['budget']
profit_B = profit / 1_000_000_000
print(f"The difference between the budget and the revenue is {profit_B:.1f}B yen.")

#3)Evaluate investment
if movie['revenue'] < movie['budget']:
    print("That was a bad investment.")
elif movie['revenue'] >= movie['budget'] * 5:
    print("That was a great investment.")
else:
    print("That was an okay investment.")

#Dictionaries2-NYC

#4)(Unit: millions)
population = {
    'Manhattan': 1.6,
    'Brooklyn': 2.6,
    'Bronx': 1.4,
    'Queens': 2.3,
    'Staten Island': 0.47
}
#5)Display the population of Brooklyn.
print(f"the population of Brooklyn is {population['Brooklyn']} million")

#6) Display the combined population of all five boroughs.
total_population = sum(population.values())
print(f"the combined population of all five boroughs is {total_population} million")

#7) Display what percent of NYC's population lives in Manhattan.
manhattan_share = (population['Manhattan'] / total_population) * 100
print(f"what percent of NYC's population lives in Manhattan is {manhattan_share:.1f}%")

