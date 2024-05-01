# Write a function that returns `True` if a dictionary is empty, and `False`
# otherwise.

# Write your function here.
def is_empty(i):
    return not i

print(is_empty({}))        #> True
print(is_empty({"a": 1}))  #> False