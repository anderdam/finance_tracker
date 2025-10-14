from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TransactionCreate(BaseModel):
    account_id: UUID
    category_id: UUID
    occurred_at: datetime
    amount: float
    currency: str = "BRL"
    type: str
    notes: Optional[str] = None


class TransactionRead(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
