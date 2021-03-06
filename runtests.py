import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)


from django.test.utils import get_runner
from django.conf import settings
try:
    from django.apps import apps
    apps.populate(settings.INSTALLED_APPS)
except ImportError:
    # Old Django versions do not need such initialisation.
    pass


def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['mail_templated'])
    sys.exit(bool(failures))


if __name__ == '__main__':
    runtests()
