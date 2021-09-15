
# Family Time

Stay in touch with your family

## ERD

 ![erd](/img/family_time_erd.png)

## Structure

This template includes a project `family_time` which should be renamed
as part of the set-up steps. It includes the `settings.py` file with special
settings to be able to run both locally and on production. **DO NOT ADD A NEW
OR MODIFY THE CURRENT `DATABASES` DEFINITION UNLESS INSTRUCTED TO DO SO.**

There is also an app `api` which can be renamed if necessary. The `api` app
includes folders for models and view files, which can then be imported into
`urls.py` for use.

## Commands

Commands are run with the syntax `python3 manage.py <command>`:

| command | action |
|---------|--------|
| `runserver`  |  Run the server |
| `makemigrations`  | Generate migration files based on changes to models  |
| `migrate`  | Run migration files to migrate changes to db  |
| `startapp`  | Create a new app  |

## Deployment

Before deploying, make sure you have renamed your project folder and replaced
all instances of `family_time` with your app's name.

Once ready, you can follow the steps in the [django-heroku-deployment-guide](https://git.generalassemb.ly/ga-wdi-boston/django-heroku-deployment-guide).

## Connecting Client

This template is intentionally minimal, and does not override many of Django's
defaults. This means connecting either the `browser-template` or `react-auth-template` clients to this backend involves updating that client code slightly.

Ultimately, Django and any other backend API framework should be able to build
standalone backend APIs that can talk to any client. We just have to make sure
the client is following some of the expectations that Django has by default.

### Port

When working on our "local" computer, we work on the `localhost` location. This
is paired with a port number to identify where our server is running on our
local machine. Our client templates use port `7165`, for example, and run at
`http://localhost:7165`.

These templates also talk to a backend at a certain port, which is set to `4147`
in the client templates. **We need to change the port in the URL the client
application uses when running locally.**

In the `browser-template` this means modifying the `config.js` file, and in the
`react-auth-template` the `apiConfig.js` file.

This django template uses the port `8000` by default, so any client speaking to
this template's default server location would be `http://localhost:8000`.

### URL Syntax

Django defaults to expecting (and requiring) trailing forward slashes `/` on
requests. You'll need to make sure any requests you make from a client to this
template look something like `http://localhost:8000/books/`.

### Token Syntax

We've gotten used to the token syntax that the Express framework expects:

```
Bearer 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

However, the DRF [`TokenAuthentication`](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) class in this template is what defines
what our token syntax should look like when the client make an authenticated
request to our Django application.

When making authenticated requests from any client, make sure your tokens
follow this pattern:

```
Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

### Incoming Request Data

Our JavaScript conventions are to use `camelCase` when defining almost everything, however Python conventions (and therefore Django conventions) use
`snake_case` instead. We have to keep this in mind when sending data from a
client to a Django application.

### Handle JSON Data

> Note: This section is only necessary if you are connecting this template to
> the `browser-template` and/or using the `$.ajax` method.

### Stringify Your Request Data

When sending data with AJAX, we must stringify it with `JSON.stringify`. See the below example:

```js
const create = function (data) {
  return $.ajax({
    url: config.apiUrl + '/mangos/',
    method: 'POST',
    headers: {
      Authorization: 'Token ' + store.user.token
    },
    data: JSON.stringify(data)
  })
}
```

### Have Django Load the JSON Data

The `request.data` object becomes a QueryDict, and generally doesn't look the way we expect.

Instead of `request.data`, you must use `request.body`. We can then load the body as JSON with `json.loads`.

See the below (focusing on just the data) example:

```py
# Import the `json` module
import json

....

class Mangos(APIView):
    def post(self, request):
        # Create variable to store readable JSON data
        data = json.loads(request.body)
        # pass the now Dictionary to the serializer, doing whatever you need
        serializer = MySerializer(data=data['resource'])
.....

```

## Debugging

`pipenv shell` moved me into a different directory!

> Pipenv wants to be in the root directory, so if it thinks it's not then it
> will move you to what it thinks is the root of your repository. Exit out
> of the shell with `exit`, then check if the folder it moved you to is a git
> repository. If you see a `.git` folder inside of the `trainings` folder,
> for example, delete that folder so that `trainings` is no longer a "git repo."
> Then, you can change back into your project directory and try running
> `pipenv shell` again.

`pipenv shell` is complaining about my python version not matching

> Our python version is defined in the `Pipfile`. Simply replace the current
> `python_version = "x.x"` statement with the appropriate version.

SyntaxError pointing to `manage.py` when trying to run the server, migrate, etc.

> Double-check your python version with `python --version`. If you see a "2.x.x"
> version, then you need to use the command `python3` when running python
> scripts. You can also follow these guides to replace your `python` command so
> it always uses python3.
>
> Mac: https://stackoverflow.com/questions/49704364/make-python3-as-my-default-python-on-mac/49711594
>
> Linux: https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux

Error: No module named <my-projects-name> when trying to run the server

> If Python can't find the module that is your project name, then very likely
> you forgot a very important piece of the preparation steps. You need to
> make sure you rename the project folder as well.

I made changes to my models & ran my migrations but it says "No migrations to apply"

> Double-check that you **generated** the migration files before you tried
> to run them. This means running `makemigrations` before `migrate`.

Errors with `psycopg2`

> There's a lot to read about this issue if you want:
> https://github.com/psycopg/psycopg2/issues/674
> https://www.psycopg.org/articles/2018/02/08/psycopg-274-released/
>
> This template uses `psycopg2-binary` to minimize errors during project
> development. If you have errors with `psycopg2` anyway, notify an instructor.

## Additional Resources

- [Django Rest Framework Tutorial: Authentication](https://www.django-rest-framework.org/api-guide/authentication)

## [License](LICENSE)

1.  All content is licensed under a CC­BY­NC­SA 4.0 license.
1.  All software code is licensed under GNU GPLv3. For commercial use or
    alternative licensing, please contact legal@ga.co.
