-- Average_weighted_score

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_weighted FLOAT DEFAULT 0;

    /* Compute weighted average safely (avoid division by zero) */
    SELECT
        IFNULL(
            SUM(c.score * p.weight) / NULLIF(SUM(p.weight), 0),
            0
        )
    INTO avg_weighted
    FROM corrections AS c
    INNER JOIN projects AS p
        ON p.id = c.project_id
    WHERE c.user_id = user_id;

    /* Persist result on the user */
    UPDATE users
    SET average_score = avg_weighted
    WHERE id = user_id;
END$$

DELIMITER ;
