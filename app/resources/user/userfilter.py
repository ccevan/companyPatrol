
# from run import app
from . import user

@user.app_template_filter('lst')
def do_return_last(li):
    return li[3]


