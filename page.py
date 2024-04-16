class Page:
    def __init__(self, id, title, status, tags, publish_type, link, markdown_path=None):
        self.id = id
        self.title = title
        self.status = status
        self.tags = tags
        self.publish_type = publish_type
        self.link = link
        self.markdown_path = markdown_path

    def __repr__(self):
        return (f"Page(id={self.id}, title={self.title}, status={self.status}, "
                f"tags={self.tags}, publish_type={self.publish_type}, "
                f"link={self.link}, markdown_path={self.markdown_path})")
