from sqlalchemy.orm import sessionmaker
from models import Customer, Review, Restaurant, create_session

def display_data(session):
    # Display information about Restaurants, Customers, and Reviews
    print("\nRestaurants:")
    for restaurant in session.query(Restaurant).all():
        print(f"ID: {restaurant.id}, Name: {restaurant.name}")

    print("\nCustomers:")
    for customer in session.query(Customer).all():
        print(f"ID: {customer.id}, Name: {customer.first_name} {customer.last_name}")

    print("\nReviews:")
    for review in session.query(Review).all():
        print(f"ID: {review.id}, Rating: {review.rating}, "
              f"Restaurant: {review.restaurant.name}, "
              f"Customer: {review.customer.first_name} {review.customer.last_name}")

if __name__ == '__main__':
    with create_session() as session:
        # Clear existing data (optional)
        session.query(Customer).delete()
        session.query(Review).delete()
        session.query(Restaurant).delete()

        # # Seed new data
        # seed_data(session)

        # Display information about the generated data
        display_data(session)

    print("Finished")
