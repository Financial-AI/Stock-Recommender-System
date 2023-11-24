from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class NASDAQStock(Base):
    __tablename__ = "nasdaq_stock"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[Optional[str]] = mapped_column(String(255))
    open: Mapped[Optional[float]]
    high: Mapped[Optional[float]]
    low: Mapped[Optional[float]]
    close: Mapped[Optional[float]]
    adj_close: Mapped[Optional[float]]
    volume: Mapped[Optional[int]]
    # addresses: Mapped[List["Address"]] = relationship(
    #     back_populates="user", cascade="all, delete-orphan"
    # )

    def __repr__(self) -> str:
        return f"NASDAQStock(id={self.id!r}, date={self.date!r}, open={str(self.open)!r}, high={str(self.high)!r}, low={str(self.low)!r}, close={str(self.close)!r}, adj_close={str(self.adj_close)!r}, volume={str(self.volume)!r})"

class NASDAQStockMetadata(Base):
    __tablename__ = "nasdaq_stock_metadata"
    id: Mapped[int] = mapped_column(primary_key=True)
    is_nasdaq_traded: Mapped[Optional[str]] = mapped_column(String(255))
    symbol: Mapped[Optional[str]] = mapped_column(String(255))
    security_name: Mapped[Optional[str]] = mapped_column(String(255))
    is_listing_exchange: Mapped[Optional[str]] = mapped_column(String(255))
    market_category: Mapped[Optional[str]] = mapped_column(String(255))
    is_etf: Mapped[Optional[str]] = mapped_column(String(255))
    round_lot_size: Mapped[Optional[float]]
    is_used_for_testing: Mapped[Optional[str]] = mapped_column(String(255))
    financial_status: Mapped[Optional[str]] = mapped_column(String(255))
    cqs_symbol: Mapped[Optional[str]] = mapped_column(String(255))
    # addresses: Mapped[List["Address"]] = relationship(
    #     back_populates="user", cascade="all, delete-orphan"
    # )

    def __repr__(self) -> str:
        return f"NASDAQStockMetadata(id={self.id!r}, is_nasdaq_traded={self.is_nasdaq_traded!r}, symbol={str(self.symbol)!r}, security_name={str(self.security_name)!r}, is_listing_exchange={str(self.is_listing_exchange)!r}, market_category={str(self.market_category)!r}, is_etf={str(self.is_etf)!r}, round_lot_size={str(self.round_lot_size)!r}, is_used_for_testing={str(self.is_used_for_testing)!r}, financial_status={str(self.financial_status)!r}, cqs_symbol={str(self.cqs_symbol)!r})"

class OneHundredthDateClosingPricePredictions(Base):
    __tablename__ = "one_hundredth_date_closing_price_predictions"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[Optional[str]] = mapped_column(String(255))
    close: Mapped[Optional[float]]
    # addresses: Mapped[List["Address"]] = relationship(
    #     back_populates="user", cascade="all, delete-orphan"
    # )

    def __repr__(self) -> str:
        return f"OneHundredthDateClosingPricePredictions(id={self.id!r}, date={self.date!r}, close={str(self.close)!r})"

class Recommend(Base):
    __tablename__ = "recommend"
    id: Mapped[int] = mapped_column(primary_key=True)
    one_hundredth_date: Mapped[Optional[str]] = mapped_column(String(255))
    close: Mapped[Optional[float]]
    macd_diff: Mapped[Optional[float]]
    decision_macd_diff: Mapped[Optional[bool]]
    sma_twenty: Mapped[Optional[float]]
    sma_fifty: Mapped[Optional[float]]
    signal: Mapped[Optional[bool]]
    decision_gc: Mapped[Optional[bool]]
    rsi: Mapped[Optional[float]]
    sma_two_hundred: Mapped[Optional[float]]
    decision_rsi_and_sma: Mapped[Optional[bool]]
    decision_final_status: Mapped[Optional[bool]]
    # user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    # user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Recommend(id={self.id!r}, date={self.one_hundredth_date!r}, close={str(self.close)!r}, macd_diff={str(self.macd_diff)!r}, decision_macd_diff={str(self.decision_macd_diff)!r}, sma_twenty={str(self.sma_twenty)!r}, sma_fifty={str(self.sma_fifty)!r}, signal={str(self.signal)!r}, decision_gc={str(self.decision_gc)!r}, rsi={str(self.rsi)!r}, sma_two_hundred={str(self.sma_two_hundred)!r}, decision_rsi_and_sma={str(self.decision_rsi_and_sma)!r}, decision_final_status={str(self.decision_final_status)!r})"
    