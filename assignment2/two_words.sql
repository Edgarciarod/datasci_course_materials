SELECT count(*) FROM (
	SELECT docid FROM frequency 
		WHERE term LIKE "transactions"
	INTERSECT
	SELECT docid FROM frequency 
		WHERE term LIKE "world");
	



