from sqlalchemy.orm import Session
from src.main.api.db.models.transaction_table import Transaction


class TransactionCrudDb:
    @staticmethod
    def get_transaction_by_id(db: Session, transaction_id: int) -> Transaction | None:
        return db.query(Transaction).filter_by(id=transaction_id).first()

    @staticmethod
    def get_last_transaction_by_account(db: Session, account_id: int, transaction_type: str) -> Transaction | None:
        """Получить последнюю транзакцию по счету (как отправитель или получатель)"""
        query = db.query(Transaction).filter(
            (Transaction.from_account_id == account_id) |
            (Transaction.to_account_id == account_id)
        )

        if transaction_type:
            query = query.filter(Transaction.transaction_type == transaction_type)

        return query.order_by(Transaction.created_at.desc()).first()