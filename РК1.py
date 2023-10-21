# Task1

# def cal_taxlevel(lary):
#     return lary * 0.2

# try:
#     name = input("Enter your name please:")
#     lary_input = input("Enter your desired salary level: ")
    
#     salary = int(lary_input)
#     tax_level = cal_taxlevel(lary)
#     print(f"{name}, the tax level you will pay with the salary {lary} is {tax_level:.0f}")
# except ValueError:
#     print(f"{name}, please enter your desired salary as a digit.")

# В этом коде блок try  преобразовать входную_зарплату в целое число, и 
# если это удается, он вычисляет уровень налога и печатает результат. Если преобразование в целое число вызывает 
# ошибку ValueError, она будет перехвачена в блоке исключений и отобразится сообщение об ошибке, предлагающее пользователю 
# ввести желаемую зарплату в виде цифры.



# Task2
# addition = lambda x, y: x + y
# multiplication = lambda x, y: x * y
# division = lambda x, y: x / y
# exponentiation = lambda x, y: x ** y

# operations = {
#     1: addition,
#     2: multiplication,
#     3: division,
#     4: exponentiation
# }

# while True:
#     try:
      
#         print("Please choose the task you want to perform:")
#         print("1. Addition")
#         print("2. Multiplication")
#         print("3. Division")
#         print("4. Exponentiation")
        
    
#         choice = int(input("user input:"))
#         if choice not in operations:
#             print("Invalid choice")
#             continue

       
#         input_str = input(f"Please enter two numbers for the operation : ")
#         x, y = map(float, input_str.split(","))

#         result = operations [choice](x, y)
#         print("Code Output:")
#         print(result)
#     except ValueError:
#         print("Invalid input. Please enter valid numbers.")
#     except Exception as e:
#         print(f"An error occurred: ")
    
    # Этот код позволяет пользователю выбрать операцию, введя соответствующий номер, а затем ввести два числа 
    # для выбранной операции. Затем он выполняет расчет с использованием лямбда-функций и отображает результат.


# Task 3

# def main():
#     unique_items = set()
#     non_unique_items = {}

#     while True:
#         try:
#             choice = int(input("Please choose the task you want to perform (1 for entering items, 2 to exit): "))

#             if choice == 1:
#                 items_input = input("Please enter items separated by a comma: ")
#                 items = [item.strip() for item in items_input.split(',')]

#                 for item in items:
#                     non_unique_items[item] = non_unique_items.get(item, 0) + 1
#                 unique_items.update(set(items))

#                 print("Items are saved")
#             elif choice == 2:
#                 break
#             else:
#                 print("Invalid choice. Please choose again.")
#         except ValueError:
#             print("Invalid input. Please enter a valid choice (1 or 2).")

#     print("Unique items:", unique_items)
#     print("Not unique items:", tuple((item, count) for item, count in non_unique_items.items()))

# if __name__ == "__main__":
#     main()
