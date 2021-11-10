from app import myobj
from flask import render_template, escape, flash, redirect, request
from app.forms import TopCities
from app import db
from app.models import City

@myobj.route("/", methods = ['GET', 'POST'])
def home():
    form = TopCities()

    if form.validate_on_submit():
        flash(f' {form.city_name.data} successfully added!')

        cityname = form.city_name.data
        cityrank = form.city_rank.data
        visited = form.is_visited.data
        city = City(city_name = cityname, city_rank = cityrank, is_visited = visited)
        db.session.add(city)
        db.session.commit()
        return redirect('/')
        
    rankcities = City.query.order_by(City.city_rank).all()
    return render_template('home.html', form = form, rankcities = rankcities)
