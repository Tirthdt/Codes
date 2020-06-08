"""
Bear Limak wants to become the largest of bears, or at least to become larger than his brother Bob.

Right now, Limak and Bob weigh a and b respectively. It's guaranteed that Limak's weight is smaller than or equal to his brother's weight.

Limak eats a lot and his weight is tripled after every year, while Bob's weight is doubled after every year.

After how many full years will Limak become strictly larger (strictly heavier) than Bob?

4 7 
o/p: 2

4 9
o/p: 3
"""

limak_weight, bob_weight = map(int, input().split())
years = 0

while limak_weight <= bob_weight:
    limak_weight *= 3
    bob_weight *= 2
    years += 1

print(years)
