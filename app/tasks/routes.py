from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models import Task
from app.tasks import tasks
from app.tasks.forms import TaskForm


@tasks.route("/", methods=["GET"])
@login_required
def list_tasks():
    form = TaskForm()
    tasks_list = current_user.tasks.order_by(Task.created_at.desc()).all()
    return render_template("tasks/list.html", title="Görevler", form=form, tasks=tasks_list)


@tasks.route("/add", methods=["POST"])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            user_id=current_user.id,
        )
        db.session.add(task)
        db.session.commit()
        flash("Görev başarıyla eklendi.", "success")
    else:
        for field_errors in form.errors.values():
            for error in field_errors:
                flash(error, "danger")
    return redirect(url_for("tasks.list_tasks"))


@tasks.route("/<int:id>/delete", methods=["POST"])
@login_required
def delete_task(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    flash("Görev silindi.", "info")
    return redirect(url_for("tasks.list_tasks"))


@tasks.route("/<int:id>/toggle", methods=["POST"])
@login_required
def toggle_task(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    task.is_done = not task.is_done
    db.session.commit()
    flash("Görev durumu güncellendi.", "success")
    return redirect(url_for("tasks.list_tasks"))
