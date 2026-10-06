class Post:
    def __init__(self, title, content, author):

        self.title = title
        self.content = content
        self.author = author
        self.likes = 0
        self.comments = []

        def add_like(self):
            self.likes += 1

            def add_comment(self, comment):
                self.comments.append(comment)

                def display_post(self):
                    print(f"---{self.title}---")
                    print(f"Por: {self.author.username}")
                    print(f"\n{self.content}\n")
                    print(f"Likes: {self.likes} | Comentarios: {len(self.comments)}")

                    if self.comments:
                        print("\nComentarios:")
                        for comment in self.comments:
                            print(f" - {comment}")


                    user1 = User("ana_dev", "ana@gmail.com", "femboy123")

                    post1 = Post("Mi primer post" user1)

                    post1.add_like()
                    post1.add_like()

                    post1.add_comment("nsienjkern")
                    post1.add_comment("jndjcoifew")

                    post1.display_post()
