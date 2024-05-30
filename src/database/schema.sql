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
