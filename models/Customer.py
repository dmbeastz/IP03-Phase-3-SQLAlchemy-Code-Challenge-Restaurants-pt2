
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, desc
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

from models.Review import Review

engine = create_engine('sqlite:///Restaurants.db')

Base = declarative_base()

class Customer:
    __tablename__ = 'Customer'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    
    reviews = relationship("Review", back_populates="customer")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self, session):
        return max(self.reviews, key=lambda review: review.rating).restaurant

    def add_review(self, session, restaurant, rating):
        new_review = Review(customer=self, restaurant=restaurant, rating=rating)
        self.reviews.append(new_review)
        session.add(new_review)

    def delete_reviews(self, session, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
            self.reviews.remove(review)


