from app.core.config import get_settings
from app.utils.postgres import PostgresUtils  # You’ll need to implement this


def main() -> None:
    settings = get_settings()

    db = PostgresUtils(
        host=settings.postgres_host,
        port=settings.postgres_port,
        user=settings.postgres_user,
        password=settings.postgres_password,
        database=settings.postgres_db,
        schema="finance_tracker",  # or settings.schema if you add it
    )

    print("🔐 Testing database connection...")
    db.test_connection()

    print("🏗️ Ensuring schema exists...")
    db.create_schema_if_not_exists()

    print("📋 Listing schemas and tables...")
    schemas = db.list_schemas()
    tables = db.list_tables()

    print("Available schemas:", schemas)
    print(f"Tables in schema '{db.schema}':", tables)


if __name__ == "__main__":
    main()
