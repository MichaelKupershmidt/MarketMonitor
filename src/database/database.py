def insert_basic_financials(data):
    day10_average_trading_volume = data.get("10DayAverageTradingVolume")
    week13_price_return_daily = data.get("13WeekPriceReturnDaily")
    week26_price_return_daily = data.get("26WeekPriceReturnDaily")
    month3_average_trading_volume = data.get("3MonthAverageTradingVolume")
    week52_high = data.get("52WeekHigh")
    week52_high_date = data.get("52WeekHighDate")
    week52_low = data.get("52WeekLow")
    week52_low_date = data.get("52WeekLowDate")
    week52_price_return_daily = data.get("52WeekPriceReturnDaily")
    day5_price_return_daily = data.get("5DayPriceReturnDaily")
    month_to_date_price_return_daily = data.get("monthToDatePriceReturnDaily")
    year_to_date_price_return_daily = data.get("yearToDatePriceReturnDaily")
    price_relative_to_sp500_13_week = data.get("priceRelativeToS&P50013Week")
    price_relative_to_sp500_26_week = data.get("priceRelativeToS&P50026Week")
    price_relative_to_sp500_4_week = data.get("priceRelativeToS&P5004Week")
    price_relative_to_sp500_52_week = data.get("priceRelativeToS&P50052Week")
    price_relative_to_sp500_ytd = data.get("priceRelativeToS&P500Ytd")

    # Define the company_id and date values
    company_id = 1  # Hard-coded company_id
    date = 'now()'  # Hard-coded date to use SQL now()

    # Generate the SQL INSERT statement
    insert_statement = f"""
    INSERT INTO TradingVolumePriceReturns (
        company_id, date, 
        day10_average_trading_volume, week13_price_return_daily, week26_price_return_daily, month3_average_trading_volume, 
        week52_high, week52_high_date, week52_low, week52_low_date, week52_price_return_daily, 
        day5_price_return_daily, month_to_date_price_return_daily, year_to_date_price_return_daily, 
        price_relative_to_sp500_13_week, price_relative_to_sp500_26_week, price_relative_to_sp500_4_week, 
        price_relative_to_sp500_52_week, price_relative_to_sp500_ytd
    ) VALUES (
        {company_id}, {date}, 
        {day10_average_trading_volume}, {week13_price_return_daily}, {week26_price_return_daily}, {month3_average_trading_volume}, 
        {week52_high}, '{week52_high_date}', {week52_low}, '{week52_low_date}', {week52_price_return_daily}, 
        {day5_price_return_daily}, {month_to_date_price_return_daily}, {year_to_date_price_return_daily}, 
        {price_relative_to_sp500_13_week}, {price_relative_to_sp500_26_week}, {price_relative_to_sp500_4_week}, 
        {price_relative_to_sp500_52_week}, {price_relative_to_sp500_ytd}
    );
    """