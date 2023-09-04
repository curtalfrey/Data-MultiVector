from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import shutil

app = Flask(__name__)



@app.route('/delete/<filename>')
@login_required
def delete_file(filename):
    upload_folder = app.config['UPLOAD_FOLDER']
    user_trash_folder = os.path.join(app.root_path, 'trash', current_user.username)

    if not os.path.exists(user_trash_folder):
        os.makedirs(user_trash_folder, exist_ok=True)
    
    file_path = os.path.join(upload_folder, filename)

    if os.path.exists(file_path):
        # Move file to user's trash folder
        trash_path = os.path.join(user_trash_folder, filename)
        os.rename(file_path, trash_path)
        flash(f'File {filename} moved to trash.', 'success')
    else:
        flash(f'File {filename} not found.', 'danger')

    return redirect(url_for('files'))

@app.route('/trash')
@login_required
def trash():
    user_trash_folder = os.path.join(app.root_path, 'trash', current_user.username)
    trashed_files = []

    for filename in os.listdir(user_trash_folder):
        file_path = os.path.join(user_trash_folder, filename)
        if os.path.isfile(file_path):
            trashed_files.append({
                'filename': filename,
                'size': os.path.getsize(file_path),
                'url': url_for('recovery', filename=filename),
            })

    return render_template('trash.html', trashed_files=trashed_files)

@app.route('/recover/<filename>')
@login_required
def recovery(filename):
    user_trash_folder = os.path.join(app.root_path, 'trash', current_user.username)
    trash_path = os.path.join(user_trash_folder, filename)
    upload_folder = app.config['UPLOAD_FOLDER']

    if os.path.exists(trash_path):
        # Move file back from trash to the original folder
        restored_path = os.path.join(upload_folder, filename)
        shutil.move(trash_path, restored_path)
        flash(f'File {filename} has been restored.', 'success')
    else:
        flash(f'File {filename} not found in trash.', 'danger')

    return redirect(url_for('trash'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
