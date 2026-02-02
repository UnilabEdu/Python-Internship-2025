from app import app, db, Movie

with app.app_context():
    movies = Movie.query.filter(Movie.id.in_([6])).all()

    print("Deleting movies:")
    for m in movies:
        print(m.id, m.name, m.img)
        db.session.delete(m)

    db.session.commit()

print("Done ✅ Movies with ID 6 deleted.")
