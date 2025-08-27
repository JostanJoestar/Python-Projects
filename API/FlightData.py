from amadeus import Client, ResponseError
import json

amadeus = Client(
    client_id='ZQPrW0lvXtJblvU4wjKHdnS74qhQwKTb',
    client_secret='RAZc6d5CAAkmExC9'
)

try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='FRA',       # Abflug Frankfurt
        destinationLocationCode='LHR',  # Ziel London Heathrow
        departureDate='2025-09-11',     # Datum YYYY-MM-DD
        adults=1,                       # Anzahl Reisende
        max=10,                         # maximale Anzahl Ergebnisse
        nonStop='true'                     # nur Direktflüge
    )

    flights = response.data
    for flight in flights:
        price = flight['price']['total']
        airline = flight['itineraries'][0]['segments'][0]['carrierCode']
        departure = flight['itineraries'][0]['segments'][0]['departure']['at']
        arrival = flight['itineraries'][0]['segments'][0]['arrival']['at']
        print(f"Flug: {airline}, Preis: {price} EUR, Abflug: {departure}, Ankunft: {arrival}")
    
except ResponseError as error:
    print(error)
