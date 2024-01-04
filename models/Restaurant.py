from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, desc
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

from models.Review import Review

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    reviews = relationship("Review", back_populates="restaurant")

    def all_reviews(self, session):
        reviews = session.query(Review).filter_by(restaurant_id=self.id).all()
        return [f"Review for {self.name} by {review.customer.full_name()}: {review.rating} stars." for review in reviews]

    def average_star_rating(self, session):
        ratings = [review.rating for review in self.reviews]
        return sum(ratings) / len(ratings) if ratings else 0

    @classmethod
    def fanciest(cls, session):
        return session.query(Restaurant).order_by(desc(Restaurant.price)).first()
