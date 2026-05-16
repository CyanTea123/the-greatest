class HeYiWei(OverflowError):
    def __init__(self, heyiwei):
        super().__init__(heyiwei)

if __name__ == "__main__":
    raise HeYiWei("何意味")