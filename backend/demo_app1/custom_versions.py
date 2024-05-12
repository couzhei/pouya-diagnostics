from rest_framework.versioning import URLPathVersioning


class DefaultDemoAppVersion(URLPathVersioning):
    allowed_versions = ["v1"]
    version_param = "version"


class DemoViewVersion(DefaultDemoAppVersion):
    allowed_versions = ["v1", "v2", "v3"]


class AnotherViewVersion(DefaultDemoAppVersion):
    allowed_versions = ["v1", "v2"]


# Let’s see what the preceding code does:

#     The DefaultDemoAppVersion class can be used for all the views that are created in demo_app.
# It has an allowed_versions attribute that lists all the allowed versions that can be used in
# the URL path whenever we use this class-based view. version_param is the URL path parameter
# name that we have used to define the version; it can be anything, depending on how
# you name the parameter, but in our case, we are using <version>, which is used in
# the config/urls.py file. This class will be used for all the views that are
# created in the demo app by default until a new version is added, after
# which we will create an individual class, as shown next.

#     The DemoViewVersion class will contain the list of all the allowed_versions attributes
# for DemoView that are allowed in the URL path.

#     The AnotherViewVersion class will contain all the versions that are allowed
# for a different class.
