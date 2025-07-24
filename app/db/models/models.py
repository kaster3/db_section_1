from datetime import date

from sqlalchemy import String, ForeignKey, Numeric, Text, Date
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base
from .mixins.pk_id_mixin import IntIdPkMixin
from .mixins.name_mixin import StrNameMixin



class Genre(IntIdPkMixin, StrNameMixin, Base):
    # Связи
    books = relationship("Book", back_populates="genre")


class Author(IntIdPkMixin, StrNameMixin, Base):
    # Связи
    books = relationship("Book", back_populates="author")


class City(IntIdPkMixin, StrNameMixin, Base):
    days_delivery: Mapped[int] = mapped_column(nullable=False)
    # Связи
    clients = relationship("Client", back_populates="city")


class Book(IntIdPkMixin, StrNameMixin, Base):
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), nullable=False)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id"), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)
    # Связи
    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")
    buy_books = relationship("BuyBook", back_populates="book")


class Client(IntIdPkMixin, StrNameMixin, Base):
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
    email: Mapped[str] = mapped_column(String(100)) # можно добавить валидацию или тип из доп библиотеки
    # Связи
    city = relationship("City", back_populates="clients")
    buys = relationship("Buy", back_populates="client")


class Buy(IntIdPkMixin, Base):
    buy_description: Mapped[str] = mapped_column(Text())
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    # Связи
    client = relationship("Client", back_populates="buys")
    buy_books = relationship("BuyBook", back_populates="buy")
    buy_steps = relationship("BuyStep", back_populates="buy")


class Step(IntIdPkMixin, StrNameMixin, Base):
    # Связи
    buy_steps = relationship("BuyStep", back_populates="step")


class BuyBook(IntIdPkMixin, Base):
    buy_id: Mapped[int] = mapped_column(ForeignKey("buys.id"), nullable=False)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)
    # Связи
    buy = relationship("Buy", back_populates="buy_books")
    book = relationship("Book", back_populates="buy_books")


class BuyStep(IntIdPkMixin, Base):
    buy_id: Mapped[int] = mapped_column(ForeignKey("buys.id"), nullable=False)
    step_id: Mapped[int] = mapped_column(ForeignKey("steps.id"), nullable=False)
    date_step_beg: Mapped[date] = mapped_column(Date, nullable=False)
    date_step_end: Mapped[date] = mapped_column(Date, nullable=False)
    # Связи
    buy = relationship("Buy", back_populates="buy_steps")
    step = relationship("Step", back_populates="buy_steps")