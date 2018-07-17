from . import dashboard


@dashboard.route("/")
def index():
    return "dashboard hello"