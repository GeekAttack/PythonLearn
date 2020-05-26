def logic(inputs, input_length):
    x = 0
    for item in inputs:
        if "0" in str(item):
            x = 1

    if x==1:
        print("yes")
    else:
        print("no")




    # x = 0
    #
    # for item in inputs:
    #     if item == 0:
    #         x = 1
    #     while item != 0:
    #         print(item)
    #         if item % 10 == 0:
    #             x = 1
    #             break
    #         else:
    #             item = int(item/10)
    #
    # if x==1:
    #     print("yes")
    # else:
    #     print("no")



input_length = int(input())
inputs = []
for x in range(input_length):
    inputs.append(int(input()))

logic(inputs, input_length)