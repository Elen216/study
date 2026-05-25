def format_time(seconds):
    if not (0 <= seconds < 8640000):
        return "Введіть число від 0 до 8639999."
    days, remaining_seconds = divmod(seconds, 24 * 60 * 60)
    hours, remaining_seconds = divmod(remaining_seconds, 60 * 60)
    minutes, final_seconds = divmod(remaining_seconds, 60)
    if days == 1:
        day_word = "день"
    elif days in [2, 3, 4]:
        day_word = "дні"
    else:
        day_word = "днів"
    formatted_str = f"{days} {day_word} {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(final_seconds).zfill(2)}"

    return formatted_str

try:
    user_input = int(input("Введіть кількість секунд (від 0 до 8639999): "))
    print(format_time(user_input))
except ValueError:
    print("Будь ласка, введіть ціле число.")
