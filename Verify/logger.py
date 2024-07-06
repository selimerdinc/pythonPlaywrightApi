from colorama import Fore, Style

class Log:
    @staticmethod
    def test_pass():
        print(Fore.GREEN + "\nPASSED" + Style.RESET_ALL)