SELECT 
	EXTRACT(WEEK FROM invoice_date) AS week_number,
	TO_CHAR(DATE_TRUNC('week',invoice_date)::DATE, 'YYYY-MM-DD') AS first_weekday,
	COUNT(DISTINCT customer_id) FILTER (WHERE EXTRACT(DOW FROM invoice_date) = 1) AS MON,
	COUNT(DISTINCT customer_id) FILTER (WHERE EXTRACT(DOW FROM invoice_date) = 2) AS TUE,
	COUNT(DISTINCT customer_id) FILTER (WHERE EXTRACT(DOW FROM invoice_date) = 3) AS WED,
	COUNT(DISTINCT customer_id) FILTER (WHERE EXTRACT(DOW FROM invoice_date) = 4) AS THU,
	COUNT(DISTINCT customer_id) FILTER (WHERE EXTRACT(DOW FROM invoice_date) = 5) AS FRI,
	COUNT(DISTINCT customer_id) FILTER (WHERE EXTRACT(DOW FROM invoice_date) = 6) AS SAT,
	COUNT(DISTINCT customer_id) FILTER (WHERE EXTRACT(DOW FROM invoice_date) = 0) AS SUN
FROM online_retail
WHERE TO_CHAR(invoice_date, 'YYYY') = '2011'
GROUP BY week_number, first_weekday
ORDER BY week_number
