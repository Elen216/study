def multiply_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

def main():
    try:
        user_input = int(input("Введіть ціле число: "))
        
        while user_input > 9:
            user_input = multiply_digits(user_input)
            
        print(f"Результат: {user_input}")
        
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")

if __name__ == "__main__":
    main()
