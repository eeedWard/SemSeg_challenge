#!/usr/bin/env python
from duckietown_challenges import wrap_solution, ChallengeSolution, ChallengeInterfaceSolution


class Solver(ChallengeSolution):
    def run(self, cis):
        assert isinstance(cis, ChallengeInterfaceSolution)

        # guess = random.uniform(0, 100)
        guess = 51
        data = {'guess': guess}
        cis.set_solution_output_dict(data)


if __name__ == '__main__':
    wrap_solution(Solver())
