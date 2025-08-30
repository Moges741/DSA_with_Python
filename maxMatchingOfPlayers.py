class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        
        i, j = 0, 0  # pointers for players and trainers
        matches = 0
        
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                # match found
                matches += 1
                i += 1
                j += 1
            else:
                # trainer too weak, move to stronger trainer
                j += 1
        
        return matches
