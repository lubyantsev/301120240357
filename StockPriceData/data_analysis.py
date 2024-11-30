def calculate_and_display_average_price(data):
    # Проверяем, содержит ли DataFrame данные о закрытии
    if 'Close' in data.columns:
        average_price = data['Close'].mean()
        print(f"Средняя цена закрытия за указанный период: {average_price:.2f}")
    else:
        print("Данные о закрытии отсутствуют.")
