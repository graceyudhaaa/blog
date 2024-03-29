import pymongo

class Home:
    def __init__(self, app):
        self.app = app

    def get_post_limit(self, n, query={}, filter=None):
        return list(
            self.app.db["posts"]
            .find(query,filter,)
            .limit(n)
            .sort("last_modified", pymongo.DESCENDING)
        )

    def get_post(self, query={}, filter=None):
        return list(
            self.app.db["posts"]
            .find(
                query,
                filter,
            )
            .sort("created_at", pymongo.DESCENDING)
        )

    # def get_all_active_category()
