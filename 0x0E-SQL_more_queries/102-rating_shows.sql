-- List all shows from hbtn_0d_tvshows_rate by their rating
SELECT ts.title, SUM(tsr.rate) as rating
FROM tv_shows as ts
JOIN tv_show_ratings as tsr
ON ts.id = tsr.show_id
GROUP BY ts.id
ORDER BY rating DESC;
