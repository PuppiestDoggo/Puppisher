import os

from pynput_robocorp import keyboard, mouse  # https://github.com/moses-palmer/pynput


class SupressInput:
    def __init__(self):
        self.key_combination = '!'
        self.hotkey = keyboard.HotKey(keyboard.HotKey.parse(self.key_combination), self.enable_all)

    def disable_all(self):
        """Disable mouse and keyboard events"""

        with mouse.Listener(suppress=True) as self.mouse_listener, \
                keyboard.Listener(suppress=True,
                                  on_press=self.for_canonical(self.hotkey.press),
                                  on_release=self.for_canonical(self.hotkey.release)) as self.keyboard_listener:
            self.mouse_listener.join()
            self.keyboard_listener.join()

    def show_unblock_message(self):
        print()
        print(f'Push {self.key_combination} to unblock mouse and keyboard input...')

    def enable_all(self):
        """Enable mouse and keyboard events"""

        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        os.system("killall python")
        return False

    def for_canonical(self, f):
        return lambda k: f(self.keyboard_listener.canonical(k))


def main():
    supress_input = SupressInput()
    supress_input.show_unblock_message()
    supress_input.disable_all()


if __name__ == '__main__':
    main()
