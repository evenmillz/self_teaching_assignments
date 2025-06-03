import connexion

# Create the Connexion app
app = connexion.App(__name__, specification_dir='.')
app.add_api(
    "openapi.yaml",
    strict_validation=True,
    swagger_ui=True,
    swagger_url="/v1/ui"  # Mounts Swagger UI at /v1/ui
)

application = app.app  # Expose the underlying Flask app (for some ASGI servers)

if __name__ == "__main__":
    # No reload in script-based run — that's for ASGI (like uvicorn CLI)
    app.run(port=5000)