class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
        self.is_active = True

    def get_profile(self):
        return f"Usuario: {self.username} | Email: {self.email} | Estado: {'Activo' if self.is_active else 'Inactivo'}"

    def set_password(self, new_password):
        if len(new_password) >=8:
            self.__password = new_password
            print("Contrasena actualizada con exito.")
            else:
                print("La contrasena debe tener al menos 8 caracteres")

        user1 = User("ana_dev", "ana@gmail.com", "femboy")
        print(user1.get_profile())