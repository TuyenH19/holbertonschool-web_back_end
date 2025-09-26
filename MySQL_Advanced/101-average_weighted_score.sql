-- Average weighted score for all students

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    /* Update every user in one pass.
       - LEFT JOIN ensures users without corrections are included.
       - NULLIF avoids division by zero.
       - IFNULL/COALESCE maps NULL to 0 for users with no data.
    */
    UPDATE users AS u
    LEFT JOIN (
        SELECT
            c.user_id,
            SUM(c.score * p.weight) / NULLIF(SUM(p.weight), 0) AS avg_weighted
        FROM corrections AS c
        INNER JOIN projects AS p
            ON p.id = c.project_id
        GROUP BY c.user_id
    ) AS t
        ON t.user_id = u.id
    SET u.average_score = IFNULL(t.avg_weighted, 0);
END$$

DELIMITER ;
