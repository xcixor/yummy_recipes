"""Initialize set up for heroku"""

from myapp import create_app

import os

app = create_app('default')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
 