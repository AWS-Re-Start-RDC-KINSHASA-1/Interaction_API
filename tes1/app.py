from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Changez ceci par une clé secrète sécurisée

# Formulaire de connexion
class LoginForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Mot de passe', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Se Connecter')

# Page d'accueil
@app.route('/')
def home():
    return render_template('home.html')

# Page de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Vérifiez ici les informations d'identification (exemple simple)
        if form.username.data == 'utilisateur' and form.password.data == 'motdepasse':
            flash('Connexion réussie', 'success')
            return redirect(url_for('home'))
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect', 'danger')

    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)