# The function is expected to return a string
# The function accepts an integer array(list of input) and an integer(length of input) as parameters.

def logic(inputs, input_length):
    # Write your code here and remove pass statement
    # You can create other functions and call from here
    # Don't print anything. Just return the intended output

    # for item in inputs:
    #     check = []
    #     if item == 0:
    #         check.append("t")
    #         return "yes"
    #
    #     else:
    #         while item > 0:
    #             if item % 10 == 0:
    #                 check.append("t")
    #                 return "Yes"
    #             else:
    #                 item = item / 10
    #
    # if "t" not in check:
    #     return "No"


# Do not edit below

# Get the input
input_length = int(input())
inputs = []
for x in range(input_length):
    inputs.append(int(input()))

# Print output returned from the logic function
print(logic(inputs, input_length))
