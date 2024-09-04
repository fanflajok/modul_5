import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.age = int(age)
        self.password = hash(password)
    def __str__(self):
        return self.nickname
class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = 0
        self.adult_mode = adult_mode
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname and hash(password) == i.password:
                self.current_user = i
                return i.nickname
        else:
            print ("Никнейм или пароль неверный")
    def register(self, nickname, password, age):
        new_user1 = User(nickname, password, age)
        for user in self.users:
            if new_user1.nickname in user.nickname:
                print(f"Пользователь {new_user1.nickname} уже существует")
        else:
            self.users.append(new_user1)
            self.current_user = new_user1
    def log_out(self):
        self.current_user = None
    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)
    def get_videos(self, new_search):
        founded_videos = []
        for i in self.videos:
            if new_search.lower() in i.title.lower():
                founded_videos.append(i.title)
        if not founded_videos:
            return "Видео не найдено, введите запрос иначе"
        else:
            return founded_videos
    def watch_video(self, name_of_movie):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for i in self.videos:
           if i.title == name_of_movie and i.adult_mode and self.current_user.age >= 18:
               for j in range(i.duration):
                   print(j+1, end=" ")
                   time.sleep(1)
               print("Конец видео")
        for i in self.videos:
           if i.title == name_of_movie and not i.adult_mode:
               for j in range(i.duration):
                   print(j+1, end=" ")
                   time.sleep(1)
               print("Конец видео")
        for i in self.videos:
           if i.title == name_of_movie and i.adult_mode and self.current_user.age < 18:
               print("Вам нет 18 лет, пожалуйста покиньте страницу")
UR = UrTube()
v1 = Video("Спидран Super Mario bros Wonder - разбор багов финального уровня", 10)
v2 = Video("Почему DOOM запускается, даже на картошке или почему Кармак - гений?", 20)
v3 = Video("История компании Nintendo: от игральных карт, до лидера игровой индустрии", 30)
v4 = Video('История компании Sony: от инноваций к "повесточке"', 10, adult_mode = True)
v5 = Video("Лучшие языки программирования для учёбы в 2024 году", 15)
UR.add(v1, v2, v3, v4, v5)
print(UR.get_videos("история"))
UR.register("fanflajok","bgakbhvlivfdba", 32)
UR.register("pandawa","4567ujhgfdr567uj", 20)
UR.register("sadida","giuvl", 17)
UR.register("xelor","kbb", 15)
UR.log_in("sadida", "giuvl")
UR.watch_video('История компании Sony: от инноваций к "повесточке"')





