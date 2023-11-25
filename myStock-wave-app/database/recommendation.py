from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import Base, Recommend, NASDAQStockMetadata

def get_top_n_most_recent_recommended_securities(sqlEngine, n: int = 5) -> dict[any]:
    # Create a session
    Session = sessionmaker(bind=sqlEngine)
    session = Session()

    top_recommendations = session.query(Recommend).filter(Recommend.signal_transformers == 1).order_by(Recommend.one_hundredth_date.desc()).limit(n).all()

    recommended_securities = []
    for index, recommendation in enumerate(top_recommendations):
      ticker_metadata = session.query(NASDAQStockMetadata).filter(NASDAQStockMetadata.id == recommendation.nasdaq_stock_metadata_id).one()
      recommended_securities.append(ticker_metadata)

    # Close the session (optional, but recommended)
    session.close()

    return recommended_securities