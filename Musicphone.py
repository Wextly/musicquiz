import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

# Список треков с прямыми ссылками на MP3
TRACKS = [
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "url": "https://p.scdn.co/mp3-preview/b05615d5e2a20b72baab986506f52e259e896696"
    },
    {
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "url": "https://p.scdn.co/mp3-preview/2b963b65288544c9cc5b1d497c2a71bf68c2aa5b"
    },
    {
        "title": "Levitating",
        "artist": "Dua Lipa",
        "url": "https://p.scdn.co/mp3-preview/081081fa49c31326fb128d506d3381fa1224bc68"
    },
    {
        "title": "Bad Guy",
        "artist": "Billie Eilish",
        "url": "https://p.scdn.co/mp3-preview/13a0c5c369527e02919d7d9b9a67475d40957b42"
    }
]

class MusicQuizGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        self.score = 0
        self.lives = 3
        self.time_left = 15
        self.current_sound = None
        self.timer_event = None

        # Панель жизней и очков
        self.info_label = Label(
            text=f"Жизни: ❤️ x {self.lives}  |  Очки: {self.score}",
            font_size='20sp',
            size_hint_y=0.1
        )
        self.add_widget(self.info_label)

        # Таймер
        self.timer_label = Label(
            text=f"Время: {self.time_left} сек",
            font_size='24sp',
            size_hint_y=0.15
        )
        self.add_widget(self.timer_label)

        # Кнопки вариантов ответа
        self.buttons_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=0.75)
        self.add_widget(self.buttons_layout)

        self.next_question()

    def next_question(self):
        if self.current_sound:
            self.current_sound.stop()
            self.current_sound.unload()

        if self.lives <= 0:
            self.game_over()
            return

        options = random.sample(TRACKS, k=4)
        self.correct_track = random.choice(options)

        # Запуск музыки по ссылке
        self.current_sound = SoundLoader.load(self.correct_track["url"])
        if self.current_sound:
            self.current_sound.play()

        # Сброс таймера
        self.time_left = 15
        self.timer_label.text = f"Время: {self.time_left} сек"
        if self.timer_event:
            self.timer_event.cancel()
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

        # Создаем кнопки
        self.buttons_layout.clear_widgets()
        for track in options:
            btn_text = f"{track['artist']} — {track['title']}"
            btn = Button(text=btn_text, font_size='18sp')
            btn.bind(on_release=lambda instance, t=track: self.check_answer(t))
            self.buttons_layout.add_widget(btn)

    def update_timer(self, dt):
        self.time_left -= 1
        self.timer_label.text = f"Время: {self.time_left} сек"
        if self.time_left <= 0:
            self.check_answer(None)

    def check_answer(self, selected_track):
        if self.timer_event:
            self.timer_event.cancel()

        if selected_track == self.correct_track:
            self.score += 100
        else:
            self.lives -= 1

        self.info_label.text = f"Жизни: ❤️ x {self.lives}  |  Очки: {self.score}"
        self.next_question()

    def game_over(self):
        self.buttons_layout.clear_widgets()
        self.timer_label.text = "ИГРА ОКОНЧЕНА!"
        final_label = Label(text=f"Ваш итоговый счет: {self.score}", font_size='22sp')
        self.buttons_layout.add_widget(final_label)

        restart_btn = Button(text="Играть заново", font_size='20sp', size_hint_y=0.3)
        restart_btn.bind(on_release=self.restart_game)
        self.buttons_layout.add_widget(restart_btn)

    def restart_game(self, instance):
        self.score = 0
        self.lives = 3
        self.info_label.text = f"Жизни: ❤️ x {self.lives}  |  Очки: {self.score}"
        self.next_question()

class QuizApp(App):
    def build(self):
        return MusicQuizGame()

if __name__ == '__main__':
    QuizApp().run()