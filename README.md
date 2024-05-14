# pouya-diagnostics

This is the beginning of our django-project. Structuring our project not only make things tidy, but also helps us in organizing our debugging strategy as well as our (modular) testing phase, so here it comes:

```
mkdir <app-name> && cd <app-name>
mkdir backend && cd backend
django-admin startproject config .
```

We, then, adopted another form of structuring when we consider the security of our project, by re-organizing our `settings.py` into `settings/base.py`, `settings/development.py`, and `settings/production.py`, as well as, making use of an `.env` file to push away our credentials and other sensitive informations (following a well-established security practice).