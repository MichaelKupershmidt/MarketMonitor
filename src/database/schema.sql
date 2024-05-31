CREATE TABLE Company(
    company_id SERIAL PRIMARY KEY,
    country VARCHAR(255),
    currency VARCHAR(10),
    estimate_currency VARCHAR(10),
    exchange VARCHAR(255),
    industry VARCHAR(255),
    ipo DATE,
    logo VARCHAR(255),
    market_capitalization FLOAT,
    name VARCHAR(255),
    phone VARCHAR(20),
    shares_outstanding FLOAT,
    ticker VARCHAR(10),
    weburl VARCHAR(255)
);

CREATE TABLE TradingVolumePriceReturns (
    id SERIAL PRIMARY KEY,
    company_id INTEGER NOT NULL,
    date DATE NOT NULL,
    day10_average_trading_volume FLOAT CHECK (day10_average_trading_volume >= 0),
    month3_average_trading_volume FLOAT CHECK (month3_average_trading_volume >= 0),
    week52_high FLOAT CHECK (week52_high >= 0),
    week52_high_date DATE,
    week52_low FLOAT CHECK (week52_low >= 0),
    week52_low_date DATE,
    week52_price_return_daily FLOAT,
    week13_price_return_daily FLOAT,
    week26_price_return_daily FLOAT,
    day5_price_return_daily FLOAT,
    month_to_date_price_return_daily FLOAT,
    year_to_date_price_return_daily FLOAT,
    price_relative_to_sp500_13_week FLOAT,
    price_relative_to_sp500_26_week FLOAT,
    price_relative_to_sp500_4_week FLOAT,
    price_relative_to_sp500_52_week FLOAT,
    price_relative_to_sp500_ytd FLOAT,
    FOREIGN KEY (company_id) REFERENCES Company(company_id),
    CHECK (week52_high_date IS NULL OR week52_low_date IS NULL OR week52_high_date >= week52_low_date)
);

-- Add indexes for performance optimization on frequently queried columns
CREATE INDEX idx_company_date ON TradingVolumePriceReturns (company_id, date);
CREATE INDEX idx_week52_high_date ON TradingVolumePriceReturns (week52_high_date);
CREATE INDEX idx_week52_low_date ON TradingVolumePriceReturns (week52_low_date);
