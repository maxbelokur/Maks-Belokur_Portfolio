WITH first_purchases AS (
    SELECT
        customer_id,
        MIN(invoice_date) AS first_purch_date
    FROM online_retail
    WHERE quantity > 0
    GROUP BY customer_id
),
cohorts AS (
    SELECT 
        customer_id,
        TO_CHAR(first_purch_date, 'YYYY-MM') AS cohort_month,
        first_purch_date
    FROM first_purchases
),
retention AS (
    SELECT 
        c.cohort_month,
        c.customer_id,
        MIN(
			CASE WHEN o.invoice_date BETWEEN c.first_purch_date + INTERVAL '30 days' 
			AND c.first_purch_date + INTERVAL '60 days' THEN 1
			ELSE 0 END
        ) AS retained_30d,
        MIN( 
            CASE WHEN o.invoice_date BETWEEN c.first_purch_date + INTERVAL '60 days'
			AND c.first_purch_date + INTERVAL '90 days' THEN 1 
			ELSE 0 END
        ) AS retained_60d,
        MIN( 
            CASE WHEN o.invoice_date > c.first_purch_date + INTERVAL '90 days' THEN 1 ELSE 0 END
        ) AS retained_90d
    FROM cohorts c
    LEFT JOIN online_retail o
        ON c.customer_id = o.customer_id
        AND o.invoice_date > c.first_purch_date
    GROUP BY c.cohort_month, c.customer_id
)
SELECT 
    cohort_month,
    COUNT(DISTINCT customer_id) AS total_customers,
    TO_CHAR(AVG(retained_30d) * 100, 'FM999.00%') AS retention_30d,
    TO_CHAR(AVG(retained_60d) * 100, 'FM999.00%') AS retention_60d,
    TO_CHAR(AVG(retained_90d) * 100, 'FM999.00%') AS retention_90d
FROM retention
GROUP BY cohort_month
ORDER BY cohort_month;
