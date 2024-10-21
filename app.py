"Get / Post Handlers. Any socket event handlers will be present in socket_routes"

from flask import Flask, render_template, request, abort
from flask_socketio import SocketIO
import db
from flask import jsonify

app = Flask(__name__)
socketio = SocketIO(app)

from models import *

@app.route("/")
def index():
    return render_template("login.jinja")

@app.route("/home")
def home():
    username = request.args.get("username")
    user = db.get_user(username)
    role = user.role
    return render_template("home.jinja", username = username, role = role)
    
@app.route('/signup')
def signup():
    return render_template('signup.jinja') 

@app.route('/signup', methods=['POST'])
def create_user():
    if not request.is_json:
        abort(400)
    
    username = request.json.get("username")    
    password = request.json.get("password")   
    role = "user"
    
    if db.get_user(username) is not None:
        return jsonify({"msg": "User already exists. Please log in!"}), 409
    
    db.insert_user(username, password, role)
    return jsonify({"message": "User created successfully!"}), 201

@app.route('/login')
def login():
    return render_template('login.jinja') 

@app.route('/login/user', methods = ['POST'])
def login_user():
    
    username = request.json.get("username")    
    password = request.json.get("password")   

    if db.get_user(username) is None:
        return jsonify({"msg": "User Doesn't Exist. Please Sign up!"}), 409    
    if db.attempt_login(username, password):    
       return jsonify({"msg": "Login Successful!"}), 200    
    else:
       return jsonify({"msg": "Incorrect Password. Please try again."}), 409    

@app.route('/packages', methods=['POST'])
def create_package():
    if not request.is_json:
        abort(400)
    title = request.json.get("title")
    content = request.json.get("category") #I accidentally swapped these around. Oops.
    category = request.json.get("content") #Keep as is or itll break
    price = request.json.get("price")
    duration = request.json.get("duration")
    image = request.json.get("imageLink")
        
    if None in (title, category, content, price, duration, image):
        return jsonify({"msg": "One or more inputs missing!"}), 409  
    else:  
        db.insert_package(title, category, content, price, duration, image)
        return jsonify({"message": "Package created successfully!"}), 201

@app.route('/packages', methods=['GET'])
def get_packages():
    category = request.args.get("category")
    minPrice = request.args.get("min")
    maxPrice = request.args.get("max")
    duration = request.args.get("duration")
    
    categories = []
    if category:
        categories = [cat.strip().strip('"') for cat in category.split(',')]

    durations = []
    if duration:
        durations = [dur.strip().strip('"') for dur in duration.split(',')]
    
    packages = db.get_packages(categories, minPrice, maxPrice, durations)
    
    packages_data = []
    
    for package in packages:
        if package:
            packages_data.append({
                "id": package.id, 
                "title": package.title, 
                "category": package.category,
                "content": package.content,
                "price": package.price, 
                "duration": package.duration,
                "image": package.image
            })
            
    return jsonify(packages_data)

@app.route('/packages/<int:package_id>', methods = ['GET'])
def get_package_by_id(package_id):
    package = db.get_package_by_id(package_id)
    
    if package is None:
        return jsonify({"msg": "Package Doesn't Exist"}), 404
    
    if package:
        package_data = {
            "id": package.id, 
            "title": package.title, 
            "category": package.category,
            "content": package.content,
            "price": package.price, 
            "duration": package.duration,
            "image": package.image
        }
        return jsonify(package_data)    
    else:
        return jsonify({"msg": "Package missing"}), 404

@app.route('/packages/<int:package_id>', methods = ['DELETE'])
def remove_package(package_id):
    
    print(package_id)
    
    package = db.get_package_by_id(package_id)
    
    if package is None:
        return jsonify({"msg": "Package Doesn't Exist"}), 404
    
    db.delete_package(package_id)
    
    return jsonify({"message": "Article deleted successfully!"}), 200


@app.route('/packages/<int:package_id>', methods=['PUT'])
def update_package(package_id):
    if not request.is_json:
        abort(400)

    title = request.json.get("title")
    content = request.json.get("category") #I accidentally swapped these around. Oops.
    category = request.json.get("content") #Keep as is or itll break
    price = request.json.get("price")
    duration = request.json.get("duration")
    image = request.json.get("imageLink")
    
    print(title)
    
    db.update_package(package_id, title, content, category, price, duration, image)
    
    return jsonify({"message": "Article updated successfully!"}), 200

@app.route('/checkout')
def checkout():
    return render_template('checkout.jinja')


if __name__ == '__main__':
    
    db.insert_user("Admin", "password", "admin")
    
    db.insert_package("Sydney", 
                     "Sydney, capital of New South Wales and one of Australia's largest cities, is best known for its harbourfront Sydney Opera House, with a distinctive sail-like design. Massive Darling Harbour and the smaller Circular Quay port are hubs of waterside life, with the arched Harbour Bridge and esteemed Royal Botanic Garden nearby. Sydney Tower’s outdoor platform, the Skywalk, offers 360-degree views of the city and suburbs.", 
                     'City Break',
                     500,
                     "1 Week",
                     "https://www.bridgeclimb.com/getmedia/17e5515e-fb1f-453a-b309-dc48ee0eae16/Hero.jpg?width=2000&height=1125&ext=.jpg")
    
    db.insert_package("Bondi Beach",
                      "The sweeping white-sand crescent of Bondi is one of Australia’s most iconic beaches. Reliable waves draw surfers while, nearby, hardy locals swim in the Icebergs ocean pool year-round. Trendy, health-conscious Sydneysiders head to laid-back cafes around Hall Street, while hip backpackers frequent the area's casual pubs. Walkers and joggers use the clifftop Bondi to Coogee Coastal Walk, with its dramatic scenery.",
                      "Beach Holidays",
                      250,
                      "1 Night",
                      "https://upload.wikimedia.org/wikipedia/commons/7/79/Bondi_from_above.jpg")
    
    
    socketio.run(app, host = 'localhost', port = 1204)