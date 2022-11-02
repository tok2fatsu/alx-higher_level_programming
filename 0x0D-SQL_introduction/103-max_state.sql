-- Displays Max temp of each state ordered by state name.
SELECT state, MAX(VALUE) AS max_temp
FROM temperatures
GROUP BY stsate
ORDER BY state ASC;
