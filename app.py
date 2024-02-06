from bottle import default_app, get, run, static_file
###############
import routes.render_index
import x
###############
## Get CSS
@get("/CSS/budget.css")
def _():
    return static_file("budget.css", root="./CSS")

###############
try:
    import production
    application = default_app()
except Exception as ex:
    print("Running local server")
    run(host="127.0.0.1", port=2, debug=True, reloader=True, )
