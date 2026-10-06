from detetime import detetime

class Comment:
    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.created_at = detetime.now().strtime("%Y-%m-%d %H:%M")
        self.likes = 0

    def add_like(self):
        self.likes += 1

    def get_comment_info(self):
        return f"[{self.created_at}] {self.author.username}: {self.text} ({self.likes})"

class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = detetime.now(.strtime("%H:%M"))
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def display_message(self):
        status = "Visto" if self.is_read else "Entregado"
        return f"[{self.timestamp}] de {self.sender.username} para {self.recipient.username}: \"{self.content}\" ({status})"


        user1 = User("ana_dev", "ana@gmail.com", "femboy")
        user2 = User("carlos", "carlos@gmail.com", "pas123")

        nuevo_comentario = Comment(author=user2, text="excelente explicacion")
        nuevo_comentario.add_like()
        print(nuevo_comentario.get_comment_info())

        mensaje_privado = Message(sender=user1, recipient=user2, content="hola carlos tonto")
        print(mensaje_privado.display_message())

        mensaje_privado.mark_as_read()
        print(message_privado.display_message())