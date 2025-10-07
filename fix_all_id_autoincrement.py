from sqlalchemy import create_engine, text

# 🔧 Ganti sesuai koneksi database kamu di Railway
DATABASE_URL = "postgresql://postgres:dtJcsbCvZDfhcOdMAWTwyzoQPmCubWIX@maglev.proxy.rlwy.net:25155/railway"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("🚀 Memperbaiki auto increment di semua tabel...\n")

    # Transactions
    conn.execute(text("CREATE SEQUENCE IF NOT EXISTS transactions_id_seq;"))
    conn.execute(text("ALTER TABLE transactions ALTER COLUMN id SET DEFAULT nextval('transactions_id_seq');"))
    conn.execute(text("ALTER SEQUENCE transactions_id_seq OWNED BY transactions.id;"))

    # Categories
    conn.execute(text("CREATE SEQUENCE IF NOT EXISTS categories_id_seq;"))
    conn.execute(text("ALTER TABLE categories ALTER COLUMN id SET DEFAULT nextval('categories_id_seq');"))
    conn.execute(text("ALTER SEQUENCE categories_id_seq OWNED BY categories.id;"))

    # Goals
    conn.execute(text("CREATE SEQUENCE IF NOT EXISTS goals_id_seq;"))
    conn.execute(text("ALTER TABLE goals ALTER COLUMN id SET DEFAULT nextval('goals_id_seq');"))
    conn.execute(text("ALTER SEQUENCE goals_id_seq OWNED BY goals.id;"))

    conn.commit()
    print("✅ Semua kolom 'id' sekarang sudah AUTO INCREMENT!")
