my_list = [1,2,3]
def multiply_by2(item):
  return item*2

def only_odd(item):
  return item % 2 != 0

print(list(filter(only_odd, my_list)))


names = ['adam', 'alex', 'andrew', 'mark', 'logan']

def begin_with_a(name):
  return name[0] == 'a'

print(list(filter(begin_with_a, names)))

scores = [100,113,127,98,75,88,102]

def high_scores(score):
  return score >= 100


print(list(filter(high_scores, scores)))

