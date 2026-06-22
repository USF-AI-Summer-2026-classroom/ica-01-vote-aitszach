from candidate import Candidate
from voter import Voter
from priority_queue import PriorityQueue

import random


class VotingSystem:

    def __init__(self):
        self.candidates = []
        self.voters = []
        self.rankings = {}

    def generate_candidates(self, count):
        names = [
            'Aang', 'Katara', 'Sokka', 'Zuko', 'Iroh',
            'Appa', 'Momo', 'Toph', 'Azula', 'Suki',
            'Ozai', 'Mai', 'Ty'
        ]

        self.candidates = [
            Candidate(
                name=names[i],
                leaning=random.uniform(-1.0, 1.0)
            )
            for i in range(count)
        ]

    def generate_voters(self, count):
        self.voters = [
            Voter(
                id=i + 1,
                leaning=random.uniform(-1.0, 1.0)
            )
            for i in range(count)
        ]

    def create_rankings(self):

        for voter in self.voters:

            pq = PriorityQueue()

            for candidate in self.candidates:

                distance = abs(
                    voter.leaning -
                    candidate.leaning
                )

                pq.enqueue(
                    candidate,
                    distance
                )

            self.rankings[voter.id] = pq

    def get_vote(self, voter, eliminated):

        for candidate in self.rankings[voter.id]:

            if candidate.name not in eliminated:
                return candidate

        return None

    def run_election(self):

        self.create_rankings()

        eliminated = set()
        round_number = 1

        while True:

            print(f"\n===== ROUND {round_number} =====")

            vote_counts = {}

            for candidate in self.candidates:
                if candidate.name not in eliminated:
                    vote_counts[candidate.name] = 0

            for voter in self.voters:

                vote = self.get_vote(
                    voter,
                    eliminated
                )

                if vote:
                    vote_counts[vote.name] += 1

            total_votes = sum(vote_counts.values())

            winner = None

            for candidate_name, votes in vote_counts.items():

                percentage = (
                    votes / total_votes
                ) * 100

                print(
                    f"{candidate_name}: "
                    f"{votes} votes "
                    f"({percentage:.2f}%)"
                )

                if percentage > 50:
                    winner = candidate_name

            if winner:
                print(f"\nWINNER: {winner}")
                return

            loser = min(
                vote_counts,
                key=vote_counts.get
            )

            print(f"\nEliminated: {loser}")

            eliminated.add(loser)

            round_number += 1


if __name__ == "__main__":

    voting_system = VotingSystem()

    voting_system.generate_candidates(5)
    voting_system.generate_voters(100)

    print("Candidates:")
    for candidate in voting_system.candidates:
        print(candidate)

    voting_system.run_election()