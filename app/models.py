from app import db
    
class City(db.Model):
     
    id = db.Column(db.Integer, primary_key = True)
    city_name = db.Column(db.String(80), unique = True)
    city_rank = db.Column(db.Integer, index = True)
    is_visited = db.Column(db.Boolean, default = False)

    def  __ref__(self):
        return f"City('{self.city_name}', {self.city_rank}, {self.is_visited})"

