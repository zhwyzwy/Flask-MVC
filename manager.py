from application import app, manager
from flask_script import Server
import sys, www

manager.add_command("runserver", Server(host='0.0.0.0', port=8999, use_debugger=app.config['DEBUG'],
                                        use_reloader=True))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
