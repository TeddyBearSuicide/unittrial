from unittrial.console import Console


class logger(object):

    _log: list = []

    @staticmethod
    def _indent_and_print():
        Console.indention += 1
        Console.writeLines(logger.getLog())
        Console.indention -= 1

    @staticmethod
    def getLog():
        logs = logger._log.copy()
        logger._log.clear()
        return logs

    @staticmethod
    def critical(msg):
        logger._log.append(
            f"{Console.BrightWhite}[{Console.BrightWhite + Console.BackgroundRed}CRITICAL{Console.Reset}{Console.BrightWhite}] {msg}"
        )

    @staticmethod
    def debug(msg):
        logger._log.append(
            f"{Console.BrightWhite}[{Console.BrightCyan}DEBUG{Console.BrightWhite}] {msg}"
        )

    @staticmethod
    def error(msg):
        logger._log.append(
            f"{Console.BrightWhite}[{Console.BrightRed}ERROR{Console.BrightWhite}] {msg}"
        )

    @staticmethod
    def info(msg):
        logger._log.append(
            f"{Console.BrightWhite}[{Console.BrightBlue}INFO{Console.BrightWhite}] {msg}"
        )

    @staticmethod
    def warning(msg):
        logger._log.append(
            f"{Console.BrightWhite}[{Console.BrightYellow}WARNING{Console.BrightWhite}] {msg}"
        )

