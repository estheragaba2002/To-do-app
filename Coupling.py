# child_input = input("Enter the feet and inches of the child")
#
# def calculate(child_input):
#     parts = child_input.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#
#     meters = feet * 0.3048 + inches * 0.0254
#     return (f"{feet} feet {inches} inches and {meters} meters")
#
# print(calculate(child_input))
user_input = "Type 'show', 'add','edit' or 'exit'"
user_input = user_input.split()
print(user_input)