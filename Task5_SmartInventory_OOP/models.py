"""
Datheon Python Programming Internship - Task 5
OOPs Architecture: Enterprise Smart Inventory & Asset System (Models)

Demonstrates:
- Abstract Base Classes (abc.ABC, @abstractmethod)
- Encapsulation with private attributes (__attr) and property decorators (@property, @setter)
- Inheritance & Polymorphism (Item -> Book, Magazine, DigitalMedia)
- Python Dunder / Magic Methods (__str__, __repr__, __len__, __eq__)
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Item(ABC):
    """
    Abstract Base Class representing a generic trackable inventory asset.
    Demonstrates Abstraction and strict Encapsulation.
    """

    def __init__(self, item_id: str, title: str, price: float):
        if not item_id or not str(item_id).strip():
            raise ValueError("Item ID cannot be empty.")
        if not title or not str(title).strip():
            raise ValueError("Title cannot be empty.")
        if price < 0.0:
            raise ValueError("Item price cannot be negative.")

        self.__item_id = str(item_id).strip()
        self.__title = str(title).strip()
        self.__price = float(price)
        self.__is_checked_out = False
        self.__borrower = None
        self.__checkout_date = None

    # --- Property Getters and Setters (Encapsulation) ---

    @property
    def item_id(self) -> str:
        return self.__item_id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title: str):
        if not new_title or not str(new_title).strip():
            raise ValueError("Title cannot be empty.")
        self.__title = str(new_title).strip()

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price < 0.0:
            raise ValueError("Price cannot be negative.")
        self.__price = float(new_price)

    @property
    def is_checked_out(self) -> bool:
        return self.__is_checked_out

    @property
    def borrower(self) -> str:
        return self.__borrower

    # --- Asset State Transitions ---

    def check_out(self, borrower_name: str):
        """Checks out the asset to a borrower."""
        if self.__is_checked_out:
            raise RuntimeError(f"Item '{self.__title}' is already checked out to {self.__borrower}.")
        if not borrower_name or not str(borrower_name).strip():
            raise ValueError("Borrower name cannot be empty.")
        self.__is_checked_out = True
        self.__borrower = str(borrower_name).strip()
        self.__checkout_date = datetime.now()

    def return_item(self):
        """Returns the asset back to available inventory."""
        if not self.__is_checked_out:
            raise RuntimeError(f"Item '{self.__title}' is not currently checked out.")
        self.__is_checked_out = False
        self.__borrower = None
        self.__checkout_date = None

    # --- Abstract Methods (Polymorphism & Abstraction) ---

    @abstractmethod
    def calculate_late_fee(self, days_overdue: int) -> float:
        """Computes daily overdue penalty fees specific to item asset category."""
        pass

    @abstractmethod
    def get_item_type(self) -> str:
        """Returns the specific classification of the inventory item."""
        pass

    # --- Dunder / Magic Methods ---

    def __str__(self) -> str:
        status = f"Checked out to {self.__borrower}" if self.__is_checked_out else "Available"
        return f"[{self.get_item_type()}] #{self.__item_id}: '{self.__title}' (${self.__price:.2f}) - {status}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(item_id='{self.__item_id}', title='{self.__title}', price={self.__price})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Item):
            return self.__item_id == other.item_id
        return False


class Book(Item):
    """Concrete subclass representing a physical book."""

    def __init__(self, item_id: str, title: str, price: float, author: str, pages: int):
        super().__init__(item_id, title, price)
        if not author:
            raise ValueError("Author cannot be empty.")
        if pages <= 0:
            raise ValueError("Pages must be greater than zero.")
        self.__author = author.strip()
        self.__pages = int(pages)

    @property
    def author(self) -> str:
        return self.__author

    @property
    def pages(self) -> int:
        return self.__pages

    def calculate_late_fee(self, days_overdue: int) -> float:
        return max(0, days_overdue) * 1.00  # $1.00 per overdue day for books

    def get_item_type(self) -> str:
        return "Book"

    def __len__(self) -> int:
        """Dunder method returning total page count."""
        return self.__pages


class Magazine(Item):
    """Concrete subclass representing a periodical publication."""

    def __init__(self, item_id: str, title: str, price: float, issue_number: int, publisher: str):
        super().__init__(item_id, title, price)
        if issue_number <= 0:
            raise ValueError("Issue number must be positive.")
        self.__issue_number = int(issue_number)
        self.__publisher = (publisher or "Independent").strip()

    @property
    def issue_number(self) -> int:
        return self.__issue_number

    @property
    def publisher(self) -> str:
        return self.__publisher

    def calculate_late_fee(self, days_overdue: int) -> float:
        return max(0, days_overdue) * 0.50  # $0.50 per overdue day for magazines

    def get_item_type(self) -> str:
        return "Magazine"

    def __len__(self) -> int:
        """Dunder method returning the issue number."""
        return self.__issue_number


class DigitalMedia(Item):
    """Concrete subclass representing digital licenses, audiobooks, or software."""

    def __init__(self, item_id: str, title: str, price: float, format_type: str, file_size_mb: float):
        super().__init__(item_id, title, price)
        self.__format_type = (format_type or "MP4").strip().upper()
        self.__file_size_mb = max(1.0, float(file_size_mb))

    @property
    def format_type(self) -> str:
        return self.__format_type

    @property
    def file_size_mb(self) -> float:
        return self.__file_size_mb

    def calculate_late_fee(self, days_overdue: int) -> float:
        return max(0, days_overdue) * 2.00  # $2.00 per overdue day for digital licenses

    def get_item_type(self) -> str:
        return f"Digital Media ({self.__format_type})"

    def __len__(self) -> int:
        """Dunder method returning integer file size in megabytes."""
        return int(self.__file_size_mb)
