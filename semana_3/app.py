import web

urls = (
    '/(.*)', 'tax.controllers.visitas.Visitas'
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()