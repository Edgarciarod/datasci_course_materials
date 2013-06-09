SELECT  SUM(value_new) FROM (
	SELECT a.row_num, b.col_num, (a.value *  b.value ) as value_new
		FROM A AS a INNER JOIN B AS b ON a.col_num = b.row_num)
	WHERE row_num = 2 and col_num = 3;