DELIMITER //
CREATE PROCEDURE delete_developer(IN in_dev_id INT)
BEGIN
DELETE FROM Developers WHERE developer_id = in_dev_id;
SELECT ROW_COUNT() AS affected_rows;
END //
DELIMITER ;