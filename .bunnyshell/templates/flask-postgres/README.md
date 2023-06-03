# Template overview

This template is a boilerplate for creating a new environment based on a stack using Flask backend and PostgreSQL database.

The template provides the Bunnyshell configuration composed of 2 Components (backend + database) and a Web application.

You can extend the template by further adding Components, be them more APIs or other services, such as queues, caches, block storage etc.

&nbsp;

# Environment overview

This environment is comprised of 2 components:

- `backend` for the backend based on Flask
- `database` for  PostgreSQL database

The Postgres DB **password** is configurable (by default is the value for the password is not set), and declared as a environment variable `dbpass` 