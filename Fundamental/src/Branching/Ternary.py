# Python ternary operator

is_nice = True

# if statement
if(is_nice):
    state = "nice"
    print(state)
else:
    state = "not nice"
    print(state)

# Ternary
# ( conditional_if_true if condition else condition_if_false )
# (condition_if_false, condition_if_true)[condition]

state = "nice" if is_nice else "not_nice"
print(state)
nice = True
personality = ("mean", "nice")[nice]
print(personality)