-- Lists all genres not linked to the show Dexter
SELECT DISTINCT g.`name`
FROM `tv_genres` AS g
LEFT JOIN (
    SELECT sg.`genre_id`
    FROM `tv_shows` AS s
    JOIN `tv_show_genres` AS sg ON s.`id` = sg.`show_id`
    WHERE s.`title` = 'Dexter'
) AS dexter_genres ON g.`id` = dexter_genres.`genre_id`
WHERE dexter_genres.`genre_id` IS NULL
ORDER BY g.`name`;

