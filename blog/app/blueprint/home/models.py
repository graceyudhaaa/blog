import pymongo

# recent_post = list(
#         current_app.db["posts"]
#         .find(
#             {"is_active": True},
#             {
#                 "_id": 0,
#                 "title": 1,
#                 "slug": 1,
#                 "created_at": 1,
#             },
#         )
#         .sort("created_at", pymongo.DESCENDING)
#     )


class Home:
    def __init__(self, app):
        self.app = app

    def get_post_limit(self, n, query={}):
        return list(
            self.app.db["posts"]
            .find(query)
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
