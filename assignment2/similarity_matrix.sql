SELECT  SUM(count_new) FROM (
	SELECT a.row_num, b.col_num, (a.value *  b.value ) as count_new
		FROM frequency AS a INNER JOIN frequency AS b ON a.docid = b.docid)