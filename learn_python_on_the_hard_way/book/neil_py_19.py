#coding: utf-8

"""
@Author: Well
@Date: 2013-03-12
"""

#习题32：循环和列表

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "this is count %d" % number

# same as above
for fruit in fruits:
    print "a fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "i got %s" % i

# we cam also build lists, first start with am empty one.
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "elements was: %d" %i