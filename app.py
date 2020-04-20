import json
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sajjadsalaria@localhost:5432/todo'

db = SQLAlchemy(app)


migrate = Migrate(app, db)

class Todo(db.Model):
      __tablename__ = 'todos'
      id = db.Column(db.Integer, primary_key=True)
      description = db.Column(db.String(), nullable=False)
      completed = db.Column(db.Boolean, nullable=False, default=False)

      def __repr__(self):
            return f'<Todo {self.id} {self.description}>'

# db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
  description = request.get_json()['description']
  todo = Todo(description=description)
  db.session.add(todo)
  db.session.commit()
  return jsonify({
    'description': todo.description
  })


@app.route('/')
def index():
  return render_template('index.html', data=Todo.query.all())