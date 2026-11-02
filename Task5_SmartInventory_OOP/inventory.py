"""
Datheon Python Programming Internship - Task 5
OOPs Architecture: Enterprise Smart Inventory & Asset System (Driver)

Demonstrates:
- Full Polymorphism: Calling common methods (calculate_late_fee, get_item_type) across Book, Magazine, and DigitalMedia
- Inventory valuation and asset status tracking
- Formatted tabular reporting
"""

from models import Item, Book, Magazine, DigitalMedia


class InventoryManager:
    """Manages collection of asset items demonstrating composition and polymorphism."""

    def __init__(self):
        self.catalog = {}  # item_id -> Item
        self.seed_initial_inventory()

    def seed_initial_inventory(self):
        """Pre-loads diverse asset types demonstrating OOP inheritance."""
        b1 = Book("BK-101", "Clean Code in Python", 45.00, "Mariano Anaya", 412)
        b2 = Book("BK-102", "Designing Data-Intensive Apps", 55.00, "Martin Kleppmann", 616)
        m1 = Magazine("MG-201", "IEEE Software Trends", 18.50, 48, "IEEE Computer Society")
        d1 = DigitalMedia("DM-301", "Machine Learning Masterclass Video", 89.99, "MP4", 4500.0)

        for item in (b1, b2, m1, d1):
            self.add_item(item)

    def add_item(self, item: Item):
        if not isinstance(item, Item):
            raise TypeError("Item must be an instance derived from Item base class.")
        if item.item_id in self.catalog:
            raise ValueError(f"Asset ID '{item.item_id}' already exists in inventory.")
        self.catalog[item.item_id] = item

    def get_item(self, item_id: str) -> Item:
        return self.catalog.get(item_id)

    def checkout_item(self, item_id: str, borrower: str):
        item = self.get_item(item_id)
        if not item:
            raise KeyError(f"Asset ID '{item_id}' not found.")
        item.check_out(borrower)
        print(f"[Success] {item.get_item_type()} '{item.title}' checked out to {borrower}.")

    def return_item(self, item_id: str, days_overdue: int = 0):
        item = self.get_item(item_id)
        if not item:
            raise KeyError(f"Asset ID '{item_id}' not found.")

        # Polymorphic late fee calculation
        late_fee = item.calculate_late_fee(days_overdue)
        item.return_item()

        print(f"\n[Asset Returned] '{item.title}' (#{item.item_id})")
        if days_overdue > 0:
            print(f"  Overdue Days : {days_overdue} days")
            print(f"  Late Penalty : ${late_fee:.2f} (Calculated via {item.get_item_type()} policy)")
        else:
            print("  Status       : Returned on time with zero penalty.")

    def total_valuation(self) -> float:
        return sum(item.price for item in self.catalog.values())

    def print_audit_report(self):
        if not self.catalog:
            print("\n[Info] Inventory catalog is empty.")
            return

        print("\n" + "=" * 105)
        print("                         ENTERPRISE SMART ASSET INVENTORY REPORT                          ")
        print("=" * 105)
        header = f"| {'ID':<8} | {'Type':<18} | {'Title':<28} | {'Value ($)':>10} | {'Metric (len)':>12} | {'Status':<15} |"
        print(header)
        print("-" * 105)

        for item in self.catalog.values():
            status = f"Borrowed ({item.borrower})" if item.is_checked_out else "AVAILABLE"
            # Using dunder method __len__ polymorphism
            metric = f"{len(item)} units"
            if isinstance(item, Book):
                metric = f"{len(item)} pages"
            elif isinstance(item, Magazine):
                metric = f"Issue #{len(item)}"
            elif isinstance(item, DigitalMedia):
                metric = f"{len(item)} MB"

            row = f"| {item.item_id:<8} | {item.get_item_type():<18} | {item.title[:28]:<28} | ${item.price:>9.2f} | {metric:>12} | {status:<15} |"
            print(row)

        print("-" * 105)
        print(f" TOTAL ASSETS REGISTERED : {len(self.catalog)}")
        print(f" TOTAL INVENTORY VALUE   : ${self.total_valuation():.2f}")
        print("=" * 105)


def run_cli():
    manager = InventoryManager()
    print("=================================================================")
    print("     DATHEON - ENTERPRISE SMART ASSET MANAGEMENT (OOP)           ")
    print("=================================================================")

    while True:
        print("\n-------------------- INVENTORY MENU --------------------")
        print("1. View Full Asset Inventory Audit Report")
        print("2. Borrow / Check Out an Asset")
        print("3. Return an Asset & Assess Late Fees (Polymorphism)")
        print("4. Add New Asset to Inventory (Book, Magazine, Media)")
        print("5. Test Dunder Methods (__repr__, __len__, __eq__)")
        print("6. Exit")
        print("--------------------------------------------------------")

        try:
            choice = input("Select an option (1-6): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting system.")
            break

        if choice == "1":
            manager.print_audit_report()
        elif choice == "2":
            item_id = input("Enter Asset ID to borrow (e.g. BK-101): ").strip()
            borrower = input("Enter Borrower Name: ").strip()
            try:
                manager.checkout_item(item_id, borrower)
            except Exception as e:
                print(f"[Error] {e}")
        elif choice == "3":
            item_id = input("Enter Asset ID to return (e.g. BK-101): ").strip()
            try:
                days = int(input("Enter Days Overdue (0 for on-time): ").strip())
                manager.return_item(item_id, days)
            except ValueError:
                print("[Error] Days must be an integer.")
            except Exception as e:
                print(f"[Error] {e}")
        elif choice == "4":
            print("\nSelect Asset Type to Add:")
            print("1. Book")
            print("2. Magazine")
            print("3. Digital Media")
            t_choice = input("Choice (1-3): ").strip()
            try:
                item_id = input("Enter Asset ID: ").strip()
                title = input("Enter Title: ").strip()
                price = float(input("Enter Price ($): ").strip())

                if t_choice == "1":
                    author = input("Enter Author: ").strip()
                    pages = int(input("Enter Page Count: ").strip())
                    new_item = Book(item_id, title, price, author, pages)
                elif t_choice == "2":
                    issue = int(input("Enter Issue Number: ").strip())
                    pub = input("Enter Publisher: ").strip()
                    new_item = Magazine(item_id, title, price, issue, pub)
                elif t_choice == "3":
                    fmt = input("Enter Format (PDF/MP4/EPUB): ").strip()
                    mb = float(input("Enter File Size in MB: ").strip())
                    new_item = DigitalMedia(item_id, title, price, fmt, mb)
                else:
                    print("[Error] Invalid selection.")
                    continue

                manager.add_item(new_item)
                print(f"[Success] {new_item.get_item_type()} '{new_item.title}' added to inventory!")
            except Exception as e:
                print(f"[Validation Error] {e}")
        elif choice == "5":
            print("\n--- DUNDER / MAGIC METHODS DEMONSTRATION ---")
            sample_book = manager.get_item("BK-101")
            sample_mag = manager.get_item("MG-201")
            print(f"1. __str__()   : {str(sample_book)}")
            print(f"2. __repr__()  : {repr(sample_book)}")
            print(f"3. __len__()   : Book len = {len(sample_book)} pages, Magazine len = {len(sample_mag)} issue number")
            print(f"4. __eq__()    : (BK-101 == BK-101) -> {sample_book == sample_book}, (BK-101 == MG-201) -> {sample_book == sample_mag}")
        elif choice == "6":
            print("\nExiting Asset System. Happy Coding with Datheon!")
            break
        else:
            print("[Error] Invalid choice. Choose 1 to 6.")


if __name__ == "__main__":
    run_cli()
