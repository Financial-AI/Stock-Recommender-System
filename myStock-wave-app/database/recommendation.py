from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from .models import Recommend, NASDAQStockMetadata

def get_top_n_most_recent_recommended_securities(sqlEngine, n: int = 5) -> dict[any]:
    # Create a session
    Session = sessionmaker(bind=sqlEngine)
    session = Session()

    top_recommendations = session.query(Recommend).filter(Recommend.signal_transformers == 1 and Recommend.signal_pytorch == 1).group_by(Recommend.nasdaq_stock_metadata_id, Recommend.id).order_by(func.count().desc()).all()

    recommended_securities = []
    recommendation_metadata_id = top_recommendations[0].nasdaq_stock_metadata_id
    ticker_metadata = session.query(NASDAQStockMetadata).filter(NASDAQStockMetadata.id == recommendation_metadata_id).one()
    recommended_securities.append(ticker_metadata)
    for index, recommendation in enumerate(top_recommendations):
      if len(recommended_securities) == n:
         break
      if recommendation.nasdaq_stock_metadata_id == recommendation_metadata_id:
         continue
      ticker_metadata = session.query(NASDAQStockMetadata).filter(NASDAQStockMetadata.id == recommendation.nasdaq_stock_metadata_id).one()
      recommended_securities.append(ticker_metadata)
      recommendation_metadata_id = recommendation.nasdaq_stock_metadata_id

    # Close the session (optional, but recommended)
    session.close()

    return recommended_securities