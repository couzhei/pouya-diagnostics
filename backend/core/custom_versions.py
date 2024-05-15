from rest_framework.versioning import URLPathVersioning


class DefaultCoreAppVersion(URLPathVersioning):
    allowed_versions = ["v1"]
    version_param = "version"
