from flask import Flask
from flask_restx import Api, Resource,fields
from .criptosocket.service       import criptosocket_bp,ns_criptosocket


app = Flask (__name__)


# Creación del objeto api de CriptoSocket
api = Api(app,version="1.0",title="ApiRest CriptoSocket", description="API Rest TFG Criptosocket",contact="" )

# Añadir objeto namespace de criptosocket
api.add_namespace(ns_criptosocket)

# Añadir endpoint service
app.register_blueprint(criptosocket_bp)



if __name__ == "__main__":
      app.run()

   