-- script that lists shows contained in database: hbtn_0c_tvshows
-- Displays NULL for shows without genres.

SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
