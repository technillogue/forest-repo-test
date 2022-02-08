from forest.core import Bot, Message, run_bot

class SomeBot(Bot):
    def do_hi(self, msg: Message) -> stR:
        return "hi"

if __name__ == "__main__":
    run_bot(SomeBot)

