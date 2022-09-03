import glob


def cli_commands(app):
    @app.cli.command("initdb")
    def initdb():
        print("Database is migrating")
        # TODO: sort files for priority
        files = glob.glob("./models/*.sql")
        for file in files:
            command = open(file, "r").read()
            print(command)
            # TODO: run command from database
    return app
