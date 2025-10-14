📦 CHANGELOG.md
[v1.1.0] — 2025-10-13
🛠️ Improved Type Safety and mypy Compliance
- Annotated all SQLAlchemy ORM models using Mapped[...] and mapped_column(...).
- Replaced ambiguous dict annotations with dict[str, object].
- Renamed metadata field in Account to extra_data to avoid conflict with SQLAlchemy internals.
- Removed unnecessary TYPE_CHECKING block from orm_models.py.
🧠 Dependency Injection Fixes
- Corrected return type for get_db() using Generator[SessionType, None, None].
- Imported Session type from sqlalchemy.orm to resolve valid-type error.
🧹 CRUD Layer Refactor
- Replaced incorrect Transaction import from sqlalchemy with model alias TransactionModel.
- Annotated all CRUD functions with precise return types:
- create_transaction: returns inserted TransactionModel instance.
- get_transaction: returns TransactionModel | None.
- list_transactions: returns Sequence[TransactionModel].
- update_transaction: returns Row[...] | None.
- delete_transaction: returns TransactionModel | None, unpacked from Row[...].

[v1.0.0] — Initial Release
🎉 Project Setup
- Defined SQLAlchemy models: User, Account, Category, Transaction, Setting.
- Established database session handling via get_db() generator.
- Implemented basic CRUD operations for Transaction.

## v0.2.0 (2025-10-13)

### Feat

- **initial-commit-with-structure,-classes-and-models**: added classes, models, crud and some other implementations
