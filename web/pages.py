# VERSION: 0.0.32
# AUTHORS: Ogekuri

def get_index(app_name, app_version, app_environment):
    with open("web/index.html", 'r', encoding='utf-8') as file:
        index = file.read()
        index = index.replace( "$APP_NAME", app_name )
        index = index.replace( "$APP_VERSION", app_version )
        index = index.replace( "$APP_ENVIRONMENT", app_environment )
        return index
    error = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Error - Page Not Found</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f8f9fa;
                color: #333;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            h1 {
                font-size: 4rem;
                margin: 0;
            }
            p {
                font-size: 1.5rem;
                margin: 10px 0;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                font-size: 1rem;
                color: #fff;
                background-color: #007bff;
                text-decoration: none;
                border-radius: 5px;
            }
            a:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h1>404</h1>
        <p>Oops! The page you're looking for doesn't exist.</p>
        <a href="/">Go Back Home</a>
    </body>
    </html>
    """
    return error

