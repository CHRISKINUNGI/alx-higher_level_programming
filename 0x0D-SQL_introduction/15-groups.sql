-- script to lists records with the same score in second_table
-- displays score, no of records for this score with
-- label number
-- in descending order

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER bY number DESC;