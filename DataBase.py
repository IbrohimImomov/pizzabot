import  sqlite3
import logging


logger = logging.getLogger("FornoPizza")

class DataBase:
    def __init__(self, db_name: str):
        self.db_name = db_name

    async def create_tables(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            total_price REAL,
            status TEXT,
             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
             FOREIGN KEY (user_id) REFERENCES orders (id)
            )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        pizza_name TEXT,
        pizza_price REAL,
        FOREIGN KEY (order_id) REFERENCES orders (id)
            )
        """)

        conn.commit()
        conn.close()
        logger.info(f"DataBase created successfully")

    def add_user(self, user_id: int, username: str = None, first_name: str = None, last_name: str = None):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT OR IGNORE INTO users (user_id, username, first,name, last_name) VALUES (?, ?, ?, ?, ?) ",
            (user_id, username, first_name, last_name)
        )

        conn.commit()
        conn.close()

    def save_order(self, user_id: int, order_data: dict) -> int:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO orders (user_id, total_price, status) VALUES (?, ?, ?)",
            (user_id, order_data['total_price'], order_data['status'])
        )
        order_id = cursor.lastrowid

        for item in order_data['items']:
            cursor.execute(
                "INSERT INTO order_items (order_id, pizza_name, pizza_price) VALUES (?, ?, ?)",
                (order_id, item['name'], item['price'])
            )

        conn.commit()
        conn.close()

        logger.info(f"Order #{order_id} saved successfully (User: {user_id})")
        return order_id

    def get_user_orders(self, user_id: int) -> list:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC",
            (user_id,)
        )

        orders = cursor.fetchall()
        conn.close()

        return orders