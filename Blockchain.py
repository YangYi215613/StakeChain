from Block import Block


class Blockchain:

    def __init__(self):
        self.blocks = [Block.genesis()]

    def addBlock(self, block):
        self.blocks.append(block)

    def toJson(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data['blocks'] = jsonBlocks
        return data
