from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str,
                 bow_level: int,
                 musical_instrument: str
                 ) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> None:
        return (
            f"Elf ranger {self.nickname}. "
            f"{self.nickname} has bow of the {self._bow_level} level"
        )

    def get_rating(self) -> None:
        return 3 * self._bow_level
