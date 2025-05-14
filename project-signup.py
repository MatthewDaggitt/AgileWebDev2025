from flask_migrate import Migrate
from app import create_application, db
from app.config import DeploymentConfig

if __name__ == "__main__":
    application = create_application(DeploymentConfig)
    migrate = Migrate(application, db)
    application.run(debug=True, use_debugger=False, use_reloader=False)