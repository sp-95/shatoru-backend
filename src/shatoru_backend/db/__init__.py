# Import all the models, so that Base has them before being
# imported by Alembic
from shatoru_backend.db.base import Base

__all__ = ["Base"]
