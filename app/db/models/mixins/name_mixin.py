from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class StrNameMixin:
    name: Mapped[str] = mapped_column(String(50), nullable=False)
