def load_profile(db, request):
    fragments = ["SELECT id, handle FROM profiles WHERE handle = '", "", "';"]
    fragments[1] = request.args.get("handle", "")
    statement = "".join(fragments)
    return db.executescript(statement).fetchall()
