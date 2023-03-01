# 0x02. i18n

`Back-end`

![meme](./images/meme.jpeg)

## Resources

**Read or Watch**

- [Flask-Babel](https://intranet.alxswe.com/rltoken/fBpGjDt2BFuBFiz-jwublQ)

- [Flask i18n tutorial](https://intranet.alxswe.com/rltoken/RtGz7pI7TKnYqrMMG9rWMg)

- [pytz](https://intranet.alxswe.com/rltoken/7rrCz4pkpqAn4FfRZ2Vsvw)

## Learning Objectives

- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings or request headers
- Learn how to localize timestamps

## Tasks

### 0. Basic Flask app

First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

solution - [0-app.py](./0-app.py), [templates/0-index.html](./templates/0-index.html)

### 1. Basic Babel setup

Install the Babel Flask extension:

```bash
pip3 install flask_babel
```

Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.

solution - [1-app.py](./1-app.py), [templates/1-index.html](./templates/1-index.html)

### 2. Get locale from request

Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

solution - [2-app.py](./2-app.py), [templates/2-index.html](./templates/2-index.html)

### 3. Parametrize templates

Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file containing

```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_

```

Then initialize your translations with

```shell
$ pybabel extract -F babel.cfg -o messages.pot .
```

and your two dictionaries with

```shell
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```

Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po `to provide the correct value for each message ID for each language. Use the following translations:

| msgid | English | French |
| ----- | ------- | ------ |
| home_title | "Welcome to Holberton" | "Bienvenue chez Holberton" |
| home_header | "Hello world!" | "Bonjour monde!" |

Then compile your dictionaries with

```
$ pybabel compile -d translations
```

Reload the home page of your app and make sure that the correct messages show up.


