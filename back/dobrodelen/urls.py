from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin
from django.shortcuts import get_object_or_404

from wagtail.documents import get_document_model
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls


def docs_serve_id(request, document_id, document_filename):
    Document = get_document_model()
    doc = get_object_or_404(Document, id=document_id)
    return wagtaildocs_urls.serve.serve(request, document_id, doc.filename)


urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    # custom document serve function that does not need exact file name
    re_path(r"^documents/(\d+)/(.*)$", docs_serve_id, name="docs_serve_id"),
    path("documents/", include(wagtaildocs_urls)),
    path("api/", include("home.urls")),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
