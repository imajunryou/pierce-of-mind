from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, current_user
from itsdangerous import BadSignature, SignatureExpired
from . import main
from .models import Post, User
from .forms import LoginForm, PostForm, SignupForm
from .. import db
from ..util import ts, send_email
from datetime import datetime


@main.route("/")
def index():
    # Get all post titles and texts
    ps = Post.query.all()
    posts = []
    for p in ps:
        posts.append(
            dict(
                id=p.id,
                title=p.title,
                video=p.video,
                text=p.content,
                private=p.private
            )
        )
    authenticated = current_user.is_authenticated
    return render_template("index.html", posts=posts, authenticated=authenticated)


@main.route("confirm/<token>")
def confirm_email(token):
    try:
        email = ts.loads(token, salt="email-confirm-key", max_age=86400)
    except BadSignature:
        abort(404)
    except SignatureExpired:
        abort(404)
    user = User.query.filter_by(email=email).first_or_404()

    user.confirmed = True

    db.session.add(user)
    db.session.commit()

    flash("Successfully confirmed your email!  Please log in.")
    return redirect(url_for('main.login'))


@main.route("signup/", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            plaintext=form.password.data
        )
        db.session.add(user)
        db.session.commit()

        subject = "Confirm your email"

        token = ts.dumps(user.email, salt="email-confirm-key")

        confirm_url = url_for(
            'main.confirm_email',
            token=token,
            _external=True
        )

        html = render_template(
            'email/activate.html',
            confirm_url=confirm_url
        )

        send_email(user.email, subject, html)

        flash("Successfully created a new user!")
        flash("Be sure to check your email to confirm your account")
        return redirect(url_for('main.index'))
    return render_template("signup.html", form=form)


@main.route("login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_user = User.query.filter_by(
            email=form.username.data
        ).first()
        if db_user and db_user.is_correct_password(form.password.data):
            if db_user.confirmed:

                login_user(db_user)
                # Redirect the user to the index
                flash("Successfully logged in!")
                return redirect(
                    request.args.get('next') or url_for('main.index')
                )
            else:
                flash("You must confirm your email address before logging in!")
                return redirect(url_for('main.login'))
        else:
            flash("Invalid credentials")
            return redirect(url_for('main.login'))
    return render_template("login.html", form=form)


@main.route("logout/")
@login_required
def logout():
    logout_user()
    flash("Successfully logged out!")
    return redirect(url_for("main.index"))


@main.route("about/")
def about():
    u=current_user.is_authenticated
    return render_template("about.html", user=u)


@main.route("post/<int:id>")
def post(id=None):
    # Get post matching the given ID, if any
    p = Post.query.get(id)
    if p is None:
        post = dict(title="This post does not exist", video="", text="")
    else:
        dt = datetime.strptime(str(p.pub_date), "%Y-%m-%d").strftime("%d-%b-%Y")
        post = dict(title=p.title, video=p.video, text=p.content, author=p.author, pub_date=dt)

    return render_template(
        "post.html",
        id=id,
        title=post["title"],
        url=post["video"],
        text=post["text"],
        pub_date=post["pub_date"],
        author=post["author"]

        )



@main.route("edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id=None):
    post = Post.query.get(id)
    title = post.title.capitalize()
    form = PostForm(
        title=title,
        author=post.author,
        publish_date=post.pub_date,
        video=post.video,
        content=post.content,
        private=post.private
    )
    if form.validate_on_submit():
        post.title = form.title.data
        post.author = form.author.data
        post.publish_date = form.publish_date.data
        if form.video.data:
            post.video = form.video.data
        else:
            post.video=None
        post.content = form.content.data
        post.private = form.private.data
        db.session.add(post)
        db.session.commit()

        flash("Successfully edited the post")
    return render_template(
        "edit.html", heading="Edit Existing Post", form=form, id=id
    )


@main.route("new/", methods=['GET', 'POST'])
@login_required
def new():
    form = PostForm()
    if form.validate_on_submit():
        if form.video.data:
            video=form.video.data
        else:
            video=None
        title = form.title.data.capitalize()
        new_post = Post(
            title=title,
            author=form.author.data,
            pub_date=form.publish_date.data,
            video=video,
            content=form.content.data,
            private=form.private.data
        )
        db.session.add(new_post)
        db.session.commit()
        flash("Successfully created a new post")
    return render_template("edit.html", heading="Create New Post", form=form)


@main.route("archive/")
def archive():
    ps = Post.query.all()
    posts = []
    for p in ps:
        dt = datetime.strptime(str(p.pub_date), "%Y-%m-%d").strftime("%d-%b-%Y")
        posts.append(dict(id=p.id, title=p.title, pub_date=dt))
    return render_template("archive.html", posts=posts)
