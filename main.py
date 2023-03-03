import ttg

# prop_vars = [
#     'p', # its rainy outside
#     'q'  # i am inside

# ]




# # => is 'if then'
# # = is 'if and only if'
# # ~ is 'not'
# prop_expressions = [
#     'p and q', 
#     'p or q', 
#     '~p', 
#     '~q', 
#     'p => q',
#     'p = q'
# ]

# prop_vars = [
#     'P11', # Pit in L1,1
#     'P21',
#     'P22',
#     'P31',
#     'P34',
#     'P43',
#     'P32',
#     'P23',
#     'B11',
#     'B21',
#     'B33'
# ]
# prop_expressions = [
#     '~P11', #There is no pit in L1,1
#     'B11 = (P11 or P21)' #There is a breeze in L1,1 if and only if there is a pit in L11 or L21
#     'B21 = (P11 or P22 or P31)',
#     'B33 = (P34 or P43 or P32 or P23)'
#     ]

# print(ttg.Truths(prop_vars, prop_expressions).as_prettytable())

# perceptrons = [
#     '~B11',
#     'B21'
# ]
# prop_expressions = prop_expressions + perceptrons

prop_vars = [
    'outside',
    'inside',
    'rainy',
    '~outside',
    '~inside',
    'car',
    'gowalk',
    '~car',
    '~walk',
    'sweater'
    
]

prop_expressions = [
    'rainy => inside', # if rainy then inside
    'inside => ~outside',
    'outside => ~inside',
    'outside => (car or walk)',
    'car => ~walk',
    'walk => ~car',
    'gowalk => sweater'
]


print(ttg.Truths(prop_vars, prop_expressions).as_prettytable())


perceptrons = [
    '~raining'
    'walk'
]

prop_expressions = prop_expressions + perceptrons

print(ttg.Truths(prop_vars, prop_expressions).as_prettytable())