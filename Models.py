from abc import ABC, abstractmethod
from aiogram import Router, types
from aiogram.filters import Command
import asyncio

router = Router()

class Pizza(ABC):
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price
        self._dough = ""
        self._sauce = ""
        self._toppings = []

    @abstractmethod
    def prepare(self) -> str:
        pass

    @property
    def name(self) -> str:
        return self.name

    @property
    def price(self) -> float:
        return self.price

    @property
    def dough(self) -> str:
        return self._dough

    @property
    def sauce(self) -> str:
        return self._sauce

    @property
    def toppings(self) -> list:
        return self._toppings

    def get_info(self) -> dict:
        return {
            'name': self.name,
            'price': self.price,
            'dough': self.dough,
            'sauce': self.sauce,
            'toppings': self.toppings
        }

    def __str__(self) -> str:
        return f"{self.name} - {self.price} UZS"

class Papperoni(Pizza):
    def __init__(self):
        super().__init__("Papperoni", 45.000)
        self._dough = "Thin Crust"
        self._sauce = "Tomato Sauce"
        self._toppings = ["Papperoni sausage", "Mozzarella cheese", "Oregano"]

    def prepare(self) -> str:
        return (
            f"🍕 {self._name} Preparing... \n"
            f"Crust: {self._dough} \n"
            f"Sauce: {self._sauce} \n"
            f"Toppings: {', '.join(self._toppings)} \n"
            f"✅ Ready!"
        )

    class Barbecue(Pizza):
        def __init__(self):
            super().__init__("Barbecue", 50.000)
            self._dough = "Thick Crust"
            self._sauce = "Barbecue Sauce"
            self._toppings = ["Chicken", "Onion", "Cheddar cheese", "Tomato"]

        def prepare(self) -> str:
            return (
                f"🍕 {self._name} Preparing... \n"
                f"Crust: {self._dough} \n"
                f"Sauce: {self._sauce} \n"
                f"Toppings: {', '.join(self._toppings)} \n"
                f"✅ Ready!"
            )

    class SeaDelights(Pizza):
        def __init__(self):
            super().__init__("Sea Delights", 70.000)
            self._dough = "Thin Crust"
            self._sauce = "White Sauce (Alfredo)"
            self._toppings = ["Crab", "Shrimp", "Mussels", "Mozzarella", "Olive"]

        def prepare(self) -> str:
            return (
                f"🍕 {self._name} Preparing... \n"
                f"Crust: {self._dough} \n"
                f"Sauce: {self._sauce} \n"
                f"Toppings: {', '.join(self._toppings)} \n"
                f"✅ Ready!"
            )

    class Alfredo(Pizza):
        def __init__(self):
            super().__init__("Alfredo", 50.000)
            self._dough = "Medium Thick Crust"
            self._sauce = "Creamy Alfredo Sauce"
            self._toppings = ["Chicken fillet", "Mushrooms", "Parmesan cheese", "Olive"]

        def prepare(self) -> str:
            return (
                f"🍕 {self._name} Preparing... \n"
                f"Crust: {self._dough} \n"
                f"Sauce: {self._sauce} \n"
                f"Toppings: {', '.join(self._toppings)} \n"
                f"✅ Ready!"
            )

    class PizzaFactory:
        @staticmethod
        def create_pizza(pizza_type: str) -> Pizza:
            pizzas = {
                'papperoni': "Papperoni",
                'barbecue': "Barbecue",
                'sea_delights': "SeaDelights",
                'alfredo': "Alfredo"
            }

            pizza_class = pizzas.get(pizza_type.lower())
            if pizza_class:
                return pizza_class()
            raise ValueError(f"Unknown pizza type: {pizza_type}")

        @staticmethod
        def get_all_pizzas() -> list:
            return ["Papperoni(), Barbecue(), SeaDelights(), Alfredo()"]

    class Order:
        def __init__(self, user_id: int, username: str = None):
            self._user_id = user_id
            self._username = username
            self._items = []
            self._status = "active"

        @property
        def user_id(self) -> int:
            return self._user_id

        @property
        def items(self) -> list:
            return self._items.copy()

        @property
        def status(self) -> str:
            return self._status

        def add_pizza(self, pizza: Pizza):
            if not isinstance(pizza, Pizza):
                raise TypeError("Only Pizza Ingredients Can Be Added")
            self._items.append(pizza)

        def calculate_total(self) -> float:
            return sum(pizza.price for pizza in self._items)

        def get_item_count(self) -> int:
            return len(self._items)

        def is_empty(self) -> bool:
            return len(self._items) == 0

        def clear(self) -> None:
            self._items.clear()
            self._status = "active"

        def confirm(self) -> None:
            if self.is_empty():
                raise ValueError("An Empty Order Cannot Be Confirmed")
            self._status = "Confirmed"

        def get_order_summary(self) -> str:
            if self.is_empty():
                return "📦 The Order is Empty"

            summary = "📦 Your Order: \n"
            for i, pizza in enumerate(self._items, 1):
                summary += f"{i}. {pizza.name} - {pizza.price:,.0f} UZS\n"

            summary += f"\n 💰 Total: {self.calculate_total():,.0f} UZS"
            return summary

        def to_dict(self) -> dict:
            return {
                'user_id': self._user_id,
                'username': self._username,
                'items': [
                    {'name': pizza.name, 'price': pizza.price}
                    for pizza in self._items
                ],
                'total_price': self.calculate_total(),
                'status': self._status,
            }

@router.message(Command("mortgage"))
async def mortgage(message: types.Message):
    for property in property:
        await message.answer_photo(
            photo=property["photo"],
            caption=property["caption"],
            reply_markup=property["keyboard"]()
        )
        await asyncio.sleep(0.3)

        def __str__(self) -> str:
            return f"Order(user={self._user_id}), items={len(self._items)}, total={self.calculate_total()})"