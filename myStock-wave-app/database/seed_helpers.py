
from database.models import Recommend, NASDAQStock, NASDAQStockMetadata
from sqlalchemy.orm import sessionmaker
import pandas as pd
import os


def seed_nasdaq_stock_db_tables(sqlEngine: any) -> None:
    home_directory = os.environ["HOME"]
    nasdaq_path = f"{home_directory}/src/sjsu/Stock-Recommender-System/myStock-wave-app/database/seed/NASDAQ_Yahoo_Finance"
    directory_path = os.path.join(nasdaq_path, "stocks")

    url = "https://en.wikipedia.org/wiki/Nasdaq-100"
    nasdaq100_meta = pd.read_html(url)[4]
    nasdaq100_meta.to_csv(f"{nasdaq_path}/nasdaq100_meta.csv", index=False)
    nasdaq100_ticker_list = nasdaq100_meta["Ticker"].tolist()

    for file in os.listdir(directory_path):
        filename_without_extension = os.path.splitext(file)[0]  # Get filename without extension
        if filename_without_extension in nasdaq100_ticker_list:
            print(f"Found {filename_without_extension} file in NASDAQ100 Meta list, loading MySQL NASDAQStock table")
            df = pd.read_csv(os.path.join(directory_path, file))

            # Create a session
            Session = sessionmaker(bind=sqlEngine)
            session = Session()
            # Create a new NASDAQ stock record

            for index, row in df.iterrows():
                if pd.isna(row["Date"]):
                    continue
                if pd.isna(row["Open"]):
                    continue
                if pd.isna(row["High"]):
                    continue
                if pd.isna(row["Low"]):
                    continue
                if pd.isna(row["Close"]):
                    continue
                if pd.isna(row["Adj Close"]):
                    continue
                if pd.isna(row["Volume"]):
                    continue

                new_record = NASDAQStock(
                    ticker = str(filename_without_extension),
                    date = str(row["Date"]),
                    open = float(row["Open"]),
                    high = float(row["High"]),
                    low = float(row["Low"]),
                    close = float(row["Close"]),
                    adj_close = float(row["Adj Close"]),
                    volume = int(row["Volume"]),
                )
                # Add the new record to the session
                session.add(new_record)
                # Commit the transaction
                
            session.commit()
            # Close the session (optional, but recommended)
            session.close()


def seed_symbols_valid_metadata(sqlEngine: any) -> None:
    home_directory = os.environ["HOME"]
    directory_path = f"{home_directory}/src/sjsu/Stock-Recommender-System/myStock-wave-app/database/seed/NASDAQ_Yahoo_Finance"

    df = pd.read_csv(os.path.join(directory_path, "symbols_valid_meta.csv"))

    # Create a session
    Session = sessionmaker(bind=sqlEngine)
    session = Session()
    # Create a new Recommend record


    for index, row in df.iterrows():
        new_record = NASDAQStockMetadata(
            is_nasdaq_traded = str(row["Nasdaq Traded"]),
            symbol = str(row["Symbol"]),
            security_name = str(row["Security Name"]),
            is_listing_exchange = str(row["Listing Exchange"]),
            market_category = str(row["Market Category"]),
            is_etf = str(row["ETF"]),
            round_lot_size = row["Round Lot Size"],
            is_used_for_testing = str(row["Test Issue"]),
            financial_status = str(row["Financial Status"]),
            cqs_symbol = str(row["CQS Symbol"]),
            next_shares = str(row["NextShares"])
        )
        # Add the new record to the session
        session.add(new_record)
        # Commit the transaction
        
    session.commit()
    # Close the session (optional, but recommended)
    session.close()

def seed_recommend_csv_data(sqlEngine: any) -> None:
    directory_path = "database/seed"
    for file in os.listdir(directory_path):
        if file.endswith('recommend.csv'):
            df = pd.read_csv(os.path.join(directory_path, file))

            filename_without_extension = os.path.splitext(file)[0]  # Get filename without extension
            filename_splitted = filename_without_extension.split("_")


            # Create a session
            Session = sessionmaker(bind=sqlEngine)
            session = Session()
            # Create a new Recommend record
            stock_metadata = session.query(NASDAQStockMetadata).filter(NASDAQStockMetadata.symbol == filename_splitted[0]).one()

            for index, row in df.iterrows():
                if pd.isna(row["MACD_diff_pytorch"]):
                    row["MACD_diff_pytorch"] = 0.0
                if pd.isna(row["MACD_diff_transformers"]):
                    row["MACD_diff_transformers"] = 0.0
                if pd.isna(row["Decision MACD_pytorch"]):
                    row["Decision MACD_pytorch"] = False
                if pd.isna(row["Decision MACD_transformers"]):
                    row["Decision MACD_transformers"] = False
                if pd.isna(row["SMA20_pytorch"]):
                    row["SMA20_pytorch"] = 0.0
                if pd.isna(row["SMA20_transformers"]):
                    row["SMA20_transformers"] = 0.0
                if pd.isna(row["SMA50_pytorch"]):
                    row["SMA50_pytorch"] = 0.0
                if pd.isna(row["SMA50_transformers"]):
                    row["SMA50_transformers"] = 0.0
                if pd.isna(row["Signal_pytorch"]):
                    row["Signal_pytorch"] = False
                if pd.isna(row["Signal_transformers"]):
                    row["Signal_transformers"] = False
                if pd.isna(row["Decision GC_pytorch"]):
                    row["Decision GC_pytorch"] = False
                if pd.isna(row["Decision GC_transformers"]):
                    row["Decision GC_transformers"] = False
                if pd.isna(row["RSI_pytorch"]):
                    row["RSI_pytorch"] = 0.0
                if pd.isna(row["RSI_transformers"]):
                    row["RSI_transformers"] = 0.0
                if pd.isna(row["SMA200_pytorch"]):
                    row["SMA200_pytorch"] = 0.0
                if pd.isna(row["SMA200_transformers"]):
                    row["SMA200_transformers"] = 0.0
                if pd.isna(row["Decision RSI/SMA_pytorch"]):
                    row["Decision RSI/SMA_pytorch"] = False
                if pd.isna(row["Decision RSI/SMA_transformers"]):
                    row["Decision RSI/SMA_transformers"] = False
                if pd.isna(row["Decision Financial Status"]):
                    row["Decision Financial Status"] = False

                new_record = Recommend(
                    one_hundredth_date = row["100th Date"],
                    close = row["Close"],
                    macd_diff_pytorch = row["MACD_diff_pytorch"],
                    macd_diff_transformers = row["MACD_diff_transformers"],
                    decision_macd_diff_pytorch = row["Decision MACD_pytorch"],
                    decision_macd_diff_transformers = row["Decision MACD_transformers"],
                    sma_twenty_pytorch= row["SMA20_pytorch"],
                    sma_twenty_transformers= row["SMA20_transformers"],
                    sma_fifty_pytorch= row["SMA50_pytorch"],
                    sma_fifty_transformers= row["SMA50_transformers"],
                    signal_pytorch= row["Signal_pytorch"],
                    signal_transformers= row["Signal_transformers"],
                    decision_gc_pytorch= row["Decision GC_pytorch"],
                    decision_gc_transformers= row["Decision GC_transformers"],
                    rsi_pytorch= row["RSI_pytorch"],
                    rsi_transformers= row["RSI_transformers"],
                    sma_two_hundred_pytorch= row["SMA200_pytorch"],
                    sma_two_hundred_transformers= row["SMA200_transformers"],
                    decision_rsi_and_sma_pytorch= row["Decision RSI/SMA_pytorch"],
                    decision_rsi_and_sma_transformers= row["Decision RSI/SMA_transformers"],
                    decision_final_status= row["Decision Financial Status"],
                    nasdaq_stock_metadata_id= stock_metadata.id
                )
                # Add the new record to the session
                session.add(new_record)
                # Commit the transaction
            session.commit()
            # Close the session (optional, but recommended)
            session.close()