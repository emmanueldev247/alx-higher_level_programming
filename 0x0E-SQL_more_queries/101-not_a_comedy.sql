-- Lists all shws without the genre Comedy in the database
SELECT DISTINCT s.title
FROM tv_shows AS s
LEFT JOIN (
    SELECT sg.show_id
    FROM tv_genres AS g
    JOIN tv_show_genres AS sg ON g.id = sg.genre_id
    WHERE g.name = 'Comedy'
) AS comedy_show ON s.id = comedy_show.show_id
WHERE comedy_show.show_id IS NULL OR comedy_show.show_id IS NULL
ORDER BY s.title;
