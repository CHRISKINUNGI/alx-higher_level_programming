-- Lists all cities in CA in hbtn_0d_usa
-- Results are in ascending cities.id

SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
