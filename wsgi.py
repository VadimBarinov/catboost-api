import sys
import os

project_home = os.path.dirname(os.path.abspath(__file__))
if project_home not in sys.path:
	sys.path.insert(0, project_home)

from app import create_app
from config import settings

application = create_app()

if __name__ == "__main__":
	application.run(
		host=settings.run.host,
		port=settings.run.port,
		debug=True,
  )