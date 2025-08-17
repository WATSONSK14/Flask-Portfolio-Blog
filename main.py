from flask import Flask, render_template, request, redirect, url_for, flash, session
from forms import AdminLoginForm, RegisterForm, Login_Form, ContantForm
from flask_bootstrap import Bootstrap5
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, LoginManager, current_user, logout_user, login_required
from flask_migrate import Migrate
from datetime import datetime, timezone, timedelta
import pytz
from models import db, User, UserVote, Message, Vote
from admin import admin
from dotenv import load_dotenv
from config import Config

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)
admin.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = "Please log in to get in touch with us."
login_manager.login_message_category = "info"

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

@app.context_processor
def inject_logged_in():
    return dict(logged_in=current_user.is_authenticated)

#Routes

#AdminLogin
@app.route('/admin/login', methods=["GET", "POST"])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.is_superuser and user.password == form.password.data:
            login_user(user)
            flash("Welcome admin!", "success")
            return redirect('/admin')
        else:
            flash("Invalid credentials or not an admin!", "danger")
    return render_template("admin_login.html", form=form)

#AdminLogout
@app.route('/admin/logout')
def admin_logout():
    logout_user()
    flash("Logged out", "info")
    return redirect(url_for('admin_login'))

#HomePage
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == "POST":   
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        
        action = request.form.get('action')
        form_id = request.form.get('post_id')

        vote = Vote.query.filter_by(
            post_id=form_id).first()

        user_vote = UserVote.query.filter_by(
            user_id=current_user.id,
            vote_post=form_id
        ).first()

        if user_vote:
            if user_vote.vote_type != action and action in ["like", "dislike"]:
                if user_vote.vote_type == "like":
                    vote.like -= 1
                else:
                    vote.dislike -= 1

                user_vote.vote_type = action
                if action == "like":
                    vote.like += 1
                else:
                    vote.dislike += 1

                db.session.commit()
        else:
            if action in ["like", "dislike"]:
                new_vote = UserVote(
                    user_id=current_user.id,
                    vote_type=action,
                    vote_post=form_id
                )
                db.session.add(new_vote)

                if action == "like":
                    vote.like += 1
                else:
                    vote.dislike += 1
                db.session.commit()

    votes = Vote.query.order_by(Vote.post_id).all()
    return render_template("home.html", votes=votes)

#About
@app.route('/about')
def about():
    return render_template('about.html')

#Gallery
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

#Contact
@app.route('/contact', methods=['GET','POST'])
@login_required
def contact():
    form = ContantForm()
    if request.method == "GET":
        form.email.data = current_user.email
    if request.method == "POST":
        messages = Message.query.filter_by(user_id=current_user.id).all()
        for message in messages:
            if message.read == False:
                flash("You have an unread support request. Please review it before creating a new one.", "info")
                return redirect(url_for('home'))
        if form.validate_on_submit():
            name = request.form.get('name')
            surname = request.form.get('surname')
            email = current_user.email
            subject = request.form.get('subject')
            message = request.form.get('message')

            now_utc = datetime.now(timezone.utc)
            turkey_tz = pytz.timezone("Europe/Istanbul")
            turkey_time = now_utc.astimezone(turkey_tz)
            rounded = turkey_time + timedelta(microseconds=500_000)
            rounded.replace(microsecond=0)

            new_message = Message(user_id = current_user.id,
                                  name = name,
                                  surname = surname,
                                  email=email,
                                  subject = subject,
                                  message = message,
                                  created_at=rounded,)
            db.session.add(new_message)
            db.session.commit()

            flash("Thank you for your message! We'll respond to your email as soon as we can.","success")
            return redirect(url_for('home'))
    return render_template('contant.html', form=form)

#Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.password.data != form.two_password.data:
                flash("Oops! Your passwords don’t match. Please try again.", "danger")
                return render_template("register.html", form=form)
                
            email = form.email.data
            result = db.session.execute(db.select(User).where(User.email==email))
            user = result.scalar()

            if user:
                flash("You've already signed up with that email, log in instead!", "danger")
                return render_template("register.html", form=form)
            
            hash_and_salted_password = generate_password_hash(
                request.form.get('password'),
                method='pbkdf2:sha256',
                salt_length=8
            )

            base_username = email = form.email.data.split('@')[0]
            username = base_username
            counter = 1

            while User.query.filter_by(username=username).first():
                username = f"{base_username}{counter}"
                counter += 1
            now_utc = datetime.now(timezone.utc)
            turkey_tz = pytz.timezone("Europe/Istanbul")
            turkey_time = now_utc.astimezone(turkey_tz)

            new_user = User(
                email=request.form.get('email'),
                password=hash_and_salted_password,
                username=username,
                created_at=turkey_time,
                last_login=None
            )
            db.session.add(new_user)
            db.session.commit()

            flash("Registration successful! You can now log in.", "success")
            return redirect(url_for('login'))  # Giriş sayfasına yönlendirme

    return render_template("register.html", form=form)

#Login
@app.route('/login', methods=['GET','POST'])
def login():
    form = Login_Form()
    if request.method  == "POST":
        if form.validate_on_submit():
            email = request.form.get('email')
            password = request.form.get('password')

            result = db.session.execute(db.select(User).where(User.email==email))
            user = result.scalar()
        
            if not user:
                flash("That email does not exist, please try again.", "danger")
                return redirect(url_for('login'))
            elif not check_password_hash(user.password, password):
                flash('Password incorrect, please try again.', "danger")
                return redirect(url_for('login'))
            else:
                login_user(user)
                now_utc = datetime.now(timezone.utc)
                turkey_tz = pytz.timezone("Europe/Istanbul")
                turkey_time = now_utc.astimezone(turkey_tz)
                rounded = turkey_time + timedelta(microseconds=500_000)
                rounded = rounded.replace(microsecond=0)
                user.last_login = rounded
                db.session.commit()
                session['login_time'] = datetime.now().isoformat()
                return redirect(url_for('home'))
            
    return render_template('login.html', form=form)

#UserLogout
@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('home'))

#UserPanel
@app.route('/user_panel', methods=['GET','POST'])
@login_required
def user_panel():
    messages = Message.query.filter_by(user_id=current_user.id).all()
    read_true = 0
    read_false = 0
    #Oturum Süresi
    login_time = datetime.fromisoformat(session['login_time'])
    now = datetime.now()
    diff = now - login_time

    hours, remainder = divmod(diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    oturum_süresi = f"{hours} saat {minutes} dakika"

    for message in messages:
        if message.read == True:
            read_true +=1
        else:
            read_false +=1

    context = {
        "messages":messages,
        "oturum_süresi":oturum_süresi,
        "read_true":read_true,
        "read_false":read_false,
    }

    return render_template('user_panel.html',**context)

#UserPanelDetail
@app.route('/user_detail', methods=['GET','POST'])
@login_required
def user_detail():
    user_vote = UserVote.query.filter_by(user_id=current_user.id).all()
    vote_like = 0
    vote_dislike = 0
    for vote in user_vote:
        if vote.vote_type == "like":
            vote_like += 1
        elif vote.vote_type == "dislike":
            vote_dislike +=1

    context = {
        "uservote":user_vote,
        "like":vote_like,
        "dislike":vote_dislike,
    }

    if request.method == "POST":
        action = request.form.get('action')
        if action == "save":
            new_username = request.form.get('username')
            existing_user = User.query.filter_by(username=new_username).first()
            if new_username == current_user.username:
                flash('This username is already in use by your account.', 'info')
                return redirect(url_for('user_detail'))
            if not existing_user:
                if len(new_username) > 16 or len(new_username) < 6:
                    flash('Please choose a username between 6 and 16 characters.', 'danger')
                    return redirect(url_for('user_detail'))
                else:
                    current_user.username = new_username
                    db.session.commit()
                    flash('Your changes were successfully saved!', 'success')
                    return redirect(url_for('user_panel'))
            else:
                flash('That username’s already in use—try picking another one.', 'danger')
                return redirect(url_for('user_panel'))
            
    return render_template("user_detail.html",**context)

#UserPanelMessages
@app.route('/user_panel/messages', methods=['GET','POST'])
@login_required
def panel_messages():
    messages = Message.query.filter_by(user_id=current_user.id).all()
    read_true = 0
    read_false = 0
    for message in messages:
        if message.read == True:
            read_true +=1
        else:
            read_false +=1
    context = {
        "messages":messages,
        "read_true":read_true,
        "read_false":read_false,
    }
    return render_template('messages.html',**context)

#UserPanelMessagesDetail
@app.route('/user_panel/messages/<int:id>', methods=['GET','POST'])
@login_required
def panel_message_detail(id):
    message = Message.query.filter_by(id=id, user_id=current_user.id).first()
    if not message:
        flash('Message not found.', 'danger')
        return redirect(url_for('panel_messages'))
    
    return render_template('message_detail.html', message=message)
