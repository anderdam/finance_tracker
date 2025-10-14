# main.py


def main() -> None:
    # # 🔐 Load credentials from environment
    # db = PostgresUtils(
    #     host=os.getenv("POSTGRES_HOST", "localhost"),
    #     port=os.getenv("POSTGRES_PORT", "5432"),
    #     user=os.getenv("POSTGRES_USER"),
    #     password=os.getenv("POSTGRES_PASSWORD"),
    #     database=os.getenv("POSTGRES_DB"),
    #     schema=os.getenv("POSTGRES_SCHEMA", "finance_tracker"),
    # )
    #
    # # 🧪 Test connection
    # db.test_connection()
    #
    # # 🏗️ Ensure schema exists
    # db.create_schema_if_not_exists()
    #
    # # 📋 List schemas and tables
    # schemas = db.list_schemas()
    # tables = db.list_tables()
    #
    # print("Available schemas:", schemas)
    # print(f"Tables in schema '{db.schema}':", tables)

    raise NotImplementedError


if __name__ == "__main__":
    main()
