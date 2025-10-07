from flask import Flask
from config.database import engine, Base
from routes.web import web
import models.transaction_model, models.category_model, models.goal_model

app = Flask(__name__)

# Buat tabel kalau belum ada
Base.metadata.create_all(bind=engine)

# Daftarkan route utama
app.register_blueprint(web)

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    print("=" * 50)
    print("🚀  UangKu API sedang berjalan!")
    print(f"📡  Akses di: http://127.0.0.1:{port} atau http://localhost:{port}")
    print("=" * 50)
    app.run(debug=True, host=host, port=port)
