#!/usr/bin/env python3

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json



views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 3:
            flash('Note must be at least 3 characters', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit() 

            flash('Note added successfully!', category='success')
    
    from .functions import convert_utc_to_local
    import datetime
    today = datetime.datetime.now()
    year = today.year

    return render_template("home.html", user=current_user,year=year, convert_utc_to_local=convert_utc_to_local)

@views.route('/delete-note',methods=['POST'])
def deleteNote():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/about', methods=['GET'])

def about():
    import datetime
    today = datetime.datetime.now()
    year = today.year

    return render_template("about.html", user=current_user,year=year)
