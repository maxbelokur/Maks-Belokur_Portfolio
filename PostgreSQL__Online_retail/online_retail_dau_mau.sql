WITH daily_data AS (
    SELECT 
        DATE_TRUNC('day', invoice_date) AS invoice_day,
        COUNT(DISTINCT customer_id) AS daily_customer
    FROM online_retail
    GROUP BY invoice_day
),
monthly_data AS (
	SELECT 
	    TO_CHAR(invoice_day, 'YYYY-MM') AS invoice_month,
	    daily_customer AS DAU,
	    SUM(daily_customer) OVER(PARTITION BY DATE_TRUNC('month', invoice_day)) AS MAU
	FROM daily_data
)
SELECT
	invoice_month,
	ROUND(AVG(DAU), 2) AS AVG_DAU,
	MAX(MAU) AS MAU
FROM monthly_data
GROUP BY invoice_month
ORDER BY invoice_month
