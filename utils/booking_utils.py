def build_booking_link(hotel_name, city):
    query = f"{hotel_name} {city}".replace(" ", "+")
    return f"https://www.google.com/travel/hotels?q={query}"
