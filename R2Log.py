import logging
from typing import Any, cast

from rich.console import Console
from rich.logging import RichHandler


# Customized logging class
class R2Log(logging.Logger):
    """Project's Logger custom class"""
    # New logging level
    CRITICAL: int = logging.CRITICAL  # 50
    ERROR: int = logging.ERROR  # 40
    WARNING: int = logging.WARNING  # 30
    SUCCESS: int = 25
    INFO: int = logging.INFO  # 20
    VERBOSE: int = 15
    ADVANCED: int = 13
    DEBUG: int = logging.DEBUG  # 10

    @staticmethod
    def setVerbosity(verbose_level: int = 0, quiet: bool = False):
        """
        Set logging level accordingly to the verbose count or with quiet enable.
        Args:
            verbose_level: Set the verbosity level: 1 = Verbose, 2 = Advanced, 3 = Debug
            quiet: If true, set the verbosity to critical messages only.

        Returns:

        """
        if quiet:
            logger.setLevel(logging.CRITICAL)
        elif verbose_level == 1:
            logger.setLevel(R2Log.VERBOSE)
        elif verbose_level == 2:
            logger.setLevel(R2Log.ADVANCED)
        elif verbose_level >= 3:
            logger.setLevel(logging.DEBUG)
        else:
            # Default INFO
            logger.setLevel(logging.INFO)

    def debug(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Change default debug text format with rich color support"""
        super(R2Log, self).debug("{}[D]{} {}".format("[bold yellow3]", "[/bold yellow3]", msg), *args, **kwargs)

    def advanced(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Add advanced logging method with text format / rich color support"""
        if self.isEnabledFor(R2Log.ADVANCED):
            self._log(R2Log.ADVANCED,
                      "{}[A]{} {}".format("[bold yellow3]", "[/bold yellow3]", msg), args, **kwargs)

    def verbose(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Add verbose logging method with text format / rich color support"""
        if self.isEnabledFor(R2Log.VERBOSE):
            self._log(R2Log.VERBOSE,
                      "{}[V]{} {}".format("[bold blue]", "[/bold blue]", msg), args, **kwargs)

    def raw(self, msg: Any, level=VERBOSE, markup=False, highlight=False, emoji=False, rich_parsing=False) -> None:
        """Add raw text logging, used for stream printing."""
        if rich_parsing:
            markup = True
            highlight = True
            emoji = True
        if self.isEnabledFor(level):
            if type(msg) is bytes:
                msg = msg.decode('utf-8', errors="ignore")
            # Raw message are print directly to the console bypassing logging system and auto formatting
            console.print(msg, end='', markup=markup, highlight=highlight, emoji=emoji)

    def info(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Change default info text format with rich color support"""
        super(R2Log, self).info("{}[*]{} {}".format("[bold blue]", "[/bold blue]", msg), *args, **kwargs)

    def warning(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Change default warning text format with rich color support"""
        super(R2Log, self).warning("{}[!]{} {}".format("[bold orange3]", "[/bold orange3]", msg), *args, **kwargs)

    def error(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Change default error text format with rich color support"""
        super(R2Log, self).error("{}[-]{} {}".format("[bold red]", "[/bold red]", msg), *args, **kwargs)

    def exception(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Change default exception text format with rich color support"""
        super(R2Log, self).exception("{}[x]{} {}".format("[bold red]", "[/bold red]", msg), *args, **kwargs)

    def critical(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Change default critical text format with rich color support
        Add auto exit."""
        super(R2Log, self).critical("{}[!]{} {}".format("[bold red]", "[/bold red]", msg), *args, **kwargs)
        exit(1)

    def success(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Add success logging method with text format / rich color support"""
        if self.isEnabledFor(R2Log.SUCCESS):
            self._log(R2Log.SUCCESS,
                      "{}[+]{} {}".format("[bold green]", "[/bold green]", msg), args, **kwargs)

    def empty_line(self, log_level: int = logging.INFO) -> None:
        """Print an empty line."""
        import os
        self.raw(os.linesep, level=log_level)


# Global rich console object
console: Console = Console()

# Main logging default config
# Set default Logger class as R2Log
logging.setLoggerClass(R2Log)

# Add new level to the logging config
logging.addLevelName(R2Log.VERBOSE, "VERBOSE")
logging.addLevelName(R2Log.SUCCESS, "SUCCESS")
logging.addLevelName(R2Log.ADVANCED, "ADVANCED")
# Logging setup using RichHandler and minimalist text format
logging.basicConfig(
    format="%(message)s",
    handlers=[RichHandler(rich_tracebacks=True,
                          show_time=False,
                          markup=True,
                          show_level=False,
                          show_path=False,
                          console=console)]
)

# Global logger object
logger: R2Log = cast(R2Log, logging.getLogger("main"))
# Default log level
logger.setLevel(logging.INFO)
