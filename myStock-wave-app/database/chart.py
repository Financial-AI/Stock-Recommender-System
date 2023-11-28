from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from .models import Recommend, NASDAQStockMetadata, MovingAverage100ToClosingPrices

def get_close_chart(sqlEngine, n: int = 5) -> dict[any]:
    # Create a session
    Session = sessionmaker(bind=sqlEngine)
    session = Session()

    top_recommendations = session.query(Recommend).filter(Recommend.signal_transformers == 1 and Recommend.signal_pytorch == 1).group_by(Recommend.nasdaq_stock_metadata_id, Recommend.id).order_by(func.count().desc()).all()

    ticker_with_close_pred_over_time = {}
    recommendation_metadata_id = top_recommendations[0].nasdaq_stock_metadata_id
    ticker_metadata = session.query(NASDAQStockMetadata).filter(NASDAQStockMetadata.id == recommendation_metadata_id).one()
    ticker_with_close_pred_over_time[ticker_metadata.symbol] = [(top_recommendations[0].one_hundredth_date,top_recommendations[0].close)]
    for index, recommendation in enumerate(top_recommendations):
      if len(ticker_with_close_pred_over_time.keys()) == n:
         break
      if recommendation.nasdaq_stock_metadata_id == recommendation_metadata_id:
         ticker_with_close_pred_over_time[ticker_metadata.symbol].append((recommendation.one_hundredth_date,recommendation.close))
         continue
      ticker_metadata = session.query(NASDAQStockMetadata).filter(NASDAQStockMetadata.id == recommendation.nasdaq_stock_metadata_id).one()
      ticker_with_close_pred_over_time[ticker_metadata.symbol] = [(recommendation.one_hundredth_date,recommendation.close)]
      recommendation_metadata_id = recommendation.nasdaq_stock_metadata_id

    # Close the session (optional, but recommended)
    session.close()

    return ticker_with_close_pred_over_time

def get_mavg_100_close_chart(sqlEngine) -> dict[any]:
  Session = sessionmaker(bind=sqlEngine)
  session = Session()

  mavg_close_prices = session.query(MovingAverage100ToClosingPrices).group_by(MovingAverage100ToClosingPrices.id).order_by(func.count().desc()).all()

  ticker_with_mavg_close_over_time = {}

  for index, mavg_to_close_price in enumerate(mavg_close_prices):
    print(f"mavg_to_close_price.ticker = {mavg_to_close_price.ticker}")
    if mavg_to_close_price.ticker not in ticker_with_mavg_close_over_time:
      ticker_with_mavg_close_over_time[mavg_to_close_price.ticker] = []
    ticker_with_mavg_close_over_time[mavg_to_close_price.ticker].append((index, "MAVG100", mavg_to_close_price.mavg))
    ticker_with_mavg_close_over_time[mavg_to_close_price.ticker].append((index, "Close Price", mavg_to_close_price.close))

  session.close()

  return ticker_with_mavg_close_over_time

def get_sma_20_diff_chart(sqlEngine, strategy: str, n: int = 5) -> dict[any]:
  # Create a session
  Session = sessionmaker(bind=sqlEngine)
  session = Session()

  top_recommendations = session.query(Recommend).filter(Recommend.signal_transformers == 1 and Recommend.signal_pytorch == 1).group_by(Recommend.nasdaq_stock_metadata_id, Recommend.id).order_by(func.count().desc()).all()

  ticker_with_close_pred_over_time = {}
  recommendation_metadata_id = top_recommendations[0].nasdaq_stock_metadata_id
  ticker_metadata = session.query(NASDAQStockMetadata).filter(NASDAQStockMetadata.id == recommendation_metadata_id).one()
  ticker_with_close_pred_over_time[ticker_metadata.symbol] = [(top_recommendations[0].one_hundredth_date,top_recommendations[0].sma_twenty_pytorch if strategy == "pytorch" else top_recommendations[0].sma_twenty_transformers)]
  for index, recommendation in enumerate(top_recommendations):
    if len(ticker_with_close_pred_over_time.keys()) == n:
        break
    if recommendation.nasdaq_stock_metadata_id == recommendation_metadata_id:
        ticker_with_close_pred_over_time[ticker_metadata.symbol].append((recommendation.one_hundredth_date,recommendation.sma_twenty_pytorch if strategy == "pytorch" else recommendation.sma_twenty_transformers))
        continue
    ticker_metadata = session.query(NASDAQStockMetadata).filter(NASDAQStockMetadata.id == recommendation.nasdaq_stock_metadata_id).one()
    ticker_with_close_pred_over_time[ticker_metadata.symbol] = [(recommendation.one_hundredth_date,recommendation.sma_twenty_pytorch if strategy == "pytorch" else recommendation.sma_twenty_transformers)]
    recommendation_metadata_id = recommendation.nasdaq_stock_metadata_id

  # Close the session (optional, but recommended)
  session.close()

  return ticker_with_close_pred_over_time