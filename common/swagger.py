from drf_spectacular.openapi import AutoSchema as BaseAutoSchema


class AutoSchema(BaseAutoSchema):

    def get_tags(self):
        tags = getattr(self.view, 'swagger_tags', None)

        if not tags:
            tokenized_path = self._tokenize_path()
            # use first non-parameter path part as tag
            tags = tokenized_path[:1]

        return tags
