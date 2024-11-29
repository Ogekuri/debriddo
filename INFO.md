
# Development Info

# Version, repository and deplyoment

The APPLICATION_VERSION in constant.py contain the version on x.y.z style.

The master tags follow the same APPLICATION_VERSION's syntax preceded by a 'v' (like v1.2.3).

A new docker image is build on every tag that start with 'v' (see the .github/workflow/release.yml file)

## TODO

### Implementations

* CORSMiddleware change origins

### Tests

* NO_CACHE_VIDEO_URL = "https://github.com/Ogekuri/debriddo/raw/main/videos/nocache.mp4"
