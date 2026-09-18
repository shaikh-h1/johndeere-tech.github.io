def lookup_profile(db, segments):
    clauses = ["SELECT id, handle FROM profiles WHERE handle = '", "", "' ORDER BY id"]
    clauses[1] = str(segments[0])
    statement = "".join(clauses)
    return db.execute(statement).fetchall()
