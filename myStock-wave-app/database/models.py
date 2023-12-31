from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Column, Boolean, Float, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class NASDAQStock(Base):
    __tablename__ = "nasdaq_stock"
    id: Mapped[int] = mapped_column(primary_key=True)
    ticker: Mapped[Optional[str]] = mapped_column(String(255))
    date: Mapped[Optional[str]] = mapped_column(String(255))
    open: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    high: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    low: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    close: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    adj_close: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    volume: Mapped[Optional[int]] = Column(Integer, default=0, nullable=True)
    # addresses: Mapped[List["Address"]] = relationship(
    #     back_populates="user", cascade="all, delete-orphan"
    # )

    def __repr__(self) -> str:
        return f"NASDAQStock(id={self.id!r}, ticker={str(self.ticker)!r}, date={self.date!r}, open={str(self.open)!r}, high={str(self.high)!r}, low={str(self.low)!r}, close={str(self.close)!r}, adj_close={str(self.adj_close)!r}, volume={str(self.volume)!r})"


class NASDAQStockMetadata(Base):
    __tablename__ = "nasdaq_stock_metadata"
    id: Mapped[int] = mapped_column(primary_key=True)
    is_nasdaq_traded: Mapped[Optional[str]] = mapped_column(String(255))
    symbol: Mapped[Optional[str]] = mapped_column(String(255))
    security_name: Mapped[Optional[str]] = mapped_column(String(255))
    is_listing_exchange: Mapped[Optional[str]] = mapped_column(String(255))
    market_category: Mapped[Optional[str]] = mapped_column(String(255))
    is_etf: Mapped[Optional[str]] = mapped_column(String(255))
    round_lot_size: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    is_used_for_testing: Mapped[Optional[str]] = mapped_column(String(255))
    financial_status: Mapped[Optional[str]] = mapped_column(String(255))
    cqs_symbol: Mapped[Optional[str]] = mapped_column(String(255))
    next_shares: Mapped[Optional[str]] = mapped_column(String(255))
    # addresses: Mapped[List["Address"]] = relationship(
    #     back_populates="user", cascade="all, delete-orphan"
    # )

    def __repr__(self) -> str:
        return f"NASDAQStockMetadata(id={self.id!r}, is_nasdaq_traded={self.is_nasdaq_traded!r}, symbol={str(self.symbol)!r}, security_name={str(self.security_name)!r}, is_listing_exchange={str(self.is_listing_exchange)!r}, market_category={str(self.market_category)!r}, is_etf={str(self.is_etf)!r}, round_lot_size={str(self.round_lot_size)!r}, is_used_for_testing={str(self.is_used_for_testing)!r}, financial_status={str(self.financial_status)!r}, cqs_symbol={str(self.cqs_symbol)!r})"

class MovingAverage100ToClosingPrices(Base):
    __tablename__ = "moving_average100_to_closing_prices"
    id: Mapped[int] = mapped_column(primary_key=True)
    ticker: Mapped[Optional[str]] = mapped_column(String(255))
    mavg: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    close: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)

    def __repr__(self) -> str:
        return f"MovingAverage100ToClosingPrices(id={self.id!r}, ticker={str(self.ticker)!r}, mavg={self.mavg!r}, close={str(self.close)!r})"


class OneHundredthDateClosingPricePredictions(Base):
    __tablename__ = "one_hundredth_date_closing_price_predictions"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[Optional[str]] = mapped_column(String(255))
    close: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    # addresses: Mapped[List["Address"]] = relationship(
    #     back_populates="user", cascade="all, delete-orphan"
    # )

    def __repr__(self) -> str:
        return f"OneHundredthDateClosingPricePredictions(id={self.id!r}, date={self.date!r}, close={str(self.close)!r})"

class Recommend(Base):
    __tablename__ = "recommend"
    id: Mapped[int] = mapped_column(primary_key=True)
    one_hundredth_date: Mapped[Optional[str]] = mapped_column(String(255))
    close: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    macd_diff_pytorch: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    macd_diff_transformers: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    decision_macd_diff_pytorch: Mapped[Optional[bool]] = Column(Boolean, default=False, nullable=True)
    decision_macd_diff_transformers: Mapped[Optional[bool]] = Column(Boolean, default=False, nullable=True)
    sma_twenty_pytorch: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    sma_twenty_transformers: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    sma_fifty_pytorch: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    sma_fifty_transformers: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    signal_pytorch: Mapped[Optional[bool]] = Column(Boolean, default=False, nullable=True)
    signal_transformers: Mapped[Optional[bool]] = Column(Boolean, default=False, nullable=True)
    decision_gc_pytorch: Mapped[Optional[bool]] = Column(Boolean, default=False, nullable=True)
    decision_gc_transformers: Mapped[Optional[bool]] = Column(Boolean, default=False, nullable=True)
    rsi_pytorch: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    rsi_transformers: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    sma_two_hundred_pytorch: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    sma_two_hundred_transformers: Mapped[Optional[float]] = Column(Float, default=0.0, nullable=True)
    decision_rsi_and_sma_pytorch: Mapped[Optional[bool]] = Column(Boolean, default=False, nullable=True)
    decision_rsi_and_sma_transformers: Mapped[Optional[bool]] = Column(Boolean, default=False, nullable=True)
    decision_final_status: Mapped[Optional[bool]] = Column(Boolean, default=False, nullable=True)
    nasdaq_stock_metadata_id: Mapped[int] = mapped_column(ForeignKey("nasdaq_stock_metadata.id"))
    # user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Recommend(id={self.id!r}, one_hundredth_date={self.one_hundredth_date!r}, close={str(self.close)!r})"